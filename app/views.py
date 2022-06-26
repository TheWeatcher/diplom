"""
Definition of views.
"""
from django.views.generic.detail import DetailView
from django.urls import reverse
from django.db.models import Count, Q
from django.core.paginator import Paginator
from django.template import loader, RequestContext
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationUserForm, EditUserForm, EditPhotoForm, NewsForm, CommentForm, NewTaskForm
from django.contrib.auth.models import User
from .models import Employee, News, Comment, Status, Tasks, Message
from django.views import View
from django.contrib.auth.decorators import login_required
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )
def zaglushka(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/zaglushka.html',
        {
            'title':'Заглушка',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def registration(request):
    """Renders the registration page."""
    assert isinstance(request, HttpRequest)
    if request.method == "POST": # после отправки формы
        regform = RegistrationUserForm (request.POST)
        if regform.is_valid(): #валидация полей формы
            reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы
            reg_f.is_staff = False # запрещен вход в административный раздел
            reg_f.is_active = True # активный пользователь
            reg_f.is_superuser = False # не является суперпользователем
            reg_f.date_joined = datetime.now() # дата регистрации
            reg_f.last_login = datetime.now() # дата последней авторизации
            reg_f.save() # сохраняем изменения после добавления данных

            return redirect('home') # переадресация на главную страницу после регистрации
    else:
        regform = RegistrationUserForm() # создание объекта формы для ввода данных нового пользователя
    return render(
        request,
        'app/registration.html',
        {
            'regform': regform, # передача формы в шаблон веб-страницы
            'year':datetime.now().year,
        }
    )
def profile(request):
    employee = User.objects.get(username = request.user.username)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/profile.html',
        {
            'employee' : employee,
            'year':datetime.now().year,
        }
    )

def foreign_profile(request, id):
    try:
        employee = User.objects.get(id=id)
        assert isinstance(request, HttpRequest)
        return render(
        request,
        'app/foreign_profile.html',
        {
            'employee' : employee,
            'year':datetime.now().year,
        }
    )
    except User.DoesNotExist:
        return HttpResponseNotFound("Пользователя не существует")

def users(request):
    users_list = User.objects.all()
    
    context = {
            "title": "Список пользователей",
            "users_list": users_list,

        }
    return render(request, 'app/users.html', context)

def editUser(request):
    if request.method == "POST":
        userForm = EditUserForm(request.POST)
        if userForm.is_valid():
            uf = userForm.save(commit=False)
            user = User.objects.get(username = request.user.username)
            user.first_name = uf.first_name
            user.last_name = uf.last_name
            user.email = uf.email
            user.save()
            return redirect('profile')
    else:
        user = User.objects.get(username = request.user.username)
        userForm = EditUserForm(initial={
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        }) 
    return render(
        request,
        'app/edit-user.html',
        {
            'userForm': userForm, 
            'year':datetime.now().year,
        }
    )
def editPhoto(request):
    assert isinstance(request, HttpRequest)
    if request.method == "POST":
        photoForm = EditPhotoForm(request.POST, request.FILES)
        
        print(request.POST)
        print (request.FILES)
        if photoForm.is_valid():
            pf = photoForm.save(commit=False)
            user = User.objects.get(username = request.user.username)
            user.employee.photo = pf.photo
            user.employee.save()
            
            return redirect('profile')
    else:
        
        user = User.objects.get(username = request.user.username)
        photoForm = EditPhotoForm(initial={
        'photo': user.employee.photo,
        })
    return render(
        request,
        'app/edit-photo.html',
        {
            'photoForm': photoForm, # передача формы в шаблон веб-страницы
            'year':datetime.now().year,
        }
    )


def news (request):
    posts = News.objects.all()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/news.html',
        {
            'title': 'Новости',
            'posts': posts,
            'year':datetime.now().year,
            }
        )



def newpost(request):
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        newsform = NewsForm(request.POST, request.FILES)
        if newsform.is_valid():
            news_f = newsform.save(commit=False)
            news_f.posted = datetime.now()
            news_f.author = request.user
            news_f.save()

            return redirect('news')
    else:
        newsform = NewsForm()

    return render(
        request,
        'app/newpost.html',
        {
            'newsform': newsform,
            'title': 'Добавить отзыв',
            'year': datetime.now().year,
            }
        )

