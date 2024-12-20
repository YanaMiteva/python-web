from django.urls import path
from todo_app import views
from todo_app.views import index

urlpatterns = [
    path('', index),
]