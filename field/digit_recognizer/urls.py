# digit_recognizer/urls.py

from django.urls import path
from .views import digit_recognizer_view

urlpatterns = [
    path('recognize/', digit_recognizer_view, name='digit_recognizer'),
]
