from django.urls import path,re_path
from bruteforce import views

app_name = 'bruteforce'

urlpatterns =[
    path('',views.index,name='index'),
    re_path(r'^register',views.register,name='register'),
]