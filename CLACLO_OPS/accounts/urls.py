# university_service/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.university_list, name='university_list'),
    path('detail/<int:id>/', views.university_detail, name='university_detail'),
    path('activate/<int:id>/', views.activate_university, name='activate_university'),
    path('deactivate/<int:id>/', views.deactivate_university, name='deactivate_university'),
]
