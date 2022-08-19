from django.contrib import messages
from re import sub
from django.shortcuts import render,redirect
from .models import Education, FontAwsIcon, Message, MyInfo, Project, Skills, Testimonial, Work

def index(request):

    skills = Skills.objects.all().values()
    info = MyInfo.objects.all().values().first()
    icons = FontAwsIcon.objects.all().values()
    educations = Education.objects.all().values()
    works = Work.objects.all().values()
    projects = Project.objects.all().values()
    testimonial = Testimonial.objects.all().values()
    empty = ""

    dict = {
        'skills' : skills,
        'info' : info,
        'icons' : icons,
        'educations' : educations,
        'works' : works,
        'projects' : projects,
        'testimonial' : testimonial,
        'empty' : empty,
    }
    
    if request.method == 'POST':

        skills = Skills.objects.all().values()
        info = MyInfo.objects.all().values().first()
        icons = FontAwsIcon.objects.all().values()
        educations = Education.objects.all().values()
        works = Work.objects.all().values()
        projects = Project.objects.all().values()
        testimonial = Testimonial.objects.all().values()
        empty = ""

        dict = {
            'skills' : skills,
            'info' : info,
            'icons' : icons,
            'educations' : educations,
            'works' : works,
            'projects' : projects,
            'testimonial' : testimonial,
            'empty' : empty,
        }

        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        

        obj = Message.objects.create(name=name,email=email,message=message,subject=subject)
        messages.success(request,'Message sent successfully.')

        return render(request,'index.html',dict)

    return render(request,'index.html',dict)



