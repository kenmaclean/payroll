from django.urls import path

from . import views


urlpatterns = [
    # /pay/1 returns a report for speficied file id
    path('<int:file_id>/', views.detail, name='detail'),
    # /pay/ returns report for all files id's
    path('', views.all_records, name='all'),
]
