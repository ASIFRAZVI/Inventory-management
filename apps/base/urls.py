from django.urls import path
from apps.base.views.welcome import Welcome

urlpatterns = [path("", Welcome.as_view(), name="welcome")]
