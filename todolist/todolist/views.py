from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

# Listar tarefas
def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'task_list.html', {'tasks': tasks})

# Adicionar tarefa
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title:
            Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'add_task.html')

# Editar tarefa
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list')
    return render(request, 'edit_task.html', {'task': task})

# Excluir tarefa
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

# Marcar/desmarcar como concluída
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')