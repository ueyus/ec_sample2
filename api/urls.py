from django.urls import path
from api import views

urlpatterns = [
	path('news/', views.news_list, name="news_list_api"),
	path('news/<int:news_id>', views.news_detail, name="news_detail_api"),
	path('items/', views.item_list, name="item_list_api"),
	path('items/<int:item_id>', views.item_detail, name="item_detail_api"),
]