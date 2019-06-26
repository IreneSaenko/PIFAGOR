from django.shortcuts import render
from Answers.models import Answers
from django.http import HttpResponseRedirect


def  first(request):
    return render(request, 'Answers/form.html')

def second(request):

    topic = request.POST['Topic']
    text = request.POST['Text']
    name = request.POST['Name']
    email = request.POST['Email']
    if (topic != '') and (text != '') and (name != '') and (email != ''):
        ans = Answers()
        ans.topic = topic
        ans.text = text
        ans.name = name
        ans.email = email
        ans.save()
        return render(request, 'Answers/submit.html', {'name': name})
    else:
        warn = 'Не все поля заполнены!'
        not_val = True
        return render(request, 'Answers/form.html', {'warn': warn, 'not_val': not_val})


