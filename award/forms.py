from django import forms
from .models import Project, Profile, Comment
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['bio','profile_picture'] 
        exclude=['user','projects','contact']  

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','design','usability','content','vote_submissions']

class VoteForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['design','usability','content']


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['comment_image','posted_by','profile']