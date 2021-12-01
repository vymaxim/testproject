
from django.contrib import admin
from django.urls import path

from mainapp.views import UserAddView, UserListView, UserEditView, UserDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', UserAddView.as_view(), name='add_user'),
    path('edit/<int:pk>', UserEditView.as_view(), name='edit_user'),
    path('delete/<int:pk>', UserDeleteView.as_view(), name='delete_user'),
    path('', UserListView.as_view(), name='users_list'),
]
