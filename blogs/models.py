from django.contrib.auth.models import User
from django.db import models


class Blogs(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.CharField(max_length=400, null=False)
    author = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    

class Comment(models.Model):
    content = models.CharField(max_length=100, null=False)
    commentator = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    source_post = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

