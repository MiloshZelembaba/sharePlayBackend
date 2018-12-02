# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

import Handlers.AuthCredsHandler as AuthCredsHandler
import Handlers.AccessTokenHandler as AccessTokenHandler
import Handlers.AttemptLoginHandler as AttemptLoginHandler
import Handlers.RefreshAccessTokenHandler as RefreshAccessTokenHandler
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_auth_creds(request):
    received_json_data = get_json_from_request(request)
    return AuthCredsHandler.pass_off(received_json_data)


@csrf_exempt
def get_access_token(request):
    received_json_data = get_json_from_request(request)
    return AccessTokenHandler.pass_off(received_json_data)


@csrf_exempt
def attempt_login(request):
    received_json_data = get_json_from_request(request)
    return AttemptLoginHandler.pass_off(received_json_data)


@csrf_exempt
def get_refreshed_access_token(request):
    received_json_data = get_json_from_request(request)
    return RefreshAccessTokenHandler.pass_off(received_json_data)


def get_json_from_request(request):
    try:
        return json.loads(request.body.decode("utf-8"))
    except ValueError:
        return None