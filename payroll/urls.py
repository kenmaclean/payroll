"""payroll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
#from payroll.pay import urls
from payroll.apps.contacts.views import contact, contact_upload
from payroll.apps.pay.views import pay_upload

urlpatterns = [
    path('pay/', include('payroll.apps.pay.urls')),
    path('contacts/', include('payroll.apps.contacts.urls')),
    path('contact', contact, name="contact"),
    path('admin/', admin.site.urls),
    path('upload-csv/', contact_upload, name="contact_upload"),
    path('upload-pay-csv/', pay_upload, name="pay_upload"),
]
