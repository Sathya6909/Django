from django.urls import path
from .views import HelloWorldisView,CreateUserView


urlpatterns = [
    path('hello/', HelloWorldisView.as_view(), name='hello-world'),
    path('signup/', CreateUserView.as_view(), name='signup'),

]
