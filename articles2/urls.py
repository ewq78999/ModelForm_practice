from django.urls import path
from . import views

app_name = 'articles2'

urlpatterns = [
    # basic
    path('', views.index, name='index'),
    # path('<int:id>/', views)
    path('<int:id>/', views.detail, name='detail'),

    # create
    path('create/', views.create, name='create'),

    # delete
    path('<int:id>/delete/', views.delete, name='delete'),

    # update
    path('<int:id>/update/', views.update, name='update'),


]