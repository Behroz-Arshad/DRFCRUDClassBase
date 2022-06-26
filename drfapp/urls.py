from django.urls import path
from drfapp.views import Std
urlpatterns = [
    path('',Std.as_view())
]