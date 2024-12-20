from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_csv, name='home'),  # This maps the root URL to the upload_csv view
    path('upload/', views.upload_csv, name='upload_csv'),  # Your existing URL for uploading CSV
    path('update_graph/', views.update_graph, name='update_graph'),
]
