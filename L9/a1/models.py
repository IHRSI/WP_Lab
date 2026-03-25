from django.db import models

class Institute(models.Model):
	institute_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=150)
	no_of_courses = models.PositiveIntegerField()

	class Meta:
		db_table = 'Institutes'

	def __str__(self):
		return self.name
