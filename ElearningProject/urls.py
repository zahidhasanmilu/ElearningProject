from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


###
from ElearningProject import user_login, views


urlpatterns = [
    path('admin/', admin.site.urls),

    #################
    path('base/', views.BASE, name='base'),
    path('', views.HOME, name='home'),
    path('single/course/', views.SINGLE_COURSE),
    path('contact/', views.CONTACT_US, name='contact'),
    path('about/', views.ABOUT_US, name='about'),

    # user_login
    path('accounts/register/', user_login.REGISTER, name='register'),
    path('doLogin/', user_login.DO_LOGIN, name='dologin'),
    path('accounts/profile/', user_login.PROFILE, name='profile'),
    path('accounts/profile/update/',
         user_login.PROFILE_UPDATE, name='profile_update'),

    path('accounts/', include('django.contrib.auth.urls')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
