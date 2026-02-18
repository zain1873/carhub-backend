from django.urls import path
from .views import LoginView, RegisterView,ForgetPasswordView, ResetPasswordView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login-view"),
    path("register/", RegisterView.as_view(), name="register-view"),
    path("forget-password/", ForgetPasswordView.as_view(), name="forget-view"),
    path("reset-password/", ResetPasswordView.as_view(), name="reset-view")
]
