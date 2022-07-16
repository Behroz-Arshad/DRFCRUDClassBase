from django.urls import path, include
from drfapp.views import Std, StudentViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("studentviewset",StudentViewset, basename="student")
urlpatterns = [
    path('',Std.as_view()),
    path('', include(router.urls))

]