from urllib.parse import urlparse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import Resolver404, reverse , resolve
from core import settings
from .models import Posts , Comment , ContactMessage
from .forms import PostForm, CommentForm,ContactForm
from django.core.mail import send_mail
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from core import settings
from django.utils import translation

@login_required(login_url='account:Login')
def home__page(request):
    form = PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        
        posts=form.save(commit=False)
        posts.author=request.user
        form.save(commit=True)
        messages.success(request, 'Your comment has been shared.')
        return redirect('home')
    
    posts = Posts.objects.all()
    context = {'form': form, 'posts': posts}
    
    return render(request, 'home.html', context)

@login_required(login_url='account:Login')
def about__page(request):
    return render(request,'about.html')

@login_required(login_url='account:Login')
def post_detail(request, id):
    post = get_object_or_404(Posts, id=id)
    comments = post.comments.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            messages.success(request, 'Your comment has been shared.')
            return redirect('post-detail', id=post.id)
    else:
        comment_form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'post-detail.html', context)

@login_required(login_url='account:Login')
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

           
            ContactMessage.objects.create(name=name, email=email, message=message)

            
            send_mail(
                f'Mesaj: {name}',
                message,
                email,
                ['your_email@example.com'],
            )

            
            messages.success(request, 'Your message has been sent successfully!')

           
            return redirect('Contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

@login_required(login_url='account:Login')
def user__page(request):
    
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        posts=form.save(commit=False)
        posts.author=request.user
        form.save(commit=True)
        messages.success(request, 'The article has been shared.')
        return redirect('user')
    posts=Posts.objects.filter(author=request.user)
    context = {'form': form, 'posts': posts}
    
    return render(request, 'user.html', context)

@login_required(login_url='account:Login')
def update_view(request, id):
    post = get_object_or_404(Posts, id=id)
    redirect_to = request.POST.get('redirect_to') 

    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    
    if form.is_valid():
        
        posts = form.save(commit=False)
        posts.author = request.user
        form.save()
        messages.success(request, 'The article has been updated.')

        
        if redirect_to == 'home':
            return redirect('home')
        else:
            return redirect('user')

    
    posts = Posts.objects.filter(author=request.user)
    context = {'form': form, 'posts': posts}

    return render(request, 'home.html', context)
   
    

@login_required(login_url='account:Login')
def delete__view(request,id):
    post = get_object_or_404(Posts, id=id)
    post.delete()
    messages.success(request, 'The article has been deleted.')    
    return redirect('user')     

def post_search(request):
    keyword = request.GET.get('keyword')
    searched = False
    if keyword:
        searched = True
        posts = Posts.objects.filter(
            Q(title__icontains=keyword) |
            Q(content__icontains=keyword) |
            Q(author__username__icontains=keyword)
        )
    else:
        posts = Posts.objects.all()
    
    form = PostForm(request.POST or None, request.FILES or None)
    context = {'form': form, 'posts': posts,'searched': searched,'keyword':keyword}

    return render(request, 'home.html', context)




def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response

def custom_404(request, exception):
    return render(request, '404.html', status=404)