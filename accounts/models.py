from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
#from anime.models import Anime


#Anime = get_anime_model()


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='')
    favorite_anime = models.CharField(max_length=100, default='')
    #anime_list = models.ManyToManyField(User, through='AddedAnime')

    def __str__(self):
        return self.user.username

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)


########     unique_together = ('user', 'anime')
