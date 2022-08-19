from email.policy import default
from django.db import models

class Skills(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    percent = models.IntegerField(default=10,blank=True, null=True)

    def __str__(self):
        return self.name


class MyInfo(models.Model):

    name = models.CharField(max_length=50, blank=True, null=True)
    profile = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    about1 = models.TextField(blank=True, null=True)
    about2 = models.TextField(blank=True, null=True)
    about3 = models.TextField(blank=True, null=True)
    address1 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.CharField(max_length=9, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    slidertext = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    facebook = models.TextField(blank=True, null=True)
    insta = models.TextField(blank=True, null=True)
    twitter = models.TextField(blank=True, null=True)
    github = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name


class Social(models.Model):

    insta = models.TextField(blank=True, null=True)
    facebook = models.TextField(blank=True, null=True)
    twitter = models.TextField(blank=True, null=True)
    linkedin = models.TextField(blank=True, null=True)
    github = models.TextField(blank=True, null=True)
    leetcode = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.id

class FontAwsIcon(models.Model):

    name = models.CharField(max_length=50, blank=True, null=True)
    icon_code = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class Education(models.Model):

    degree = models.CharField(max_length=100, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    year = models.CharField(max_length=50, blank=True, null=True)
    score_name = models.CharField(max_length=50, blank=True, null=True)
    score_value = models.CharField(max_length=50, blank=True, null=True)
    img = models.ImageField(upload_to="", height_field=None,width_field=None, max_length=100,default="img/vit.png")
    proof = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.school + " " + self.degree

class Work(models.Model):

    post = models.CharField(max_length=100, blank=True, null=True)
    comapny = models.CharField(max_length=100, blank=True, null=True)
    year = models.CharField(max_length=50, blank=True, null=True)
    contact_name = models.CharField(max_length=50, blank=True, null=True)
    contact_email = models.CharField(max_length=50, blank=True, null=True)
    img = models.ImageField(upload_to="", height_field=None,width_field=None, max_length=100,default="img/vit.png")
    proof = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.comapny 
        
class Project(models.Model):

    name = models.TextField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to="", height_field=None,width_field=None, max_length=100,default="img/vit.png")

    def __str__(self):
        return self.name 

class Testimonial(models.Model):

    name = models.TextField(blank=True, null=True)
    desg = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to="", height_field=None,width_field=None, max_length=100,default="img/vit.png")

    def __str__(self):
        return self.name 



class Message(models.Model):

    name = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name + " " + str(self.date)

