from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import View

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('login/', views.login_user, name='login'),
    path('testing/', views.testing, name='testing'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup_user, name='signup'),
    path('about/', views.about, name='about'),
    path('user_info/', views.user_info, name='user_info'),
]

handler404 = 'app.views.custom_404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)