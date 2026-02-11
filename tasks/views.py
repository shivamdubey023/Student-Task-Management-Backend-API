from django.http import HttpResponse
from .models import Task


def list_tasks (request):
    tasks = Task.objects.all()

    output = ""
    for task in tasks:
        output += f"{task.title} - Completed : {task.is_completed}\n"



    return HttpResponse(output)

