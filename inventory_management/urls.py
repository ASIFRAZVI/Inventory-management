from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # base
    path("", include("apps.base.urls")),
    # auth
    path("api/auth/", include("apps.authentication.urls")),
    # inventory_mgmt app
    path("api/mgmt/", include("apps.inventory_mgmt.urls")),
    # swagger ui urls
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
