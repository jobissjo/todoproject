from django.urls import path
from .views import UserSignInView, UserSignUpView, get_user_info

# from res

urlpatterns = [
    path('signup/',UserSignUpView.as_view(), name='user_signup'),
    path('signin/', UserSignInView.as_view(), name='user_signin'),
    path('current_user/', get_user_info, name='current_user')   
]