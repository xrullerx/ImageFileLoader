from django.db import models
from .validators import validate_file_extension

# Create your models here.
class Image(models.Model):
   name = models.CharField(u"Название", max_length = 50)
   image = models.ImageField(u"Изображение", upload_to = 'pictures', null =  True, blank = True,
                             validators=[validate_file_extension])
   description = models.TextField(u"Описание")

   class Meta:
      db_table = "image"

   def __str__(self):
      return self.name