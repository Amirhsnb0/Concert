from django.db import models
from django.contrib.auth.models import User


class PorfileModel (models.Model):
    class Meta:
        verbose_name="پروفایل "
        verbose_name_plural = " پروفایل  "
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    Profleimage =models.ImageField(upload_to=('profileimages/'), verbose_name="تصویر پروفایل")

    man=1
    voman=2
    status_choices =((man,"مرد"), (voman,"زن"))
    status = models.IntegerField(choices=status_choices, verbose_name="جنسیت")
    credit=models.IntegerField(default=0)
    
    