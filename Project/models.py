from django.db import models
from users_auth.models import Users
# Create your models here.

class Categories(models.Model):
    title = models.CharField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Projects(models.Model):
    title = models.CharField(max_length=100,unique=True)
    details = models.TextField(null=True)
    totaltaget = models.IntegerField()
    rate = models.FloatField(default=0.0)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='users')
    cat = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='categories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Project_pics(models.Model):
    picture = models.ImageField()
    prj_pic = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='oproject')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Project_tags(models.Model):
    title = models.CharField(max_length=100)
    prj_tag = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='tproject')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Project_comments(models.Model):
    title = models.CharField(max_length=100)
    prj_comment = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='cproject')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class comment_reply(models.Model):
    reply = models.CharField(max_length=100)
    comment = models.OneToOneField(Project_comments, on_delete=models.CASCADE, related_name='comment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Project_User_Donation(models.Model):
    prj = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='dproject')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user')
    rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



