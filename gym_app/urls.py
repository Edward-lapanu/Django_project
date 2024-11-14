from django.urls import path
from . import views
app_name = 'gym_app'
urlpatterns = [
    path('', views.index_page, name="index"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('service-details/', views.service, name="service"),
    path('starter-page/', views.starter_page, name="starter_page"),
    path('appointment/', views.appointment, name="appointment"),
    path('appointments/', views.retrieve_appointments, name= "show"),
    path('delete/<int:id>', views.delete_appointment, name="delete_appointment"),
]
