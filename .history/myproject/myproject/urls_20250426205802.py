from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/register/", views.register, name="register"),
    path("api/login/", views.login_view, name="login"),
    path("api/trees/", views.tree_list),
    path("api/trees/<int:pk>/", views.tree_detail),
]
