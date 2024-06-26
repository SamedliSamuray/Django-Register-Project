from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Posts(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name=_('Author'))
    title = models.CharField(max_length=200,verbose_name=_('Title'))
    content = RichTextField(verbose_name=_('Content'))
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='Post Images',blank=True,null=True,verbose_name=_('İmage'))
    def __str__(self):
        return f'{self.author}|{self.title}'
    
class Comment(models.Model):
    post = models.ForeignKey(Posts, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name=_('Content'))
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content[:20]
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.name} ({self.email})'