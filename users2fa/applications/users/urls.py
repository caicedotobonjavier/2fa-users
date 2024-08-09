from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from rest_framework.routers import DefaultRouter

from . import views

app_name = "auth"

router = DefaultRouter()

urlpatterns = [
    path("register/", views.CreateUserView.as_view(), name="register-user"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("verity-otp/", views.VerityOTPView.as_view(), name="verify-otp"),
    path("profile/", views.UserProfileView.as_view(), name="user-profile"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh-token"),
    path("token/verify/", TokenVerifyView.as_view(), name="verify-token"),
    path("", include(router.urls)),
]