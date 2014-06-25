# ~*~ coding: utf-8 ~*~
from django.db import models

from django.contrib import admin

from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from captcha.fields import CaptchaField

class Order(models.Model):
	SOURCELANG_CHOICES = (
        (u'Английский', u'Английский'),
        (u'Немецкий', u'Немецкий'),
        (u'Русский', u'Русский'),
    )
	MANAGE_CHOICES = (
        (u'Новый', u'Новый'),
        (u'В обработке', u'В обработке'),
        (u'Завершен', u'Завершен'),
    )

	name = models.CharField(verbose_name=_(u'Name'),max_length=240)
	contact = models.CharField(verbose_name=_(u"Как с вами связаться(телефон, email или Skype)"),max_length=240)
	sourcelang = models.CharField(verbose_name=_(u"С какого языка нужно перевести?"),max_length=100, choices=SOURCELANG_CHOICES, blank='true')
	resultlang = models.CharField(verbose_name=_(u"На какой язык нужно перевести?"),max_length=100, choices=SOURCELANG_CHOICES, blank='true')
	doc_file = models.FileField(verbose_name=_(u"Загрузите ваш документ"), upload_to='orderfile', blank='true')
	comments = models.TextField(verbose_name=_(u"Ваши комментарии"), blank='true')
	status = models.CharField(verbose_name=_(u"Статус"),max_length=100, choices=MANAGE_CHOICES, blank='true')
	def __unicode__(self):
		return self.name;

class OrderForm(ModelForm):
	captcha = CaptchaField()
	class Meta:
		model = Order
		exclude = ['status']
		

class OrderAdmin(admin.ModelAdmin):
	fields = ['name', 'status']

admin.site.register(Order)