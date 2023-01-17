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
    read_by = models.ManyToManyField(User, related_name='read_topics', blank=True)    
    
 
    # def get_url(self):
    #    return reverse('detail', args=[self.id])


class PolicyConditions(models.Model):
    privacy_policy = RichTextUploadingField(null=True, blank=True, default=None)
    terms_of_service = RichTextUploadingField(null=True, blank=True, default=None)
    misc = RichTextUploadingField(null=True, blank=True, default=None)
