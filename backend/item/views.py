from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ItemForm, EditForm
from api.models import Item

def details(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'detail.html', {'item': item})


@login_required
def new(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('detail', pk=item.id)
    else:
        form = ItemForm()

    return render(request, 'form.html', {'form': form, 'title': 'New Item'})


@login_required
def edit_item(request, pk):
    item = get_object_or_404(Item, id=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('detail', pk=item.id)
    else:
        form = EditForm(instance=item)

    return render(request, 'form.html', {'form': form, 'title': 'Edit Item', 'item': item})


@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, id=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard')
