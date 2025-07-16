from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    # Cascade means: When this note is delete, if user associated with this note wasç deleted, 
    # delete all notes corresponding to this user.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    public = models.BooleanField(default=False)
