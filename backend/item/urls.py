from django.urls import path 
from . import views 
urlpatterns=[
    path('<int:pk>',views.details,name='detail'),
    path('newitem/',views.new,name='new_item'),
    path('<int:pk>/delete',views.delete_item,name='delete_item'),
    path('<int:pk>/edit',views.edit_item,name='edit_item')
]