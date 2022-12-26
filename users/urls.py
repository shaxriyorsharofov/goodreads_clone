from django.urls import path
from .views import RegisterView, LoginView, LogoutView, UserProfileView, UserUpdateView


app_name = 'users'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    # path('home/', .as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/edit', UserUpdateView.as_view(), name='profile_update')
]


