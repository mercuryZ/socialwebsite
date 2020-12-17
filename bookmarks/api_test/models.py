from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length = 250)
    add_time = models.DateField(auto_now_add = True)

    def __unicode__(self):
        return self.book_name