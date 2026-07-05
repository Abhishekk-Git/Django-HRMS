from django.urls import path
from .views import DesignationListView, DesignationCreateView, DesignationUpdateView, DesignationDeleteView

urlpatterns = [
    path("", DesignationListView.as_view(), name="designation_list"),
    path("create/", DesignationCreateView.as_view(), name="designation_create"),
    path('<int:pk>/update/', DesignationUpdateView.as_view(), name='designation_update'),
    path('<int:pk>/delete/', DesignationDeleteView.as_view(), name='designation_delete'),
]
