from django.urls import path
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'accounts'
urlpatterns = [
	path('register/', views.UserRegister.as_view()),
	path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


router = routers.SimpleRouter()
router.register('user', views.UserViewSet)
urlpatterns += router.urls

# "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMTMyNDI0NSwiaWF0IjoxNzMxMjM3ODQ1LCJqdGkiOiI5ODZhNjBmMjI5OTI0Mjg4YTIxY2RlMjQwNWU2YTc2NiIsInVzZXJfaWQiOjEyfQ.bVkyiA1Q32gCa4Cdi_1yXbOwQErWiMIVygMym4J4zVI",
# "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxMjM4MTQ1LCJpYXQiOjE3MzEyMzc4NDUsImp0aSI6ImEwY2U4Njg3MDNhMTQ3NmU5NjZlYTk3M2FkOWFjNDZlIiwidXNlcl9pZCI6MTJ9.CzjjgiwwXxFVEqvsZFtfyPOlRyZ2Wjb4xmqRcBNzp4E"