def newspost(request, parametr):
    
    post_1 = News.objects.get(id=parametr) 
    comments = Comment.objects.filter(post=parametr)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = News.objects.get(id=parametr)
            comment_f.save()
            
            return redirect('newspost', parametr=post_1.id)
    else:
        form = CommentForm()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/newspost.html',
        {
            'title':'Новости',
            'post_1': post_1, 
            'comments': comments,
            'form': form,
            'year':datetime.now().year,
        }
    )   


def newtask(request):
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        taskform = NewTaskForm(request.POST, request.FILES)
        if taskform.is_valid():
            task_f = taskform.save(commit=False)
            task_f.posted = datetime.now()
            task_f.author = request.user
            task_f.save()

            return redirect('home')
    else:
        taskform = NewTaskForm()

    return render(
        request,
        'app/newtask.html',
        {
            'taskform': taskform,
            'title': 'Добавить задание',
            'year': datetime.now().year,
            }
        )


def tasks (request):
    tasks = Tasks.objects.all()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/tasks.html',
        {
            'title': 'Задания',
            'tasks': tasks,
            'year':datetime.now().year,
            }
        )


def ConfirmTask(request, parametr):

    tasks = Tasks.objects.filter(id = parametr)
    status = Status.objects.get(text = 'Выполнено')

    for task in tasks:
        task.done = status
        task.save()

    return redirect('tasks')

def RejectTask(request, parametr):

    tasks = Tasks.objects.filter(id = parametr)
    status = Status.objects.get(text = 'Провалено')

    for task in tasks:
        task.done = status
        task.save()

    return redirect('tasks')

def ResetTask(request, parametr):

    tasks = Tasks.objects.filter(id = parametr)
    status = Status.objects.get(text = 'В процессе')

    for task in tasks:
        task.done = status
        task.save()

    return redirect('tasks')

def DeleteTask(request, parametr):
    tasks = Tasks.objects.filter(id = parametr)

    for task in tasks:
        task.delete()

    return redirect('tasks')


@login_required
def Inbox(request):
	messages = Message.get_messages(user=request.user)
	active_direct = None
	directs = None

	if messages:
		message = messages[0]
		active_direct = message['user'].username
		directs = Message.objects.filter(user=request.user, recipient=message['user'])
		directs.update(is_read=True)
		for message in messages:
			if message['user'].username == active_direct:
				message['unread'] = 0

	context = {
		'directs': directs,
		'messages': messages,
		'active_direct': active_direct,
		}

	template = loader.get_template('app/direct.html')

	return HttpResponse(template.render(context, request))

@login_required
def UserSearch(request):
	query = request.GET.get("q")
	context = {}
	
	if query:
		users = User.objects.filter(Q(username__icontains=query))

		#Pagination
		paginator = Paginator(users, 6)
		page_number = request.GET.get('page')
		users_paginator = paginator.page(page_number)

		context = {
				'users': users_paginator,
			}
	
	template = loader.get_template('app/search_user.html')
	
	return HttpResponse(template.render(context, request))

@login_required
def Directs(request, username):
	user = request.user
	messages = Message.get_messages(user=user)
	active_direct = username
	directs = Message.objects.filter(user=user, recipient__username=username)
	directs.update(is_read=True)
	for message in messages:
		if message['user'].username == username:
			message['unread'] = 0

	context = {
		'directs': directs,
		'messages': messages,
		'active_direct':active_direct,
	}

	template = loader.get_template('app/direct.html')

	return HttpResponse(template.render(context, request))


@login_required
def NewConversation(request, username):
	from_user = request.user
	body = ''
	try:
		to_user = User.objects.get(username=username)
	except Exception as e:
		return redirect('users')
	if from_user != to_user:
		Message.send_message(from_user, to_user, body)
	return redirect('inbox')

@login_required
def SendDirect(request):
	from_user = request.user
	to_user_username = request.POST.get('to_user')
	body = request.POST.get('body')
	
	if request.method == 'POST':
		to_user = User.objects.get(username=to_user_username)
		Message.send_message(from_user, to_user, body)
		return redirect('inbox')
	else:
		HttpResponseBadRequest()

def checkDirects(request):
	directs_count = 0
	if request.user.is_authenticated:
		directs_count = Message.objects.filter(user=request.user, is_read=False).count()

	return {'directs_count':directs_count}


