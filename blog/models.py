from django.conf.urls import url
from django.db import models

# create a Blog models
# title , pub_date, body , image 
# add the Blog app to the settings
# create a migration
# migrate 
# add to the admin

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')