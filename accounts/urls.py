from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserCrudView,CustomTokenObtainPairView

router=DefaultRouter()
router.register('users',UserCrudView)

urlpatterns = [
    path('token/',CustomTokenObtainPairView.as_view(), name="create-user"),
    
]+router.urls
