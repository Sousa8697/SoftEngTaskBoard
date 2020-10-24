from django.urls import path
from . import views
urlpatterns =[
    path('accounts/sign-in',views.signIn, name="sign-In"),
    path('',views.home,name="home"),
    path('accounts/sign-up',views.signUp,name="sign-up"),
    path('accounts/profile',views.profile,name="profile"),
    
]