from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
all_answers = []


def survey(request):
    global all_answers
    try:
        all_answers = [request.GET['q1'], request.GET['q2'], request.GET['q3'], request.GET['q4'], request.GET['q5'],
                       request.GET['q6'], request.GET['q7'], request.GET['q8'], request.GET['q9'], request.GET['q10'],
                       request.GET['q11']]

        # with open("file.txt", 'a') as datafile:
        #     for answer in all_answers:
        #         datafile.write(f"\n{answer}\n")

        return render(request, 'submit.html')

    except MultiValueDictKeyError:
        pass

    return render(request, 'survey.html')


def submit(request):
    try:
        name = request.GET['name']
        email = request.GET['email']
        password = request.GET['password']

        print(all_answers)

        with open('file.txt', 'a') as datafile:
            for answer in all_answers:
                datafile.write(f"{answer}\n")
            datafile.write(f"\nname:{name}\nemail:{email}\nphone:{password}\n---------------------")

        return render(request, 'done.html')

    except MultiValueDictKeyError:
        pass

    return render(request, 'submit.html')


def done(request):
    return render(request, 'done.html')