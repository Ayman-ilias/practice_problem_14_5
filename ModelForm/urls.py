from django.urls import path
from .import views


urlpatterns = [
    path('go/',views.modelform,name='modelform'),
]
