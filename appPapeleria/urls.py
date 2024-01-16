
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from papeleria import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),

    path('home/', views.ViewRegistroNoAut.as_view()),
    path('home/<int:pk>/', views.ViewRegistroNoAut.as_view()),
    path('registro/', views.ViewRegistro.as_view()),
    path('registro/<int:pk>/', views.ViewRegistro.as_view()),
    path('ventas/',views.ViewVentas.as_view()),
    path('ventas/<int:pk>/',views.ViewVentas.as_view())
]
"""path('admin/', admin.site.urls),"""