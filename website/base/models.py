from django.db import models

from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()

class BlogPost(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=250)
	description = models.TextField()
	image = models.ImageField(upload_to='image/', blank=True, null=True)

	def __str__(self):
		return self.title

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
	comment = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.comment