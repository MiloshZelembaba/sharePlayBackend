from django.http import HttpResponse

from models import User
from handlers import LoginHandler
from handlers import CreatePartyHandler
from handlers import JoinPartyHandler
from handlers import AddSongToPartyHandler
from handlers import GetPartyDetailsHandler
from handlers import IncrementSongVoteCountHandler
from handlers import UpdateNetworkInfo
from handlers import LeavePartyHandler
from handlers import RemoveSongFromPartyHandler
from handlers import UpdateFCMTokenHandler
from handlers import RefreshSpotifyAccessTokenHandler
import json

def login(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body.decode("utf-8"))
        return LoginHandler.passOff(received_json_data)
    else:
        return HttpResponse("poop")

def joinParty(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body.decode("utf-8"))
        return JoinPartyHandler.passOff(received_json_data)
    else:
        return HttpResponse("poop")

def leaveParty(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body.decode("utf-8"))
        return LeavePartyHandler.passOff(received_json_data)
    else:
        return HttpResponse("poop")

def createParty(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body.decode("utf-8"))
        return CreatePartyHandler.passOff(received_json_data)
    else:
        return HttpResponse("poop")

def addSongToParty(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body.decode("utf-8"))
        return AddSongToPartyHandler.passOff(received_json_data)
    else:
        return HttpResponse("poop")

def removeSongFromParty(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body.decode("utf-8"))
        return RemoveSongFromPartyHandler.passOff(received_json_data)
    else:
        return HttpResponse("poop")

def getPartyDetails(request):
    if request.method == "POST": ## should be a GET but whatever
        received_json_data = json.loads(request.body.decode("utf-8"))
        return GetPartyDetailsHandler.passOff(received_json_data)
    else:
        return HttpResponse("poop")


def incrementSongVoteCount(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body.decode("utf-8"))
        return IncrementSongVoteCountHandler.passOff(received_json_data)
    else:
        return HttpResponse("poop")

def updateNetworkInfo(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body.decode("utf-8"))
        return UpdateNetworkInfo.passOff(received_json_data)
    else:
        return HttpResponse("poop")

def updateFCMRefreshToken(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body.decode("utf-8"))
        return UpdateFCMTokenHandler.passOff(received_json_data)
    else:
        return HttpResponse("poop")

def refreshSpotifyAccessToken(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body.decode("utf-8"))
        return RefreshSpotifyAccessTokenHandler.passOff(received_json_data)
    else:
        return HttpResponse("poop")



### TESTING ENDPOINTS

def getEmailAddress(request):
    milosh = User.objects.get(first_name="Milosh")
    return HttpResponse(milosh.email)

def success(request):
    return HttpResponse("success")

def test(request):
    import socket
    socket.gethostbyname(socket.gethostname())
    return HttpResponse(socket.gethostbyname(socket.gethostname()))
