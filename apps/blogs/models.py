from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def  __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    slug = models.CharField(max_length=100, blank=False, null=False)
    thumbnail = models.ImageField(upload_to='upload/thumbnail/posts/%Y/%m/%d', blank=True, null=True)
    banner = models.ImageField(upload_to='upload/banner/posts/%Y/%m/%d', blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def  __str__(self):
        return self.title
