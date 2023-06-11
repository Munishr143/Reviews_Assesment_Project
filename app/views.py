from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def Home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        #Questions=Question.objects.all()
        d={'username':username}
        return render(request, 'home.html', d)
    
    return render(request, 'home.html')


def Registration(request):
    UFO=User_Form()
    d={'UFO':UFO}

    if request.method=='POST':
        UFD=User_Form(request.POST)

        if UFD.is_valid():
            NSUO=UFD.save(commit=False)
            NSUO.set_password(UFD.cleaned_data['password'])
            NSUO.save()

            send_mail('Registration', 
                      'Sucessfully Registration is done', 
                      'munishr428@gmail.com', 
                      [NSUO.email], 
                      fail_silently=False)
            return render(request, 'home.html')
        else:
            return HttpResponse('Data is not Valid')
        
    return render(request, 'registration.html', d)


def User_Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        AUO=authenticate(username=username, password=password)

        if AUO and AUO.is_active:
            login(request, AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('Home'))
        
        else:
            return HttpResponse('Invalid username or password')

    return render(request, 'User_Login.html')


@login_required
def User_Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Home'))


@login_required
def Change_Password(request):
    username=request.session.get('username')
    d={'username':username}

    if request.method=='POST':
        password=request.POST['password']
        UO=User.objects.get(username=username)
        UO.set_password(password)
        UO.save()
        return HttpResponseRedirect(reverse('User_Login'))
    
    return render(request, 'Change_Password.html', d)


def Forget_Password(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        UO=User.objects.filter(username=username)

        if UO:
            UO[0].set_password(password)
            UO[0].save()
        else:
            return HttpResponse('Invalid Username')
        
        return HttpResponseRedirect(reverse('User_Login'))
    
    return render(request, 'Forget_Password.html')


@login_required
def Ask_Question(request):
    if request.session.get('username'):
        QFO=Question_Form()
        username=request.session.get('username')
        d={'QFO':QFO, 'username':username}

        if request.method=='POST':
            QFD=Question_Form(request.POST)
            UO=User.objects.filter(username=username)

            if QFD.is_valid():
                NSQO=QFD.save(commit=False)
                NSQO.username=UO[0]
                NSQO.save()

                return HttpResponseRedirect(reverse('Home'))
            
            else:
                return render(request, 'askquestion.html', d)
            
        return render(request, 'askquestion.html', d)
    

@login_required
def display_questions(request):
    if request.session.get('username'):
        username=request.session.get('username')
        Questions=Question.objects.all()
        d={'username':username, 'Questions':Questions}
        return render(request, 'display_questions.html', d)


@login_required
def Answer_the_Questions(request):
    if request.session.get('username'):
        AFO=Answer_Form()
        username=request.session.get('username')
        questions=Question.objects.all()
        d={'AFO':AFO, 'username':username, 'questions':questions}

        if request.method=='POST':
            AFD=Answer_Form(request.POST)
            UO=User.objects.get(username=username)

            if AFD.is_valid():
                NSAO=AFD.save(commit=False)
                NSAO.username=UO
                NSAO.save()

                QO=NSAO.question
                AO=Answer.objects.filter(question=QO)
                print(AO)
            
                return HttpResponseRedirect(reverse('Home'))
            
            else:
                return render(request, 'Answer_the_Questions.html', d)
            
        return render(request, 'Answer_the_Questions.html', d)
    

@login_required
def display_answers(request):
    if request.session.get('username'):
        username=request.session.get('username')
        Questions=Question.objects.all()
        Answers=Answer.objects.all()
        d={'username':username, 'Questions':Questions, 'Answers':Answers}
        return render(request, 'display_answers.html', d)
