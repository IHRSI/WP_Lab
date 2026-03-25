from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=100, unique=True)
	visits = models.PositiveIntegerField(default=0)
	likes = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.name


class Page(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='pages')
	title = models.CharField(max_length=150)
	url = models.URLField(max_length=300)
	views = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.title
