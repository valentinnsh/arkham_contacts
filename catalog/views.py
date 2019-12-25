from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404 , redirect
from django.db import transaction
from random import randint
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import RandomContactForm
from random import choice
from django.db.models import Count

# Create your views here.

from .models import Expansions, Locations, Contacts

from django.views import generic

class ExpansionsListView(generic.ListView):
    model = Expansions



class ExpansionsDetailView(generic.DetailView):
    model = Expansions

    def get_context_data(self, **kwargs):
        context = super(ExpansionsDetailView, self).get_context_data(**kwargs)
        context['locations'] = Locations.objects.filter(expansion = self.object.id)
        print(context)

        return context

def GiveRandomContact(request):
    if request.method == 'POST':
        form = RandomContactForm(request.POST)
        if form.is_valid():
            loc = form.cleaned_data['locate']
            exp = form.cleaned_data['expansion']
            rcont = Contacts.objects.filter(location = loc).filter(expansion__expansion_name__in=[expan.expansion_name for expan in exp]).distinct()
            if not rcont:
                context = {
                    'form' : form,
                    'mesg' : 'Упс, контакта с такими параметрами не существует. Но вы всегда можете его добавить!'
                }
                return render(request, 'catalog/random_contact.html', context)    
            cont_final = choice(rcont)
            context = {
                'form' : form,
                'contact' : cont_final
            }
            return render(request, 'catalog/random_contact.html', context)
    else:
        form = RandomContactForm()
    context = {
        'form': form
    }
    return render(request, 'catalog/random_contact.html', context)


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """

    num_expansions=Expansions.objects.all().count()
    num_locations=Locations.objects.all().count()
    num_contacts=Contacts.objects.all().count()
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_expansions':num_expansions,'num_locations':num_locations, 'num_contacts':num_contacts},
    )


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class ExpansionsCreate(LoginRequiredMixin, CreateView):
    model = Expansions
    fields = ['expansion_name']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    


class ExpansionsUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Expansions
    fields = ['expansion_name']

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        expansion = self.get_object()
        if self.request.user == expansion.creator:
            return True
        return False

class ExpansionsDelete(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Expansions
    success_url = reverse_lazy('expansions')
    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        expansion = self.get_object()
        if self.request.user == expansion.creator:
            return True
        return False

class LocationsCreate(LoginRequiredMixin, generic.CreateView):
    model = Locations
    fields = ['expansion', 'district', 'location_name']
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    #initial={'creator':,}


class LocationsUpdate(LoginRequiredMixin, UserPassesTestMixin,generic.UpdateView):
    model = Locations
    fields = ['location_name', 'district']
    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        location = self.get_object()
        if self.request.user == location.creator:
            return True
        return False

class LocationsDelete(LoginRequiredMixin, UserPassesTestMixin,generic.DeleteView):
    model = Locations
    success_url = reverse_lazy('/')
    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        location = self.get_object()
        if self.request.user == location.creator:
            return True
        return False


class LocationsDetailView(generic.DetailView):
    model = Locations

    def get_context_data(self, **kwargs):
        context = super(LocationsDetailView, self).get_context_data(**kwargs)
        context['locations'] = Locations.objects.filter(expansion = self.object.id)
        print(context)

        return context

class ContactsDetailView(generic.DetailView):
    model = Contacts

    def get_context_data(self, **kwargs):
        context = super(ContactsDetailView, self).get_context_data(**kwargs)
        context['contacts'] = Contacts.objects.filter(expansion = self.object.id)
        print(context)

        return context
        
class ContactsCreate(LoginRequiredMixin, generic.CreateView):
    model = Contacts
    fields = ['expansion', 'location', 'incident']
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class ContactsUpdate(LoginRequiredMixin, UserPassesTestMixin,generic.UpdateView):
    model = Contacts
    fields = ['location', 'expansion', 'incident']
    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        contact = self.get_object()
        if self.request.user == contact.creator:
            return True
        return False

class ContactsDelete(LoginRequiredMixin, UserPassesTestMixin,generic.DeleteView):
    model = Contacts
    success_url = reverse_lazy('/')
    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        location = self.get_object()
        if self.request.user == location.creator:
            return True
        return False