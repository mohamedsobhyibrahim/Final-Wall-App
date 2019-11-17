from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #return '/detail/{}'.format(self.pk)
        return reverse('detail' , args=[self.pk])


    #python manage.py makemigrations
    #python manage.py migrate
    #To create this model as sql

    class Meta:
        ordering = ('-post_date',)

class comment (models.Model):
    name = models.CharField(max_length=50)
    email=models.EmailField()
    body = models.TextField()
    comment_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)
    posts= models.ForeignKey(post , on_delete=models.CASCADE , related_name='comments')

    def __str__(self):
        return 'comment {} on {}.'.format(self.name , self.posts)

        # class Meta:
        #     ordering('-comment_date',)

        class Meta:
            ordering = ('-comment_date',)

