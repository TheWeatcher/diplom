"""
Definition of models.
"""
from django.core.files import storage
from django.db import models
from django.contrib import admin
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db.models import Max

# Create your models here.
class Status(models.Model):
  text = models.CharField(max_length = 150, unique = True, verbose_name = 'Наименование сатуса')


  def __str__(self):
    return self.text

  class Meta:
    db_table = "Statuses"
    ordering = ["id"]
    verbose_name = "Статус"
    verbose_name_plural = "Статусы заданий"
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.FileField(upload_to='employee/%Y/%m/%d', blank=True, verbose_name = "Фото")
def __str__(self):
    return str(self.user)
    class Meta:
        db_table = "Employee"
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

@receiver(post_save, sender=User)
def save_or_create_profile(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)
    else:
        try:
            instance.employee.save()
        except ObjectDoesNotExist:
            Employee.objects.create(user=instance)


class News(models.Model):
    title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Заголовок")
    description = models.TextField(verbose_name = "Краткое содержание")
    content = models.TextField(verbose_name = "Полное содержание")
    posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Опубликован")
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    image = models.FileField(default = 'temp.jpg', verbose_name = "Путь к картинке")

    def get_absolute_url(self):
        return reverse("newspost", args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        db_table = "News"
        ordering = ["-posted"]
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Comment(models.Model):
    text = models.TextField(verbose_name = "Комментарий")
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Дата")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор")
    post = models.ForeignKey(News, on_delete = models.CASCADE, verbose_name = "Новость")

    def __str__(self):
        return 'Комментарий %s к %s' % (self.author, self.post)

    class Meta:
        db_table = "Comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарий к новости"
        ordering = ["-date"]

class Tasks(models.Model):
    worker = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Работник')
    name = models.CharField(max_length = 255, verbose_name = 'Краткое содержание')
    content = models.TextField(verbose_name = 'Задача')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Создан')
    done = models.ForeignKey(Status, verbose_name = 'Статус')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
 
class Message(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', verbose_name = "Пользователь")
	sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user', verbose_name = "Отправитель")
	recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user', verbose_name = "Получатель")
	body = models.TextField(max_length=1000, blank=True, null=True, verbose_name = "Сообщение")
	date = models.DateTimeField(auto_now_add=True, verbose_name = "Дата")
	is_read = models.BooleanField(default=False, verbose_name = "Прочитано")

	def send_message(from_user, to_user, body):
		sender_message = Message(
			user=from_user,
			sender=from_user,
			recipient=to_user,
			body=body,
			is_read=True)
		sender_message.save()

		recipient_message = Message(
			user=to_user,
			sender=from_user,
			body=body,
			recipient=from_user,)
		recipient_message.save()
		return sender_message

	def get_messages(user):
		messages = Message.objects.filter(user=user).values('recipient').annotate(last=Max('date')).order_by('-last')
		users = []
		for message in messages:
			users.append({
				'user': User.objects.get(pk=message['recipient']),
				'last': message['last'],
				'unread': Message.objects.filter(user=user, recipient__pk=message['recipient'], is_read=False).count()
				})
		return users