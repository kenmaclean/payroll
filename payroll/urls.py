from django.contrib import admin
from django.urls import include, path
from payroll.apps.pay.views import pay_upload

urlpatterns = [
    path('pay/', include('payroll.apps.pay.urls')),
    path('admin/', admin.site.urls),
    path('uploadfile/', pay_upload, name="uploadfile"),
]
