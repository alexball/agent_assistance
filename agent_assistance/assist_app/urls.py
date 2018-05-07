from django.urls import path, re_path

from . import views

urlpatterns = [
    path('claim/<int:call_id>/', views.claim_call, name='claim_call'),
    path('', views.index, name='index'),
]
