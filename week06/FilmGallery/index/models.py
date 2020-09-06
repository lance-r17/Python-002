from django.db import models

# Create your models here.
# 电影
class Film(models.Model):
    # id = models.AutoField(primary_key=True)  # Django会自动创建,并设置为主键
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    director = models.CharField(max_length=50)
    actors = models.CharField(max_length=200)
    categories = models.CharField(max_length=100)
    language = models.CharField(max_length=20)
    imdbname = models.CharField(max_length=20)
    imdburl = models.CharField(max_length=100)
    imageurl = models.CharField(max_length=200)

# 短评
class Comment(models.Model):
    author = models.CharField(max_length=20)
    content = models.CharField(max_length=1000)
    stars = models.IntegerField()
    commenttime = models.CharField(max_length=20)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    class Meta:
        ordering = ['commenttime']