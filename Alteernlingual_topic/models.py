from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField

from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import  reverse

class Topic(models.Model):
    title = models.CharField(_("title"), max_length=150)
   
    main_explanations = RichTextUploadingField(null=True, blank=True, default=None)
   
    EN_explanations = RichTextUploadingField(null=True, blank=True, default=None)
    
   
    def __str__(self):
        return self.title
 
    def get_url(self):
       return reverse('detail', args=[self.id])


