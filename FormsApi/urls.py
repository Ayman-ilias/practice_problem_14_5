from django.urls import path
from .import views


urlpatterns = [
    path('go/',views.djangoForm,name='formapi'),
]
