from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from webapp.forms import PollForm
from webapp.models import Poll


class PollListView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'polls'
    paginate_by = 5

    def get_context_data(self,*, object_list=None, **kwargs):
        return super().get_context_data(object_list=object_list,**kwargs)

    def get_queryset(self):
        data = Poll.objects.all()
        return data


class PollView(DetailView):
    template_name = 'polls/poll_view.html'
    model = Poll
    # paginate_polls_by = 5
    # paginate_polls_orphans = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PollCreateView(CreateView):
    template_name = 'polls/poll_create.html'
    form_class = PollForm
    model = Poll

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollUpdateView(UpdateView):
    template_name = 'polls/poll_update.html'
    form_class = PollForm
    model = Poll


    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})