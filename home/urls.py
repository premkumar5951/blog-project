from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contacts/',views.contacts,name="contacts"),
    path('search/',views.search,name="search"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.loginform,name="login"),
    path('logout/',views.logmeout,name="logout"),



]