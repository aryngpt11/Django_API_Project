from django.urls import path,include
from enroll.api.views import UserViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('crud',UserViewSet,basename='user'),

urlpatterns=[
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
]