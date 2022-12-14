from django.db import models
from user.models import User

class Post(models.Model):
    image = models.ImageField(upload_to="post_pics")
    content = models.TextField(max_length=180)
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    
    like_authors = models.ManyToManyField(User, related_name='like_posts')
    bookmark_authors = models.ManyToManyField(User, related_name='bookmark_posts')
    
    def __str__(self):
        return self.content
    
class Comment(models.Model):
    content = models.TextField(max_length=50, blank=False)
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return self.content
