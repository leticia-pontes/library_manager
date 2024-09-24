from django.urls import path
from .views import IndexView, HomeView, RegisterView, AcessoLoginView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('home/', HomeView.as_view(), name='home'),
    path('login/', AcessoLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
