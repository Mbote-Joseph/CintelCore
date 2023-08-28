from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import VisitorViewSet
from core import views

urlpatterns = [
    path("user/", views.user_list, name="user_list"),
    path("user/<int:pk>/", views.user_detail, name="user_detail"),

    path("building/", views.building_list, name="building_list"),
    path("building/<int:pk>/", views.building_detail, name="building_detail"),

    path("floor/", views.floor_list, name="floor_list"),
    path("floor/<int:pk>/", views.floor_detail, name="floor_detail"),

    path("office/", views.office_list, name="office_list"),
    path("office/<int:pk>/", views.office_detail, name="office_detail"),

    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),

    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),

    path('verify-otp/', views.verify_otp, name="verify_otp"),
    path('resend-otp/', views.resend_otp, name="resend_otp"),
    path('generate-otp/', views.generate_otp, name="generate_otp"),

    # For VisitorViewSet
    path('visitors/', VisitorViewSet.as_view({'get': 'list', 'post': 'create'}), name='visitor_list'),
    path('visitors/<int:pk>/', VisitorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='visitor_detail'),
]
