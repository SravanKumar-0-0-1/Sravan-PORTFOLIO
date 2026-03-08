from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.HomepageView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('resume/', views.ResumeView.as_view(), name='resume'),
    path('resume/download/<int:resume_id>/', views.resume_download, name='resume_download'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact/success/', views.ContactSuccessView.as_view(), name='contact_success'),
    path('projects/', views.ProjectListView.as_view(), name='list'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='detail'),
]
