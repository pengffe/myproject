from django.db.models import Q  # ????????????????????????
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json

from appbackend import models
from .models import Book
from .models import Users
from .forms import UserRegisterForm


def user_register(request):
    response = {}
    print("hello: 接受request！！！！！！！！！！！！！！！！！！！！！！")
    user_register_form = UserRegisterForm(request.GET)
    if user_register_form.is_bound:
        email = user_register_form.data['user_name']
        password = user_register_form.data['password']

        # new_user = models.Users.objects.create(user_name=email, password=password, personality=1)
        # user_register?user_name=pengf190224@gmail.com&password=planet0929

        user_list = Users.objects.filter(user_name=email)
        if user_list:
            response['msg'] = 'User is existing'
            return JsonResponse(response)
        else:
            new_user = models.Users(user_name=email, password=password)
            new_user.save()
        response['error_num'] = 0
    else:
        response['error_num'] = 1
    return JsonResponse(response) #render(request, {'user_register_form': user_register_form})


# Create your views here.

@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = "pengffe: worng"  # str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def show_books(request):
    print(request)
    response = {}
    try:
        books = Book.objects.all()
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def add_user(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = "pengffe: worng"  # str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def show_users(request):
    print(request)
    response = {}
    try:
        users = Users.objects.all()
        response['list'] = json.loads(serializers.serialize("json", users))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def add_friends(request):
    response = {}
    try:
        name = request.GET.get('user_name')
        user = Users.objects.filter(user_name=name).first()
        Chloe = Users.objects.create(user_name="Chloe", personality=1)
        phil = Users.objects.create(user_name="phil", personality=1)
        Chloe.friends.add(phil)
        user.friends.add(Chloe)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def show_friends(request):
    response = {}
    try:
        name = request.GET.get('user_name')
        user = Users.objects.filter(user_name=name).first()
        friends = user.friends
        response['list'] = friends  # json.loads(serializers.serialize("json", friends))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)
