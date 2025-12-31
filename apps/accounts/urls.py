from django.urls import path
from .views import RegisterAPI, LoginAPI, LogoutAPI, DashboardAPI

urlpatterns = [
    path("register/", RegisterAPI.as_view()),
    path("login/", LoginAPI.as_view()),
    path("logout/", LogoutAPI.as_view()),
    path("dashboard/", DashboardAPI.as_view()),
]
