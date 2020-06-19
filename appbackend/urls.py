from django.conf.urls import url, include
from . import views

urlpatterns = [url(r'add_book$', views.add_book, ), url(r'show_books$', views.show_books, ),
               url(r'show_users$', views.show_users),
               url(r'show_friends$', views.show_friends),
               url(r'add_friends$', views.add_friends),
               url(r'user_register$', views.user_register)
               ]

# Create your tests here.
