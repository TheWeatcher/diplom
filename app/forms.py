"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee, News, Comment, Status, Tasks


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Логин'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class RegistrationUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'})) 
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
   
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
       
class EditUserForm(forms.ModelForm):
  first_name = forms.CharField(max_length=150)
  last_name = forms.CharField(max_length=150)
  email = forms.EmailField(max_length=150)
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'email']


class EditPhotoForm(forms.ModelForm):

   class Meta:
    model = Employee
    fields = ['photo']
    labels = {'photo': "Фото"}

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'description', 'content', 'image')
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"}

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': "Комментарий"}


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('worker', 'name', 'content', 'done')
        labels = {'worker': "Работник", 'name': "Название", 'content': "Содержимое", 'done': "Статус"}

#class MessageForm(forms.ModelForm):
#    message = forms.Textarea()
#    class Meta:
#        model = Message
#        fields = ['message']
#        labels = {'message': ""}