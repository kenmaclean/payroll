from django.urls import path

from . import views


urlpatterns = [
    # /pay/1 returns a report for speficied file id
    path('<int:file_id>/', views.detail, name='detail'),
    # /pay/ returns report for all files id's
    path('', views.all, name='all'),
    # /pay/1/results
    path('<int:file_id>/results/', views.results, name='results'),
    #path('<int:employee_id>/employee/', views.employee, name='employee'),
]
