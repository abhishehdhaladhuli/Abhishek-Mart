from django.urls import path
from . import views 
urlpatterns=[
    path('new/<int:item_pk>/',views.new_conversation,name='conversation_add'),
    path('',views.inbox,name='inbox'),
    path('<int:pk>/',views.detail_conversation,name='detail_conversation')                                                                    
]