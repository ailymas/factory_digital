from django.db import models

class User(models.Model):
    email=models.EmailField(max_length=50, null=False,blank=False)

    def __str__(self):
        return self.email

class Todo(models.Model):
    title=models.CharField(max_length=50, null=False,blank=False)
    description=models.CharField(max_length=50, null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True )

    def __str__(self):
        return self.title
