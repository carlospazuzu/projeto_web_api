from django.urls import path, include
from todomanager import views 

urlpatterns = [
        path('projectusers/', views.ProjectUserList.as_view(), name=views.ProjectUserList.name),
        path('projectusers/<int:pk>', views.ProjectUserDetail.as_view(), name=views.ProjectUserDetail.name),
        path('labels/', views.LabelList.as_view(), name=views.LabelList.name),
        path('labels/<int:pk>/', views.LabelDetail.as_view(), name=views.LabelDetail.name),
        path('projects/', views.ProjectList.as_view(), name=views.ProjectList.name),
        path('projects/<int:pk>', views.ProjectDetail.as_view(), name=views.ProjectDetail.name),
        path('activities/', views.ActivityList.as_view(), name=views.ActivityList.name),
        path('activities/<int:pk>', views.ActivityDetail.as_view(), name=views.ActivityDetail.name),
        path('users/', views.UserList.as_view(), name=views.UserList.name),
        path('users/<int:pk>/', views.UserDetail.as_view(), name=views.UserDetail.name),
        path('timeline/', views.TimelineList.as_view())

]
