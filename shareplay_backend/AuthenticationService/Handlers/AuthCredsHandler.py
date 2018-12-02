import json
from django.http import HttpResponse
import AuthInfoStore as AuthInfoStore

__REDIRECT_URI = AuthInfoStore.REDIRECT_URI
__CLIENT_ID = AuthInfoStore.CLIENT_ID


def pass_off(request_data):
    result = {}
    result['client_id'] = __CLIENT_ID
    result['redirect_uri'] = __REDIRECT_URI

    return HttpResponse(json.dumps(result, default=str), content_type='application/json')
