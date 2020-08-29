from django.shortcuts import render


def index_view(request):
    return render(request, 'rename/index.html')
