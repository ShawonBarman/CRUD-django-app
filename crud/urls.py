from django.urls import path
from . import views
urlpatterns = [
    path('', views.add_show_data, name="home"),
    path('delete/<int:id>/', views.delete_info, name="deleteInfo"),
    path('update/<int:id>/', views.update_info, name="updateInfo"),
]