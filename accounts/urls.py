from django.urls import path
from .views import view_profile
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('profile/', view_profile),
    #path('profile/<username>/', view_profile, name='view_profile_with_username')

]