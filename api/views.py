from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from core.models import (
	News,
)

def news_list(request):
	news_list_json = []
	for news in News.objects.all():
		news_list_json.append(news.to_dict())
	return JsonResponse(news_list_json, safe=False)

def news_detail(request, news_id):
	news = get_object_or_404(News, pk=news_id)
	return JsonResponse(news.to_dict(), safe=False)