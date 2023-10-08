from django.urls import path
from app import views
urlpatterns = [
    path('',views.handleindex,name='handleindex'),
    path('contact',views.contact,name='contact'),
    path('signup',views.handlesignup,name='handlesignup'),
    path('home',views.home,name='home'),
    path('logout',views.handlelogout,name='handlelogout')
]
