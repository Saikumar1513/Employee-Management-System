from django.db import models
from employees.models import Employee

class Performance(models.Model):
    RATING_CHOICES = (
        (1, '1 - Poor'),
        (2, '2 - Below Average'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    )
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performances')
    rating = models.IntegerField(choices=RATING_CHOICES)
    review_date = models.DateField()
    comments = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.employee.name} - {self.rating} - {self.review_date}"
    
    class Meta:
        ordering = ['-review_date']