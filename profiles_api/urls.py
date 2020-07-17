from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()

# Register urls for HelloViewSet, UserProfileViewSet
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')  # base_name depricated in Django 3.0.8
router.register('profile', views.UserProfileViewSet) # basename not required because we have queryset in UserProfileViewSet
router.register('feed', views.UserProfileFeedViewSet) # basename not required because we have querysViewSet

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
