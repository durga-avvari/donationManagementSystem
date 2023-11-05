"""
URL configuration for donationManagementSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from operator import index

from django.contrib import admin
from django.urls import path
from donation.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('all_logins',all_logins,name='all_logins'),
    path('donor_login',donor_login,name='donor_login'),
    path('volunteer_login',volunteer_login,name='volunteer_login'),
    path('admin_login',admin_login,name='admin_login'),
    path('donor_reg',donor_reg,name='donor_reg'),
    path('donor_home',donor_home,name='donor_home'),
    path('donor_home',donor_home,name='donor_home'),
    path('donate_now',donate_now,name='donate_now'),
    path('donation_history',donation_history,name='donation_history'),
    path('admin_home', admin_home, name='admin_home'),
    path('pending_donation', pending_donation, name='pending_donation'),
    path('view_donationdetail/<int:pid>', view_donationdetail, name='view_donationdetail'),
    path('logout/',Logout,name='logout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

