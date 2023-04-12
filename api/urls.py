from django.urls import path
from .views import *


urlpatterns = [
    path('get_hash/', favicon.as_view()),
]