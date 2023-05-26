from django.contrib.auth.models import User
from django.db import models

def upload_avatar_to(instance: "Profile", filename: str) -> str:
    return "avatars/user_{user_id}/{filename}".format(
        user_id=instance.user_id,
        filename=filename,
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    agreement_accepted = models.BooleanField(default=False)
    avatar = models.ImageField(null=True, blank=True, upload_to=upload_avatar_to)
