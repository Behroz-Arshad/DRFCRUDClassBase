from django.urls import path
from drfapp.views import Std, StudentListGenericMixinClass, StudentCreateGenericMixinClass, \
    StudentDeleteGenericMixinClass ,StudentUpdateGenericMixinClass, StudentRetereveGenericMixinClass, \
    DestroyModelMixin
urlpatterns = [
    path('',Std.as_view()),
    #generic api view and model mixin
    path('student-list-mixin/', StudentListGenericMixinClass.as_view()),
    path('student-create-mixin/', StudentCreateGenericMixinClass.as_view()),
    path('student-update-mixin/<int:pk>/', StudentUpdateGenericMixinClass.as_view()),
    path('student-delete-mixin/<int:pk>/', StudentDeleteGenericMixinClass.as_view()),
    path('student-retreve-mixin/<int:pk>/', StudentRetereveGenericMixinClass.as_view())
]