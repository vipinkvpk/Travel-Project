from . import views
from django.urls import path,include

urlpatterns = [

    path('',views.demo,name='demo'),
    # path('calculation/', views.calculation, name='calculation')
    # path('about/',views.about,name='about'),
    # path('contact/',views.contact, name='contact')

    # path('subtract/', views.subtraction, name='subtraction'),
    # path('multiply/', views.multiplication, name='multiplication'),
    # path('divison/', views.divison, name='divison')
]