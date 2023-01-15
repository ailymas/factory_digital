from .views import RegisterView,TodoView
from django.urls import path

urlpatterns = [
    path("register/",RegisterView.as_view(),name="register_user"),
    path("add_todo/",TodoView.as_view(),name="create_todo")
]