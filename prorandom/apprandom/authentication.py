# myapp/authentication.py

from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed

class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # Check if the request is for the signup endpoint
        if request.path == '/api/signup/':
            return None  # Allow unauthenticated access for signup
        else:
            raise AuthenticationFailed('Authentication required')
