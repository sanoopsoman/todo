from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from .forms import todoform
from .models import task
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView,DeleteView


class tasklistview(ListView):
    model = task
    template_name = 'demo.html'
    context_object_name = 'task1'


class taskdetailview(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'task'


class taskupdateview(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs= {'pk': self.object.id})
class taskdeleteview(DeleteView):
    model=task
    template_name='delete.html'
    success_url=reverse_lazy('cbvhome')


def demo(request):
    task1 = task.objects.all()
    if request.method == "POST":
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        save = task(name=name, priority=priority, date=date)
        save.save()
    return render(request, 'demo.html', {'tasks': task1})


# def detail(request):
#
#     return render(request, 'delete.html', )
def delete(request, task_id):
    task2 = task.objects.get(id=task_id)
    if request.method == "POST":
        task2.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task3 = task.objects.get(id=id)
    G = todoform(request.POST or None, instance=task3)
    if G.is_valid():
        G.save()
        return redirect('/')
    return render(request, 'update.html', {'G': G, 'task3': task3})
