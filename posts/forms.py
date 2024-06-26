from django import forms
from .models import Posts
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=['title','content','image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(widget=forms.Textarea, label='Message')