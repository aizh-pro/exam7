from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView

from webapp.forms import PollChoiceForm
from webapp.models import Choice, Poll


class IndexView(ListView):
    # template_name = 'task/index.html'
    context_object_name = 'choices'

    def get_context_data(self,*, object_list=None, **kwargs):
        return super().get_context_data(object_list=object_list,**kwargs)

    def get_queryset(self):
        data = Choice.objects.all()
        return data

class PollChoiceCreateView(CreateView):
    model = Choice
    template_name = 'choice/choice_create.html'
    form_class = PollChoiceForm

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.poll = poll
        choice.save()
        return redirect('poll_view', pk=poll.pk)