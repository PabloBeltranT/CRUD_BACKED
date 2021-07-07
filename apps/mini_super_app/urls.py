from django.urls import path 

from .views import list_users, edit_user, add_user, delete_user, sort_alphabetically, sort_numerically

urlpatterns = [
    path('app/', list_users, name='list_users'),
    path('add-user/', add_user, name='add_user'),
    path('edit-user/<int:pk>', edit_user, name='edit_user'),
    path('delete-user/<int:pk>', delete_user, name='delete_user'),
    path('sort-surname/', sort_alphabetically),
    path('sort-numerically/', sort_numerically),
]
