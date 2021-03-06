from django.conf import settings
from django.db import models
from django.utils import timezone

#Creates an object Post that has author, title, text, and dates as attributes
#Let's you publish and then pass the title of the post when you publish
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #This is how we publish our postings
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    #Returns only comments that are approved
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


#Creates an object Comment. Takes a post, author, texxt, date, and comment-approval
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    #Approves and saves comment
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
