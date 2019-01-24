from django.urls import path
from api import views

urlpatterns = [
	path('news/', views.news_list, name="news_list_api"),
	path('news/<int:news_id>', views.news_detail, name="news_detail_api"),
]