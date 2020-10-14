from django.urls import path
from .views import RandomView, IndexView


urlpatterns = [
    path('', IndexView.as_view()),
    path('random/', RandomView.as_view()),
]