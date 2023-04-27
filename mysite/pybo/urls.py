from django.contrib import admin
from django.urls import path,include
import pybo.views as pv

app_name = 'pybo'
urlpatterns = [
    path('',pv.index , name = 'index'),
    path('<int:question_id>/', pv.detail,name = 'detail'),
    path('answer/create/<int:question_id>/', pv.answer_create, name='answer_create'),


]