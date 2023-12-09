from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/',login_user, name='login'),
    path('register/',register_user, name='register'),
    path('change_password/', change_password, name='change_password'),
    path('logout/',logout_user, name='logout'),
    path('navbar/',navbar, name='navbar'),
    path("home/",emp_home),
    path("add-emp/",add_emp),
    path("delete-emp/<int:emp_id>",delete_emp),
    path("update-emp/<int:emp_id>",update_emp),
    path("do-update-emp/<int:emp_id>",do_update_emp),
]
