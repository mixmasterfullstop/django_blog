from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(null=False,max_length=100)
    content= models.TextField()
    image = models.ImageField(upload_to='postimages')
    url = models.URLField(blank=True)
    date_posted = models.DateTimeField(auto_now=True)

