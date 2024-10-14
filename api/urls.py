from django.urls import path
from api import views

#  this urls are api urls


# for token authentication
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
        path('',views.home,name='homepage'),
        path('studata/',views.Students_Data.as_view()),
        path('studata/<int:pk>',views.Students_Data.as_view()),
        
        path('gettoken/',obtain_auth_token)

]
