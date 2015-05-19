from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Photos, Event, load_data, timemachine, create_photos
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


def index(request):
	events = Event.objects.filter(user=1)
	print events
	#photos = Photos.objects.filter(event_id=11)

	return render(request, 'event/index.html', {"events" : events})

def new_event(request):
	return render(request, 'event/new_event.html')

def show(request, event_id):
	try:
	    event = Event.objects.get(pk=event_id)
	    photos = Photos.objects.filter(event_id=event_id)

	except Event.DoesNotExist:
	    raise Http404("Event does not exist")
	return render(request, 'event/show.html', {'photos': photos, 'event':event})

def create_event(request):
	try:
		print request
		e = Event(user = User.objects.all()[0], event_name=request.POST['event_name'], instagram_hashtag=request.POST['instagram_hashtag'], instagram_handle=request.POST['instagram_handle'],twitter_hashtag=request.POST['twitter_hashtag'], twitter_handle=request.POST['twitter_handle'], status=request.POST['active_status'],)

		print e

		e.save()

		data = load_data(e.instagram_hashtag)
		event = e

		create_photos(data, e.id)

		photos = Photos.objects.filter(event_id=e.id)

	except:
		return HttpResponse("Try Again.")
	return HttpResponseRedirect(reverse("event:show", args = (event.id,)))


def delete_event(request, event_id):
	try:
		e = Event.objects.get(pk=event_id)
		print e
		Photos.objects.filter(event_id=e.id).delete
		e.delete()

	except Event.DoesNotExist:
	    raise Http404("Event does not exist")
	return index(request)
