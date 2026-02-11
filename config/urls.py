from django.contrib import admin
from django.urls import path
from tasks.views import list_tasks


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/',list_tasks),
]
