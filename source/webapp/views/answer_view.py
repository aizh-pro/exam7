from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View
from webapp.models import Poll, Choice


class AnswerView(TemplateView):
   template_name = 'answer/answer.html'

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)

       pk = self.kwargs.get('pk')
       poll = get_object_or_404(Poll, pk=pk)
       choices = poll.poll.all()
       context['poll'] = poll
       context['choices'] = choices
       return context



