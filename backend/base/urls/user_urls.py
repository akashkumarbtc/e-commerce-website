from django.urls import path, include
from ..views import user_views as views

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.register_user, name="register_user"),
    path('', views.get_users, name="user"),
    path('profile/', views.get_user_profile, name="user_profile"),
    path('profile/update/', views.update_user_profile, name="update_user_profile"),
]