from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import PollForm
from webapp.models import Poll


class PollListView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'polls'
    paginate_by = 5
    paginate_orphans = 0

    def get_context_data(self,*, object_list=None, **kwargs):
        return super().get_context_data(object_list=object_list,**kwargs)

    def get_queryset(self):
        data = Poll.objects.all()
        return data.order_by('-created_at')


class PollView(DetailView):
    template_name = 'polls/poll_view.html'
    model = Poll
    paginate_choices_by = 5
    paginate_choices_orphans = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # choices, page, is_paginated = self.paginate_choices(self.object)
        choices = self.paginate_choices(self.object)
        context['choices'] = choices
        # context['page_obj'] = page
        # context['is_paginated'] = is_paginated

        return context

    def paginate_choices(self, poll):
        choices = poll.poll.all()
        return choices
        # if choices.count() > 0:
        #     paginator = Paginator(choices, self.paginate_choices_by, orphans=self.paginate_choices_orphans)
        #     page_number = self.request.GET.get('page', 1)
        #     page = paginator.get_page(page_number)
        #     is_paginated = paginator.num_pages > 1
        #     return page.object_list, page, is_paginated
        # else:
        #     return choices, None, False


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


class PollDeleteView(DeleteView):
    template_name = 'polls/poll_delete.html'
    model = Poll
    context_object_name = 'poll'
    success_url = reverse_lazy('index')