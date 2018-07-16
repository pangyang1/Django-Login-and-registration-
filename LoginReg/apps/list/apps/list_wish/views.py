from django.shortcuts import render
from django.shortcuts import render, HttpResponse, 
from django.core.urlresolvers import reverse
from django.contrib import messages
from.models import User, Item

def index(request):
    checkID(request)
    user = User.objects.get(id=request.session.get('id'))
    items = Item.objects.all()
    context={
        'items': items,
        'users': users,
    }
    return render(request, 'list/index.html', contex)

def createItem(request):
    checkID(request)
    status = Item.objects.makeItem(request.POST)
    if not status['valid']:
        for error in status['errors']:
            messages.error(request.error)
            return redirect('list:makeItem')
        else:
            messages.success(request, 'Item has been created')

        return redirect(reverse('list:index'))



# Create your views here.
