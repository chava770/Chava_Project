from django.urls import path
from . import views

app_name = 'worker'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:EMPLOYEE_ID>/', views.detail, name='detail')
]