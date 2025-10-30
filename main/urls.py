# main/urls.py
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),        # placeholder
    path('courses/', views.courses, name='courses'),  # placeholder
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('contact/', views.contact, name='contact'),  # placeholder
]


