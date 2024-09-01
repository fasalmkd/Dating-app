from django.urls import path
from.import views

urlpatterns = [
    path("",views.index,name="index"),
    path("profile.html",views.profile,name="profile"),
    path("password.html",views.password,name="password"),
]
