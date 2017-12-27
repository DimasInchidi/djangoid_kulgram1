from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class UserProfile(models.Model):
    NONE = 'N'
    FEMALE = 'F'
    MALE = 'M'
    OTHER = 'O'
    SEX_CHOICES = (
        (NONE, _('None')),
        (FEMALE, _('Female')),
        (MALE, _('Male')),
        (OTHER, _('Other')),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(max_length=255, blank=True, default='')
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=SEX_CHOICES)
    photo = models.ImageField(upload_to=user_directory_path, default="avatar/default.jpg", null=True, blank=True)
