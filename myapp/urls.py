from django.urls import path
from .views import Home , Login
urlpatterns = [
    path('', Home , name="home"),
    path("login/" , Login , name="login")
]
