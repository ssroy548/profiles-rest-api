from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("helloviewset",views.HelloViewSet,base_name="helloviewset")
router.register('profile',views.UserProfileViewSet)
router.register('feed',views.UserProfileFeedViewSet)

urlpatterns = [
    path('helloview/', views.HelloApiView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
