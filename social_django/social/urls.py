from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from .views import ProfileUpdateView

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('feed', views.feed, name='feed'),
    path('profile/', views.profile, name='profile'),
    
    path('profile/edit/', views.ProfileUpdateView.as_view(), name='profile-update'),

    path('profile/<str:username>/', views.profile, name='profile'),

    path('password/', views.PasswordsChangeView.as_view(template_name='social/change_password.html'), name='password_change'),                                                 
    path('password/done/', views.password_succes, name='password_change_done'),  
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='social/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='social/logout.html'), name='logout'),
    path('post/', views.post, name='post'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
