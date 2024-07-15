from django.db import models
from django.utils import timezone


# Create your models here.

class Contact(models.Model):
	first_name = models.CharField(max_length = 100)
	second_name = models.CharField(max_length = 100)
	email = models.EmailField() 
	mobile = models.CharField(max_length = 10)
	message = models.TextField()
	date = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.first_name 


class Product(models.Model):
    name = models.CharField(max_length=100)
    manufacture = models.CharField(max_length=200)
    img = models.ImageField(null = True, blank = True)
    descriptions = models.CharField(max_length=200)
    price = models.FloatField()
    sale = models.IntegerField(null = True, blank = True)
    date = models.DateTimeField(auto_now_add = True)
	#slug = models.SlugField()

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try :
            url = self.img.url
        except:
        	url = ''
        return url
