from django.db import models

# Create your models here.
class Author (models.Model):
    first_name = models.CharField( max_length= 80)
    last_name = models.CharField( max_length= 80)
    birth_date= models.DateField ( null=True, help_text= "iveskite data" )
    # null = true leis palikti tuscia langeli
    # saugoti kada buvo sukurtas ar atnaujintas irasas
    created_at = models.DateTimeField( auto_now_add= True)
    update_at = models.DateTimeField( auto_now= True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    # cover = models.ImageField('Virselis', upload_to='cover, null= True, blank = True ')