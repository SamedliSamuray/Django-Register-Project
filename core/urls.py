"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404
from posts.views import *
from account.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
urlpatterns = [
    # path('',register,name='register'),
    path('',home__page,name='home'),
    path('about/',about__page,name='About'),
    path('contact/',contact_view,name='Contact'),
    path('posts/',post_search,name='post_search'),
    path('post-detail/<int:id>',post_detail,name='post-detail'),
    path('update/<int:id>',update_view,name='update'),
    path('delete/<int:id>',delete__view,name='delete'),
    path('user/',user__page,name='user'),
    path('account/',include('account.urls')),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'posts.views.custom_404'
urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path("set-language/<str:language>", set_language, name="set-language"),
]
