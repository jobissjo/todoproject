from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import get_user_model

User = get_user_model()

def get_user_from_token(token):

    try:
        print("i am here")
        access_token = AccessToken(token=token)
        user_id = access_token.payload.get('user_id')
        print("i am here", user_id)
        user = User.objects.get(pk=user_id)
        print(user, user_id)
        return user, user_id
    except Exception as e:
        return None, None