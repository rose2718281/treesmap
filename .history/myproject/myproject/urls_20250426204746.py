from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/trees/", views.tree_list),
    path("api/trees/<int:pk>/", views.tree_detail),
]
