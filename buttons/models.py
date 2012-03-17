# -*-coding: utf-8

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Button(models.Model):
    name = models.CharField(max_length=256);
    password = models.CharField(max_length=256);
    label = models.CharField(max_length=64);
    public_time = models.DateTimeField(auto_now_add=True);
    
    def __unicode__(self):
        return (self.name);


class Like(models.Model):
    button = models.ForeignKey(Button);
    time = models.DateTimeField(auto_now_add=True);
    used_flag = models.BooleanField();
    
    def post_form(self):
        result = u'''
        <form action="%s" method="POST">
            <input type="submit" value="%s"/>
        </form>
        ''' % ("/like_post/" + str(self.button.id)  + "/", self.button.label);
        
        return (result);

from django.contrib import admin

admin.site.register(Button);
admin.site.register(Like);
