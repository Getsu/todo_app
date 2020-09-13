from django.shortcuts import render, redirect
from .models import List # データベースと連動して表示させる用
from .forms import ListForm

def home(request):

    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            return render(request, 'home.html', {'all_items': all_items})
    
    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})


    # Listデータベースのすべてのアイテムを取得し、home.htmlに渡す
    all_items = List.objects.all
    return render(request, 'home.html', {'all_items': all_items})

def about(request):
    # context = {'first_name': 'Harry', 'last_name': 'Potter'}
    return render(request, 'about.html', context)

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    # messages.success(request, ('Item Has Been Deleted from List!'))
    return redirect('home')

def uncomplete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

def complete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')