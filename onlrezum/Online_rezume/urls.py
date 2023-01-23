from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

from Online_rezume import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.register),
    path('sign_in/', user_views.sign_in),
    path('pers_area/', user_views.pers_area),
    path('privacy', user_views.privacy),
]