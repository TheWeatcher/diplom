from django.contrib import admin
from .models import Employee, Status, Tasks, News, Comment, Message


class EmployeeAdmin(admin.ModelAdmin):
  list_display = ['user', 'photo']

class TasksAdmin(admin.ModelAdmin):
  list_display = ['worker', 'name', 'content', 'created', 'done']


class StatusAdmin(admin.ModelAdmin):
  list_display = ['text']





admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Tasks, TasksAdmin)
admin.site.register(News)
admin.site.register(Comment)
admin.site.register(Message)
