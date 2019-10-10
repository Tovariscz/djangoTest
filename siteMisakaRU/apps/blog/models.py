import datetime
from django.db import models

from django.utils import timezone

class Article(models.Model):
	title = models.CharField("Название статьи", max_length=100)
	text = models.TextField("Текст", max_length=10000)
	pub_date = models.DateTimeField("Время публикации", auto_now_add=True)
	
	def __str__(self):
		return self.title

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	author = models.CharField("Автор комментария", max_length=50)
	text = models.CharField("Текст комментария", max_length=500)
	like = models.PositiveSmallIntegerField("Лайки")

	def __str__(self):
		return str(self.article) + " <-- " + self.author + ": " + self.text