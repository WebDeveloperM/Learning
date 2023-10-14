from django.urls import path
from users.views.sign_in import SignInView
from users.views.verification import VerificationView

urlpatterns = [
    path('sign_in/', SignInView.as_view()),
    path('verification/', VerificationView.as_view()),
]
