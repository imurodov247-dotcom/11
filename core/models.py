from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

# Create your models here.


class Xodim(models.Model):
    name = models.CharField()
    age = models.IntegerField(validators=[MinValueValidator(18)])
    position = models.CharField()
    salary = models.DecimalField(max_digits=10,decimal_places=2 )
    join_date = models.DateField(default=timezone.now(),blank=True)
    city = models.CharField()
    department = models.CharField(choices=[
        ("IT",'IT department'),
        ('HR','HRdepartment'),
        ('STUDY', 'Study department'),
        ('SALES','Sales department')
        
    ], default="IT")
    
    
    def __str__(self):
        return self.name
    
    class Meta :
        verbose_name = 'Xodim'
        verbose_name_plural = 'Xodimlar'
        