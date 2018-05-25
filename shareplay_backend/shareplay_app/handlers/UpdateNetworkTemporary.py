import json
from shareplay_app.models import User
from ipware import get_client_ip


'''
So this is a very temporary method and implementation just to make debugging easier
It basically allows me to not have to specify the client IP address in the client that it sends to the
server. 
'''

def updateNetworkInfo(request):
    received_json_data = json.loads(request.body.decode("utf-8"))
    remote_address = request.META.get('REMOTE_ADDR')  # this shouldn't be relied on, bad practice
    email = received_json_data['user']['email']

    ip, is_routable = get_client_ip(request)
    if ip is None:
        pass
        print("None")
        # Unable to get the client's IP address
    else:
        # We got the client's IP address
        if is_routable:
            print("public")
            # The client's IP address is publicly routable on the Internet
        else:
            print("private")
            # The client's IP address is private

    try:
        user = User.objects.get(email=email)
        user.address = ip
        user.save()
    except User.DoesNotExist:
        print("couldn't do network update for some reason")
