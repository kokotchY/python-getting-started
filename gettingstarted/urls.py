from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("hello", hello.views.hello, name="hello"),
    path("bla", hello.views.bla, name="bla"),
    path("chat", hello.views.chat, name="chat"),
    path("db/", hello.views.db, name="db"),
    path("who", hello.views.who, name="who"),
    path("helloworld", hello.views.hello_world, name="hello_world"),
    path("admin/", admin.site.urls),
]
