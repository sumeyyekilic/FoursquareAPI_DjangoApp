from django.shortcuts import render
import requests
from pandas.io.json import json_normalize
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse
import urllib
from django.conf import settings

from .models import QueryModel
from .forms import QueryForm

CLIENT_ID = settings.CLIENT_ID
CLIENT_SECRET = settings.CLIENT_SECRET

def query_venue_view(request):
	global query
	query_form = QueryForm(request.GET)
	if query_form.is_valid():
		query_form.location = query_form.cleaned_data['location']
		query_form.venue = query_form.cleaned_data['venue']
		query_form.limit = query_form.cleaned_data['limit']
		parameters = {
			'client_id':CLIENT_ID,
			'client_secret':CLIENT_SECRET,
			'near': query_form.location,
			'query': query_form.venue,
			'limit': query_form.limit,
			'v': '20180111'
		}
		url_params = urllib.parse.urlencode(parameters)
		response = requests.get("https://api.foursquare.com/v2/venues/search", url_params)
		fjson = response.json()
		response2 = fjson['response']['venues']
		query_venue =[]
		for venue in response2:
			query_dict={}
			query_dict['id'] = venue.get('id')
			query_dict['ratings'] = venue.get('rating',',,')
			query_dict['name'] = venue.get('name', "---")
			query_dict['phone'] = venue['contact'].get("phone", "iletişim yok")
			query_dict['address'] = venue['location'].get('address', "iletişim yok")
			query_dict['users_count'] = venue['stats'].get('usersCount', "---")
			query_dict['now_count'] = venue['hereNow'].get('count', "---")
			query_venue.append(query_dict)

			query = QueryModel(location=query_form.location, venue=query_form.venue)
		query.save()

	else:
		query_venue = []
		query_form.location = ""
		query_form.venue = ""
		query_form.limit = ""

	return render(request, 'dfas/query_venue.html', context={'form': query_form,
															 'query_venue':query_venue,
															 'searched_location': query_form.location,
															 'searched_venue': query_form.venue,
															 'searched_limit': query_form.limit})

def query_detail_view(request, venue_id):
	detayParam = {
		'client_id': CLIENT_ID,
		'client_secret': CLIENT_SECRET,
		'v': '20180604'
	}
	detay_Url= urllib.parse.urlencode(detayParam)
	detay_request = 'https://api.foursquare.com/v2/venues/' + venue_id + '?' +detay_Url
	response = requests.get(detay_request)
	response = response.json()
	mekanlar= response["response"]["venue"]
	mekan_detay ={}
	try:
		urlPrefix = mekanlar['photos']['groups'][0]['items'][0]['prefix']
		urlSuffix = mekanlar['photos']['groups'][0]['items'][0]['suffix']
		rPhoto = urlPrefix + '110x110' + urlSuffix
	except:
		rPhoto = " "
	mekan_detay['photo'] = rPhoto
	mekan_detay['name'] = mekanlar['name']
	mekan_detay['likes']= mekanlar['likes'].get('count',',,')
	mekan_detay['phone'] = mekanlar['contact'].get("phone", "-")
	mekan_detay['address'] = mekanlar['location'].get("address", "-")
	mekan_detay['twiter'] = mekanlar['contact'].get("twitter", "-")
	mekan_detay["users_count"] = mekanlar['stats'].get("usersCount", "-")
	mekan_detay["checkin_count"] = mekanlar['stats'].get("checkinsCount", "-")

	#kullamıcıdan limit=5 yorum için parametre tanımım
	parameters = {
		'oauth_token': 'BIH2RYEL3G20JYPXJX4LNZ01EL3VTMC0QXDNOTZKE5NZRAJL',
		'v': '20180604',
		'limit': '5',

	}

	#kullanıcıya ait tip verilerini getirme
	api_url = urllib.parse.urlencode(parameters)
	api_url = "https://api.foursquare.com/v2/venues/%s/tips?" % venue_id + api_url
	response = requests.get(api_url)
	response = response.json()
	userTip = response["response"]["tips"]["items"]
	user_list = []

	for user in userTip:
		user_k = {}
		user_photo = user["user"]["photo"].get("suffix", "---")
		user_photo = "https://irs3.4sqi.net/img/user/" + "200x200" + user_photo
		user_k["user_photo"] = user_photo
		user_k["text"] = user.get("text", "---")
		user_k["firstName"] = user["user"].get("firstName", "---")
		user_k["lastName"] = user["user"].get("lastName", "")
		user_list.append(user_k)
	return render(request, 'dfas/query_detail.html', context={'mekan_detay': mekan_detay,
															  'user_list':user_list})


