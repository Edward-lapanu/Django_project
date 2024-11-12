from django.urls import path
from . import views
app_name = 'gym_app'
urlpatterns = [
    path('', views.index_page, name="index"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('service-details/', views.service, name="service"),
    path('starter-page/', views.starter_page, name="starter_page"),
]
