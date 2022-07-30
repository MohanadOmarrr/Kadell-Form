from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def survey(request):
    try:
        all_answers = [request.GET['q1'], request.GET['q2'], request.GET['q3'], request.GET['q4'], request.GET['q5'],
                       request.GET['q6'], request.GET['q7'], request.GET['q8'], request.GET['q9'], request.GET['q10'],
                       request.GET['q11']]

        with open("file.txt", 'w') as datafile:
            for answer in all_answers:
                datafile.writelines(f"{answer}\n")

        return render(request, 'index.html', {"all_answers": all_answers})

    except MultiValueDictKeyError:
        pass

    return render(request, 'survey.html')