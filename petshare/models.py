from django.db import models

# Create your models here.
class Post(models.Model):
    TYPES = (
        (0, 'Other'),
        (1, 'Cat'),
        (2, 'Dog'),
        (3, 'Guinea Pig'),
        (4, 'Hamster'),
        (5, 'Poring'),
        (6, 'Dragon')
    )
    nickname = models.CharField(max_length=128, null=False, default='Unknown')
    pet_name = models.CharField(max_length=128, null=False, default='Unknown Pet')
    pet_type = models.IntegerField(choices=TYPES, null=False, default=0)
    comment = models.CharField(max_length=128, null=True, default='')
    photo = models.FileField(upload_to='petshare/static/uploads', verbose_name='filepath', default=None)
    date_posted = models.DateTimeField(verbose_name='Upload date', auto_now=True)

    @property
    def pet_type_str(self):
        return self.TYPES[self.pet_type][1]

    @property
    def photo_path(self):
        return str(self.photo).replace('petshare/', '')

class Vote(models.Model):
    nickname = models.CharField(max_length=128, null=False, default='Unknown')
    photo_id = models.ForeignKey(Post, on_delete=models.CASCADE)