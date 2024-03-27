from django.urls import path
from . import views
from .views import contact_view

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('contact/', contact_view, name='contact_form'),
    path('confirmation', views.confirmation, name='confirmation'),
]