from django.urls import path,include
from .views import add ,list
urlpatterns = [
    path('add',view=add,name='add'),
    path('list',view=list,name='list'),
]
