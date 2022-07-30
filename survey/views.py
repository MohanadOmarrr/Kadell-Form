from django.shortcuts import render, redirect


# Create your views here.
def survey(request):
    return render(request, 'survey.html')