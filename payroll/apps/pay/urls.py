from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # /pay/1
    path('<int:file_id>/', views.detail, name='detail'),
    # /pay/1/results
    path('<int:file_id>/results/', views.results, name='results'),
    path('<int:employee_id>/employee/', views.employee, name='employee'),
]
