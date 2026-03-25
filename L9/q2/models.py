from django.db import models

class Lives(models.Model):
	person_name = models.CharField(max_length=100, primary_key=True)
	street = models.CharField(max_length=150)
	city = models.CharField(max_length=100)

	class Meta:
		db_table = 'LIVES'

	def __str__(self):
		return f"{self.person_name} - {self.city}"


class Works(models.Model):
	person_name = models.CharField(max_length=100)
	company_name = models.CharField(max_length=100)
	salary = models.DecimalField(max_digits=12, decimal_places=2)

	class Meta:
		db_table = 'WORKS'

	def __str__(self):
		return f"{self.person_name} @ {self.company_name}"
