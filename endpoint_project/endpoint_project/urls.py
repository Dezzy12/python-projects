
from django.contrib import admin
from django.urls import path
from endpoint_app.views import endpoint_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', endpoint_view, name='endpoint')
]

