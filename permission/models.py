from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models


class User(AbstractUser):
    is_blogger = models.BooleanField(default=False, help_text='Can update posts', null=True, blank=True)
    is_manager = models.BooleanField(default=False, help_text='Can approve posts', null=True, blank=True)

    def set_manager(self):
        group, created = Group.objects.get_or_create(name='Managers')
        if created:
            content_types = ContentType.objects.get_for_models(
                Blogger, PostManager,
            )
            group.permissions.add(Permission.objects.get(codename='change_blooger',
                                                         content_type=content_types[Blogger]))

            group.permissions.add(Permission.objects.get(codename='change_postmanager',
                                                         content_type=content_types[PostManager]))

            group.permissions.add(Permission.objects.get(codename='delete_blogger',
                                                         content_type=content_types[Blogger]))
        self.groups.add(group)

    @property
    def is_manager(self):
        return self.groups.filter(name="Managers").exists()


class Blogger(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        permissions = [('search_blogger', 'Can search blogger')]

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('permission.Blogger', on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.author.name, self.title)

class PostManager(models.Model):
    post = models.OneToOneField('permission.Post', on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=(('RJ','REJECT'), ('AP','APPROVE'), ('W','Waiting')), default="Waiting")

    def __str__(self):
        return "{} - {}".format(self.status, self.post)
