from django.urls import path
from apps.authentication.views.user_auth import Registration, Login, Logout

urlpatterns = [
    path("register/", Registration.as_view(), name="register_user"),
    path("login/", Login.as_view(), name="login_user"),
    path("logout/", Logout.as_view(), name="logout_user"),
]
