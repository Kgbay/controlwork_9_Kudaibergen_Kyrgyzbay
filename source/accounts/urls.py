from django.urls import path

from .views import RegisterView, LoginView, logout_view, ProfileView, \
    UserPasswordChangeView, UserChangeView

urlpatterns = [
    path('login', LoginView.as_view(), name='login_employer'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:pk>', ProfileView.as_view(), name='detail'),
    path('profile/<int:pk>/change/', UserChangeView.as_view(), name='change'),
    path('<int:pk>/password_change', UserPasswordChangeView.as_view(), name='password_change'),
]