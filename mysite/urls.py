"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.urls import path
from htmlcss import views
import signup.views
import getstart.views
import getbook.views
import givebook.views
import status.views
from django.conf.urls.static import static



urlpatterns = [
    # path('admin/', admin.site.urls),

    path('', views.home,name='index'),
    path('admin/', admin.site.urls),
    path('contact/', signup.views.signuppage,name='contact'),
    path('signout/',signup.views.signout,name='signout'),
    path('getstarted/',getstart.views.getstarted,name='getstarted'),
    path('getbook/',getbook.views.getabook,name='getabook'),
    path('booklist/',getbook.views.booklist,name='booklist'),
    path('givebook/',givebook.views.bookupload,name='givebook'),
    path('success/',givebook.views.success,name='success'),
    path('request/',getbook.views.requestbook,name='requ'),
    path('cancel/', getbook.views.cancelbook, name='cancel'),
    path('status/',status.views.myrequests,name='status'),
    path('requests/',status.views.requests,name='requests'),
    path('chats/', status.views.chats, name='chats'),
    path('chat/', status.views.chatsend, name='chatsend'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)