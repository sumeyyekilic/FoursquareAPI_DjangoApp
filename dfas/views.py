from django.shortcuts import render
import requests
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
		#url'ye gönderilecek gerekli parametreler format metodu ile de atanabilir.
		queryParam = {
			'client_id':CLIENT_ID,
			'client_secret':CLIENT_SECRET,
			'near': query_form.location,
			'query': query_form.venue,
			'limit': query_form.limit,
			'v': '20180111'
		}
		url_params = urllib.parse.urlencode(queryParam)
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
			query_dict['address2'] = venue['location'].get('formattedAddress', "iletişim yok")
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
	context = {'form': query_form,
			   'query_venue': query_venue,
			   'searched_location': query_form.location,
			   'searched_venue': query_form.venue,
			   'searched_limit': query_form.limit}
	return render(request, 'dfas/query_venue.html', context)

#sorgulanan konumda ki mekanın detay bilgilerini çekme
def query_detail_view(request, venue_id):
	detayParam = {
		'client_id': CLIENT_ID,
		'client_secret': CLIENT_SECRET,
		'v': '20180604'
	}
	detay_Url= urllib.parse.urlencode(detayParam)
	detay_request = 'https://api.foursquare.com/v2/venues/' + venue_id + '?' +detay_Url
	response = requests.get(detay_request)
	fjson = response.json()
	mekanlar= fjson["response"]["venue"]
	mekan_detay ={}
	try:
		urlPrefix = mekanlar['photos']['groups'][0]['items'][0]['prefix']
		urlSuffix = mekanlar['photos']['groups'][0]['items'][0]['suffix']
		rPhoto = urlPrefix + '110x110' + urlSuffix
	except:
		rPhoto = " "

	mekan_detay['photo'] = rPhoto
	mekan_detay['name'] = mekanlar['name']
	mekan_detay['likes'] = mekanlar['likes'].get('count',',,')
	mekan_detay['phone'] = mekanlar['contact'].get("phone", "-")
	mekan_detay['ratings'] = mekanlar.get("rating")
	mekan_detay['address'] = mekanlar['location'].get("formattedAddress", "-")
	mekan_detay['twiter'] = mekanlar['contact'].get("twitter", "-")
	mekan_detay["users_count"] = mekanlar['stats'].get('usersCount', "-")
	mekan_detay["checkin_count"] = mekanlar['stats'].get("checkinsCount", "-")

#kullamıcıdan limit=5 yorum için parametre tanımım
	commentParam= {
		'oauth_token': 'BIH2RYEL3G20JYPXJX4LNZ01EL3VTMC0QXDNOTZKE5NZRAJL',
		'client_id': CLIENT_ID,
		'client_secret': CLIENT_SECRET,
		'v': '20180604',
		'limit': '5',
	}

	#kullanıcıya ait tip verilerini getirme
	api_url = urllib.parse.urlencode(commentParam)
	api_url = "https://api.foursquare.com/v2/venues/%s/tips?" % venue_id + api_url
	response = requests.get(api_url)
	fjson = response.json()
	userTip = fjson['response']['tips']['items']
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

	context = {'mekan_detay': mekan_detay,
			   'user_list': user_list}
	return render(request, 'dfas/query_detail.html', context )


#yorumlarda ki kullanıcının detay dayfası
def user_comment_view(request, user_id):
	'''userParam = {
		'oauth_token': 'BIH2RYEL3G20JYPXJX4LNZ01EL3VTMC0QXDNOTZKE5NZRAJL',
		'v': '20180604'
	}
	detay_Url = urllib.parse.urlencode(userParam)
	detay_request = "https://api.foursquare.com/v2/venues/%s/tips?" % user_id + detay_Url
	response = requests.get(detay_request)
	response = response.json()
	user = response["response"]["tips"]["items"]
	user_detay = []
	try:
		user_photo1 = user["user"]["photo"].get("suffix", "---")
		user_photo2 = "https://irs3.4sqi.net/img/user/" + "200x200" + user_photo1
		rPhoto = user_photo2
	except:
		rPhoto = ' '
	for user in user:
		user_d = {}
		user_d["user_photo"] = rPhoto
		#user_d["name"] = user['user'].get("firstName", "---")
		user_d["lastName"] = user["user"].get("lastName", "")
		user_d['gender'] = user['user'].get("gender", "--")
		user_d["text"] = user.get("text", "---")
		user_detay.append(user_d)

	context = {'user_detay': user_detay}'''
	commentParam = {
		'oauth_token': 'BIH2RYEL3G20JYPXJX4LNZ01EL3VTMC0QXDNOTZKE5NZRAJL',
		'client_id': CLIENT_ID,
		'client_secret': CLIENT_SECRET,
		'v': '20180604',
	}

	# kullanıcıya ait tip verilerini getirme
	api_url = urllib.parse.urlencode(commentParam)
	api_url = "https://api.foursquare.com/v2/venues/%s/tips?" % user_id + api_url
	response = requests.get(api_url)
	fjson = response.json()
	userTip = fjson['response']['tips']['items']
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
	context={'user_list': user_list}
	return render(request,'dfas/user_detail.html', context)