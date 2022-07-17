from django.urls import path, include
from drfapp.views import Std, StudentModelViewset, StudentModelViewsetReadonly
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('studentModelViewset', StudentModelViewset, basename="stident")
#ReadOnly ModelViewset
router.register('studentModelViewsetReadOnly', StudentModelViewsetReadonly, basename="stident")
urlpatterns = [
    path('',Std.as_view()),
    path('', include(router.urls))
]