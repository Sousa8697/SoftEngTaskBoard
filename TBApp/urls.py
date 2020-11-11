from django.urls import path
from . import views
urlpatterns =[
    path('sign-in/',views.signIn, name="sign-In"),
    path('sign-up/',views.signUp,name="sign-up"),
    path('logout/',views.user_logout, name="logout"),
    path('profile/',views.profile,name="profile"),
]