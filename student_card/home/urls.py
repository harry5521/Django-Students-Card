from django.urls import path
from home import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('marks/<std_id>/', views.marks, name='view_marks'),
]