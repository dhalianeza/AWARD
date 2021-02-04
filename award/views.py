from django.http  import HttpResponse,Http404
import datetime as dt 
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Project, Profile, Comment
from .forms import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
from rest_framework import status

# Create your views here.
def welcome(request):
    projects = Project.objects.all()

    return render(request, 'welcome.html',{"projects":projects})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('welcome')

    else:
        form = ProjectForm()
    return render(request, 'new_post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile(request, username=None):
	'''
	Method that fetches a users profile page
	'''
	current_user = request.user
	pi_images = Project.objects.filter(user=current_user)

	return render(request,"profile.html",{"pi_images":pi_images})

@login_required(login_url='/accounts/login/')
def profile_edit(request):
    current_user=request.user
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.user=current_user
            image.save()
        return redirect('profile')
    else:
        form=ProfileForm()
    return render(request,'profile_edit.html',{"form":form})

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_articles = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def project(request,project_id):
  
       project = Project.objects.filter(id=project_id).first()
       average_score = round(((project.design + project.usability + project.content)/3),2)
       if request.method == 'POST':
           vote_form = VoteForm(request.POST)
           if vote_form.is_valid():
               project.vote_submissions+=1
               if project.design == 0:
                   project.design = int(request.POST['design'])
               else:
                   project.design = (project.design + int(request.POST['design']))/2
               if project.usability == 0:
                   project.usability = int(request.POST['usability'])
               else:
                   project.usability = (project.usability + int(request.POST['usability']))/2
               if project.content == 0:
                   project.content = int(request.POST['content'])
               else:
                   project.content = (project.content + int(request.POST['usability']))/2
               project.save()
               return redirect('project', project_id)
       else:
           vote_form = VoteForm()

           return render(request,'project.html',{"vote_form":vote_form,"project":project,"average_score":average_score})

@login_required(login_url='/accounts/login/')     
def add_comment(request,project_id):
    current_user=request.user
    if request.method=='POST':
        image_item=Project.objects.filter(id=project_id).first()

    
        form=CommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.posted_by=current_user
            comment.comment_image=image_item
            comment.save()
        return redirect('welcome')
    else:
        form=CommentForm()
    return render(request,'comment.html',{"form":form,"project_id":project_id})

class ProfileList(APIView):
    def get(self, request, format=None):
        all_users = Profile.objects.all()
        serializers = ProfileSerializer(all_users, many=True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)
