from django.shortcuts import render
from django.views.generic import View, ListView
from django.db.models import Q
from django.http import HttpResponseRedirect, request
from django.urls import reverse
from .forms import *

from .models import *
# Create your views here.


class DashboardView(View):

    def get(self, request):
        return render(request, 'new/dashboard.html')


class RuView(ListView):
    paginate_by = 4
    model = Ru
    template_name = 'new/table-ru.html'
    context_object_name = 'table-ru'

    def get_queryset(self):
        return Ru.objects.all().filter(Q(stable_status='Offline') | Q(stable_status='Lost_registration'))

    def get_context_data(self, **kwargs):
        context = {
            'whatsapp': super().get_context_data(
                object_list=self.get_queryset().filter(transport="Whatsapp"), **kwargs),
            'viber': super().get_context_data(
                object_list=self.get_queryset().filter(transport="Viber"))
        }
        return context


class EuroView(ListView):
    paginate_by = 4
    model = Euro
    template_name = 'new/table-euro.html'
    context_object_name = 'table-euro'

    def get_queryset(self):
        return Euro.objects.all().filter(Q(stable_status='Offline') | Q(stable_status='Lost_registration'))

    def get_context_data(self, **kwargs):
        context = {
            'wa': super().get_context_data(
                object_list=self.get_queryset().filter(transport="Whatsapp"), **kwargs),
            'vib': super().get_context_data(
                object_list=self.get_queryset().filter(transport="Viber"))
        }
        return context


class FreeView(ListView):
    paginate_by = 2
    model = Free
    template_name = 'new/free.html'
    context_object_name = 'free_ru'

    def get_queryset(self):
        return Free.objects.all().filter(status="Free")

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['bs'] = self.get_queryset().filter(type="BS")
    #     context['clicker'] = self.get_queryset().filter(type="Clicker")
    #     return context
    def get_context_data(self, **kwargs):
        context = {
            'bs': super().get_context_data(
                object_list=self.get_queryset().filter(type="BS"), **kwargs),
            'clicker': super().get_context_data(
                object_list=self.get_queryset().filter(type="Clicker"))
        }
        return context


class HomeView(View):

    def get(self, request):
        return render(request, 'new/home.html')


class UserView(View):

    def get(self, request):
        return render(request, 'new/user.html')


class AllUsersView(ListView):
    model = User
    template_name = 'new/all-users.html'
    context_object_name = 'allusers'

    def get_queryset(self):
        return User.objects.all()


class NotificationsView(View):

    def get(self, request):
        users = User.objects.using('my_sql').all()
        print('================================================')
        print(users)
        return render(request, 'new/notifications.html')


class LoginView(View):

    def get(self, request):
        return render(request, 'registration/login2.html')


class LogoutView(View):

    def get(self, request):
        return render(request, 'registration/logged_out.html')


class RegistrationView(View):
    def get(self, request):
        return render(request, 'registration/register.html')
