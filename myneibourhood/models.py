from django.db import models

# Create your models here.
class NeighbourHood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_lenght=70)
    admin = models.ForeignKey("Profile",on_delete=models.CASCADE,related_name='hood')
    hood_logo =  models.ImageField(upload_to='static/static_dirs/images/')
    description = models.TextField()
    health_info = models.IntegerField(null=True,blank=True)
    health_officer = models.CharField(max_length=60, null=True,)
    police_info = models.IntegerField(null=True, blank=True)
    police_officer=models.CharField(max_length=60,null=True, blank=True)

    def __str__(self):
        return f'{self.name} hood'

    def create_neighborhood(self):
        self.save()

    def delete_neibourhood(self):
        self.delete()

    @classmethod
    def find_neibourhood(cls, neibourhood_id):
        return cls.objects.filter(id=neibourhood_id)
        