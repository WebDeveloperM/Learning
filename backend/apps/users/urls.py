from django.urls import path
from .views import *

urlpatterns = [
    path('sign_in/', SignInView.as_view()),
    path('verification/', VerificationView.as_view()),
]
