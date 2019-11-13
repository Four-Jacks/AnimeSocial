from django.urls import path
from .views import login_view
from .views import view_profile

app_name = 'accounts'

urlpatterns = [
    path('accounts/', login_view),
    path('profile/', view_profile),
    #path('profile/<username>/', view_profile, name='view_profile_with_username')

]