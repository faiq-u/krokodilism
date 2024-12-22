from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('menu/',views.menu,name='menu'),
    path('hb/',views.hb,name='hb'),
    path('sp/',views.sp,name='sp'),
    path('s/',views.s,name='s'),
    path('login/',views.login,name='login'),
]
