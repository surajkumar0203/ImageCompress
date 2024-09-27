from django.urls import path
from myapp.views import home,download
urlpatterns = [
    path("",home,name="home"),
    path('download/',download,name="download")
]