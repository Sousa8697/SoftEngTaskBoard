from django.urls import path
from . import views
urlpatterns =[
    path('sign-in',views.signIn, name="sign-In"),
    path('sign-up',views.signUp,name="sign-up"),
    path('profile',views.profile,name="profile"),
    path('tasks',views.testTask, name = "tasks")
]