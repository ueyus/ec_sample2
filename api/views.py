from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from core.models import (
	News,
	Item,
)
from datetime import datetime
import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

@require_http_methods(["GET", "POST"])
@csrf_exempt
def news_list(request):
	if request.method == 'GET':
		news_list = [news.to_dict for news in News.objects.all()]
		return JsonResponse(news_list, safe=False)
	else:
		params = json.loads(request.body)
		news = News.objects.create(day=datetime.strptime(params["day"],"%Y-%m-%d"),
															 title=params["title"],
															 body=params["body"])
		return JsonResponse({"id": news.id})



		news_list_json.append(news.to_dict())
	return 

@require_http_methods(["GET", "PUT", "DELETE"])
@csrf_exempt
def news_detail(request, news_id):
	if request.method == "GET":
		news = get_object_or_404(News, pk=news_id)
		return JsonResponse(news.to_dict())
	elif request.method == "PUT":
		params = json.loads(request.body)
		news = News.objects.filter(id=news_id).update(
															 day=datetime.strptime(params["day"],"%Y-%m-%d"),
															 title=params["title"],
															 body=params["body"])
	else:
		News.objects.filter(id=news_id).delete()

		return JsonResponse({})

@csrf_exempt
@require_http_methods(["GET", "POST"])
def item_list(request):
	if request.method == request.GET:
		items = [item.to_dict() for item in Item.objects.order_by("id").all()]
		return JsonResponse(items, safe=False)
	else:
		params = json.loads(request.body)
		item = Item.objects.create(name=params["name"],
															 price=params["price"],
															 description=params["description"])
		return JsonResponse({"id": item.id})


@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def item_detail(request, item_id):
	if request.method == "GET":
		item = get_object_or_404(Item, pk=item_id)
		return JsonResponse(item.to_dict())
	elif request.method == "PUT":
		item = Item.objects.filter(id=item_id).update(name=params["name"],
																					 price=params["price"],
																					 description=params["description"])
		return JsonResponse({})
	else:
		item = Item.objects.filter(id=item_id).delete()
		return JsonResponse({})

