from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.name)


class User(models.Model):
    name = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.name)


class Task(object):
    def __init__(self, **kwargs):
        for field in ('id', 'name', 'owner', 'status'):
            setattr(self, field, kwargs.get(field, None))


class Tasklist(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)


class Task(models.Model):
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    completed = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    date_modified = models.DateField(auto_now=True)
    tasklist = models.ForeignKey(Tasklist, related_name='tasks', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='tags')

    PRIORITY = (
        ('h', 'High'),
        ('m', 'Medium'),
        ('l', 'Low'),
        ('n', 'None')
    )

    priority = models.CharField(max_length=1, choices=PRIORITY, default='n')

    def __str__(self):
        return "{}".format(self.name)
