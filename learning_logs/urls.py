"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page for all Topics
    path('topics/', views.topics, name='topics'),
    # Page for single Topic
    path('topics/<int:topic_id>', views.topic, name='topic'),
    # Page for adding new Topic
    path('topics/new_topic/', views.new_topic, name='new_topic'),
    # Page for adding new Entry
    path('topics/<int:topic_id>/new_entry/', views.new_entry, name='new_entry'),
    # # Page for editting Entry
    path('edit_entry/<int:entry_id>', views.edit_entry,
         name='edit_entry'),
]
