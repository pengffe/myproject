# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_name


class Users(models.Model):
    # image = models.ImageField(upload_to='user/', max_length=200, verbose_name='user profile', null=True, blank=True)
    user_name = models.CharField(max_length=65, verbose_name="Username", null=True)
    password = models.CharField(max_length=15, verbose_name="password", null=True)

    first_name = models.CharField(max_length=64, verbose_name="First Name", null=True, blank=True)
    last_name = models.CharField(max_length=64, verbose_name="Last Name", null=True, blank=True)
    date_of_birth = models.DateField(verbose_name="Birthday", null=True, blank=True)
    gender = models.CharField(choices=(('Girl', 'Women'), ('Boy', 'Man')), max_length=10, verbose_name='Gender',
                              default='Boy')
    address = models.CharField(max_length=200, verbose_name="Address", null=True, blank=True)
    phone = models.CharField(max_length=11, verbose_name="Phone Number", null=True, blank=True)
    # 以后改成choice
    school = models.CharField(max_length=64, verbose_name="School", null=True, blank=True)
    major = models.CharField(max_length=64, verbose_name="Major", null=True, blank=True)
    #
    enrol_time = models.DateField(verbose_name="Enroll Time", null=True, blank=True)
    personality = models.IntegerField(choices=((1, 'party'), (2, 'sports'), (3, 'game'), (4, 'None')), default=4)
    # add_time = models.DateTimeField(default = datetime.now, verbose_name="添加时间")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    # friends:
    friends = models.ManyToManyField("self", blank=True)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profile'

    def __str__(self):
        return self.user_name


# class PostList(models.Model):
#     content = models.CharField(max_length=2000, verbose_name='Post')
#     # image =
#     user_id = models.ForeignKey(Users)


class EmailVerifyCode(models.Model):
    code = models.CharField(max_length=20, verbose_name="Email verify code")
    email = models.EmailField(max_length=200, verbose_name="Email address for verifying")
    send_type = models.IntegerField(choices=((1, 'register'), (2, "forget"), (3, "change")),
                                    verbose_name="Type of code")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = 'Information of Email verifying'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code


# class FriendsList(models.Model):
#     friend = models.ForeignKey(Users, on_delete=Users, verbose_name="friends")
#
#     class Meta:
#         verbose_name = 'Friends list'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.friend
