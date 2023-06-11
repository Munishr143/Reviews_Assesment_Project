"""
URL configuration for Reviews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Registration/', Registration, name='Registration'),
    path('Home/', Home, name='Home'),
    path('User_Login/', User_Login, name='User_Login'),
    path('User_Logout/', User_Logout, name='User_Logout'),
    path('Change_Password/', Change_Password, name='Change_Password'),
    path('Forget_Password/', Forget_Password, name='Forget_Password'),
    path('Ask_Question/', Ask_Question, name='Ask_Question'),
    path('display_questions/', display_questions, name='display_questions'),
    path('Answer_the_Questions/', Answer_the_Questions, name='Answer_the_Questions'),
    path('display_answers/', display_answers, name='display_answers'),

]

