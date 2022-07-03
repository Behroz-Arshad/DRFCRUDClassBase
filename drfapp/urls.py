from django.urls import path
from drfapp.views import Std, StudentListAPIView, StudentCreateAPIView, StudentDestroyAPIView,\
    StudentRetreveAPIView, \
    StudentUpdateAPIView, StudentRetrieveDestroy, StudentRetrieveUpdateDestroy,\
    StudentRetrieveUpdate, StudentListCreate

urlpatterns = [
    path('', Std.as_view()),
    path('StudentListAPIview/', StudentListAPIView.as_view()),
    path('StudentCreateAPIView/', StudentCreateAPIView.as_view()),
    path('StudentDestroyAPIView/<int:pk>/', StudentDestroyAPIView.as_view()),
    path('StudentRetreveAPIView/<int:pk>/', StudentRetreveAPIView.as_view()),
    path('StudentUpdateAPIView/<int:pk>/', StudentUpdateAPIView.as_view()),
    # combination of more class to one
    path('StudentRetrieveDestroyAPi/<int:pk>/', StudentRetrieveDestroy.as_view()),
    path('StudentRetrieveUpdateDestroyudentAPi/<int:pk>/', StudentRetrieveUpdateDestroy.as_view()),
    path('StudentRetrieveUpdateAPi/<int:pk>/', StudentRetrieveUpdate.as_view()),
    path('StudentListCreate/', StudentListCreate.as_view()),

]
