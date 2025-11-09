from django.shortcuts import render,redirect,get_object_or_404
from api.models import Item 
from django.contrib.auth.decorators import login_required
from .forms import ConversationMessageForm
from .models import Conversation,ConversationMessage
# Create your views here.
def new_conversation(request,item_pk):
    item=get_object_or_404(Item,pk=item_pk)
    if item.created_by==request.user:
        return redirect('dashboard')
    conversations=Conversation.objects.filter(item=item).filter(members__in=[request.user.id])
    if conversations:
        pass # redirect to conversation
    if request.method=='POST':
        form=ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation=Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message=form.save(commit=False)
            conversation_message.conversation=conversation
            conversation_message.members=request.user
            conversation_message.save()
            return redirect('detail',pk=item_pk)
    else:
        form=ConversationMessageForm()
        
    return render(request,'new_conversation.html',{'form':form})

@login_required
def inbox(request):
    conversations=Conversation.objects.filter(members__in=[request.user.id])
    return render(request,'conversation_inbox.html',{'conversations':conversations})

@login_required
def detail_conversation(request,pk):
    conversation=Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
    return render(request,'detail_conversation.html',{'conversation':conversation})
    
