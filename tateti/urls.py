from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.game),
    path('play',views.game),
    path('reset',views.reset)
]
