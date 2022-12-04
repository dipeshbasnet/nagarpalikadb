# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from django.contrib.auth.views import LogoutView

from apps.authentication.api.v1.views.token import TokenAuthLogout
from apps.authentication.views import login_view, register_user

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('remove-token/', TokenAuthLogout.as_view(), name='token_logout'),
]
