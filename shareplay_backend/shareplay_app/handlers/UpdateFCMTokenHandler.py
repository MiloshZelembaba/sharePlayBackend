from django.http import HttpResponse
from shareplay_app.models import User

def passOff(json_data):
    user_id = json_data['user']['id']
    refresh_token = json_data['refresh_token']

    try:
        user = User.objects.get(id=user_id)
        user.fcm_token = refresh_token
        user.save()

    except User.DoesNotExist:
        return HttpResponse("User does't exist", content_type='application/json', status=418)

    return HttpResponse({}, content_type='application/json', status=200)
