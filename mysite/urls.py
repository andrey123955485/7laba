from django.contrib import admin
from django.urls import path
from visits import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('monitoring/', views.monitoring, name='monitoring'),
]
