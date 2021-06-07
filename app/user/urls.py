from django.urls import path

from . import views

app_name = 'user'

# Teremos o seguinte caminho:
# /user/create

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
]
