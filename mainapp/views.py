from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from mainapp.forms import UserForm
from mainapp.models import User


class UserAddView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'mainapp/add_update_user.html'
    success_url = reverse_lazy('users_list')

    def get_context_data(self, **kwargs):
        context = super(UserAddView, self).get_context_data(**kwargs)
        context['h2'] = 'Добававление сотрудника'
        context['submit_button'] = 'Добававить'

        return context


class UserListView(ListView):
    model = User
    template_name = 'mainapp/users_list.html'
    context_object_name = 'users_list'
    success_url = reverse_lazy('users_list')


class UserEditView(UpdateView):
    model = User
    template_name = 'mainapp/add_update_user.html'
    form_class = UserForm
    success_url = reverse_lazy('users_list')

    def get_context_data(self, **kwargs):
        context = super(UserEditView, self).get_context_data(**kwargs)
        context['h2'] = 'Изменение данных сотрудника'
        context['submit_button'] = 'Сохранить'

        return context


class UserDeleteView(DeleteView):
    model = User
    template_name = 'mainapp/delete_user.html'
    success_url = reverse_lazy('users_list')
