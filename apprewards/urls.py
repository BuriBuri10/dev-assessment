"""
URL configuration for apprewards project.

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
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static
# from home.views import MainView

urlpatterns = [
    path('', views.index, name="home"),
    # path('User', views.User, name='User'),
    path('superadmin', views.superadmin, name='superadmin'),
    path('profile_page', views.profile_page, name='profile_page'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('logins', views.logins, name='login'),
    path('points', views.points, name='points'),
    path('tasks', views.tasks, name='tasks'),
    path('MainView', views.MainView.as_view(), name='main-view'),
    path('upload/', views.file_upload_view, name='upload'),
    path('log_out', views.log_out, name='logout'),
    path('notifications', views.notifications, name='notifications'),
    
    path('admin/', admin.site.urls),

    path('LinkedIn', views.LinkedIn, name='LinkedIn'),
    path('Facebook', views.Facebook, name='Facebook'),
    path('Twitter', views.Twitter, name='Twitter'),
    path('Instagram', views.Instagram, name='Instagram'),
    path('Snapchat', views.Snapchat, name='Snapchat')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

