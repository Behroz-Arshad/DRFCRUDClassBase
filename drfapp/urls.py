from django.urls import path
from drfapp.views import Std, Studentapi

urlpatterns = [
    path('', Std.as_view()),
    path('student/<int:pk>/', Studentapi.as_view())
]