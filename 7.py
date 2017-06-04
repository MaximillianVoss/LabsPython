from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from sqlalchemy import Column, String, Integer


class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    url = Column(String)
    comments = Column(Integer)
    points = Column(Integer)
    label = Column(String)


def parsePage():
    import requests
    r = requests.get("https://news.ycombinator.com/")
    if (r.ok):
        from bs4 import BeautifulSoup
        return BeautifulSoup(r.text, 'html.parser')
    else:
        from bs4 import BeautifulSoup
        return BeautifulSoup('', 'html.parser')


def get_news(page):
    # item = {'author': ,'comments': ,'points': ,'title': ,'url': }
    # arr =[]
    # arr.append(item)
    # arr.append(item)
    # print(arr)
    tbl_list = page.table.findAll('table')
    if (len(tbl_list) > 1):
        rows = tbl_list[1].findAll('tr')
        items = []
        item = {}
        for row in rows:
            if len(row.attrs) > 0:
                if row.attrs['class'] == ['athing']:
                    id=''
                    auth=''
                    title=''
                    url=''
                    if row.find('span', {'class': 'rank'}) is not None:
                        id = row.find('span', {'class': 'rank'}).text
                    if row.find('span', {'class': 'sitestr'}) is not None:
                        auth = row.find('span', {'class': 'sitestr'}).text
                    if  row.find('a', {'class': 'storylink'}) is not None:
                        title = row.find('a', {'class': 'storylink'}).text
                    if row.find('a', {'class': 'storylink'}) is not None:
                        url =row.find('a', {'class': 'storylink'}).get('href')

                    item = {
                        'id' : id,
                        'author': auth,
                        'comments': '',
                        'points': '',
                        'title': title,
                        'url': url
                    }
            else:
                if row.find('td', {'class': 'subtext'}) is not None:
                    score = row.find('td', {'class': 'subtext'}).find('span', {'class': 'score'})
                    if score is not None:
                        item['points'] = score.text
                    comments = row.find('td', {'class': 'subtext'}).find_all('a')[-1]
                    if comments is not None:
                        item['comments'] = comments.text
                    items.append(item)
    return items


def getSession():
    from sqlalchemy import create_engine
    engine = create_engine("sqlite:///news.db")
    Base.metadata.create_all(bind=engine)
    from sqlalchemy.orm import sessionmaker
    session = sessionmaker(bind=engine)
    s = session()
    return s


def addItems(s, items):
    for item in items:
        news = News(title=item['title'],
                    author=item['author'],
                    url=item['url'],
                    comments=item['comments'],
                    points=item['points']
                    )
        s.add(news)
        s.commit()
    return

#s = getSession()
#addItems(s, get_news(parsePage()))

from bottle import route, run, template
from bottle import redirect, request


@route('/news')
def news_list():
    s = getSession()
    rows = s.query(News).filter(News.label == None).all()
    return template('news_template', rows=rows)


@route('/add_label/')
def add_label():
    # 1. Получить значения параметров label и id из GET-запроса
    label = request.query['label']
    id = request.query['id']
    s = getSession()
    # 2. Получить запись из БД с соответствующим id (такая запись только одна!)
    for item in s.query(News).filter(News.id == id).all():
        # 3. Изменить значение метки записи на значение label
        item.label = label
    # 4. Сохранить результат в БД
    s.commit()
    redirect('/news')


@route('/update_news')
def update_news():
    # 1. Получить данные с новостного сайта
    s = getSession()
    news = get_news(parsePage())
    # 2. Проверить каких новостей еще нет в БД. Будем считать,
    # что каждая новость может быть уникально идентифицирована
    # по совокупности двух значений: заголовка и автора
    for item in news:
        if (len(s.query(News).filter(News.title == item['title'], News.author == item['author']).all()) == 0):
            news = News(title=item['title'],
                        author=item['author'],
                        url=item['url'],
                        comments=item['comments'],
                        points=item['points']
                        )
            s.add(news)
            # 3. Сохранить в БД те новости, которых там нет
            s.commit()
    redirect('/news')


run(host='localhost', port=8080)
