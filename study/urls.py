
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AssignmentViewSet,
    TestViewSet,
    MaterialViewSet,
)

router = DefaultRouter()

router.register(
    'assignments',
    AssignmentViewSet,
    basename='assignment'
)

router.register(
    'tests',
    TestViewSet,
    basename='test'
)

router.register(
    'materials',
    MaterialViewSet,
    basename='material'
)

urlpatterns = [
    path('', include(router.urls)),
]
