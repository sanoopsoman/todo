
from django.urls import path
from . import views
urlpatterns = [
    path('', views.demo, name='demo'),
    # path('detail/', views.detail, name='detail')
    path('delete/<int:task_id>/',views.delete, name='delete'),
    path('update/<int:id>/',views.update, name='update'),
    path('cbvhome/', views.tasklistview.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.taskdetailview.as_view(), name='cbvdetail'),

path('cbvdelete/<int:pk>/', views.taskdeleteview.as_view(), name='cbvdelete'),
 ]