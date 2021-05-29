from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name = "index"),
    path("soumyadeep", views.soumyadeep, name = "soumyadeep"),
    path("<str:name">, views.greet, name = "greet")
]