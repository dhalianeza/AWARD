from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.eve = Profile( profile_picture  = '/', bio = 'my tests', contact='uevelyne44@gmail.com')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.eve,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.eve.save_profile()
        eve = Profile.objects.all()
        self.assertTrue(len(eve) > 0)

    def tearDown(self):
        Profile.objects.all().delete()
        

class ProjectTestClass(TestCase):
    def setUp(self):
        self.delani = Project( title  = 'delani', description = 'my tests', photo = '/',  link = 'github.com', design='5', usability ='6', content = '7',vote_submissions= '7')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.delani,Project))

    # Testing Save Method
    def test_save_method(self):
        self.delani.save_project()
        delani = Project.objects.all()
        self.assertTrue(len(delani) > 0)

    def tearDown(self):
        Project.objects.all().delete()


