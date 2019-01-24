from django.db import models

class Item(models.model):
	name = models.CharField("商品名", max_length=200)
	description = models.TextField("説明", max_length=200)
	price = models.PositiveIntegerField("価格")

	class Meta:
    db_table = "item"


class News(models.model):
	day = models.DateField("日")
	title = models.CharField("タイトル", max_length=128)
	body = models.TextField("本文", max_length=1000)

	def to_dict(self):
		return {
			"id": self.id,
			"day": self.day.strftime("%Y-%m-%d"),
			"title": self.title,
			"body": self.body
		}

	class Meta:
		db_table: "news"
		ordering: ("-day")

'''
class Customer(models.model):
	name = models.CharField("名前", max_length=200)
	email = models.EmailField("メール")
	age = models.PositiveIntegerField("年齢")

class Customer_log(models.model):
	amount =  models.PositiveIntegerField("容量")
	note = models.CharField("内容", max_length=200)
	customer_id = models.PositiveIntegerField("ID")

class Emtry(models.model):
	day = models.DateField("日")
	title = models.CharField("タイトル", max_length=64)
	content = models.CharField("本文", max_length=1000)

class Emtry_tags(models.model):
	entry_id = models.PositiveIntegerField()
	tag_id = models.PositiveIntegerField()

'''
