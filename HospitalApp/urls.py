
from django.contrib import admin
from django.urls import path
from HospitalApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name ='index'),
    path('innerpage/',views.inner,name = 'inner'),

]
