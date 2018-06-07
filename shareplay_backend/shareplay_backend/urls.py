"""shareplay_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from shareplay_app import views as shareplay_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', shareplay_views.login, name='login'),
    url(r'^joinParty/', shareplay_views.joinParty, name='joinParty'),
    url(r'^leaveParty/', shareplay_views.leaveParty, name='leaveParty'),
    url(r'^createParty/', shareplay_views.createParty, name='createParty'),
    url(r'^addSongToParty/', shareplay_views.addSongToParty, name='addSongToParty'),
    url(r'^getPartyDetails/', shareplay_views.getPartyDetails, name='getPartyDetails'),
    url(r'^incrementSongVoteCount/', shareplay_views.incrementSongVoteCount, name='incrementSongVoteCount'),
    url(r'^removeSongFromParty/', shareplay_views.removeSongFromParty, name='removeSongFromParty'),
    url(r'^updateNetworkInfo/', shareplay_views.updateNetworkInfo, name='updateNetworkInfo'),
    url(r'^updateFCMRefreshToken/', shareplay_views.updateFCMRefreshToken, name='updateFCMRefreshToken'),
    url(r'^test/', shareplay_views.test, name='test'),
    url(r'^success/', shareplay_views.success, name='success'),
]
