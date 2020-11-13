from django.db import models

class Details(models.Model):
	Name=models.CharField(max_length=25)
	Email=models.EmailField(max_length=30)
	About=models.TextField()

	