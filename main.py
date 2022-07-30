from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError


def homepage(request):

    try:
        age = request.GET['age']
        return render(request, 'index.html', {"age": age})

    except MultiValueDictKeyError:
        pass

    return render(request, 'index.html')