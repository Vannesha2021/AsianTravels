from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class BlogPost (models.Model):

    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog")
    slug = models.CharField(max_length=130, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    spotlight_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    dateTime = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    hearts = models.ManyToManyField(
        User, related_name='blog_likes', blank=True)

class Meta:
    ordering = ['-created_on']

    def __str__(self):
        return str(self.author) + " Blog Title: " + self.title

    def get_absolute_url(self):
        return reverse('blogs')

    def number_of_hearts(self):
         return self.hearts.count()

    
class Comment (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    content = models.TextField()
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    dateTime = models.DateTimeField(default=now)

class Meta:
    ordering = ['-created_on']

    def __str__(self):
        return self.user.username + " Comment: " + self.content

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_image = CloudinaryField('image', default='profileimage')
    bio = models.TextField(blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return str(self.user)
