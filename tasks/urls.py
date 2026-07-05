
from django.urls import path

from tasks.views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView, EmployeeTaskListView


urlpatterns = [

    path(
        "",
        TaskListView.as_view(),
        name="task_list",
    ),

    path(
        "create/",
        TaskCreateView.as_view(),
        name="task_create",
    ),

    path(
        "update/<int:pk>/",
        TaskUpdateView.as_view(),
        name="task_update",
    ),

    path(
        "delete/<int:pk>/",
        TaskDeleteView.as_view(),
        name="task_delete",
    ),

    path(
        "detail/<int:pk>/",
        TaskDetailView.as_view(),
        name="task_detail",
    ),
    path(
        "my-tasks/",
        EmployeeTaskListView.as_view(),
        name="my_tasks"
    )
]