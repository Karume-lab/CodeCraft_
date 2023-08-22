from django.db import models

# Create your models here.
class ProjectModel(models.Model):
    user = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=45)
    date_created = models.DateField(auto_now=True, auto_now_add=False)
    date_due = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    WORKING_ON = 'w'
    PENDING = 'p'
    COMPLETED = 'c'
    DRAFT = 'd'
    STATUS_CHOICES = [
        (WORKING_ON, 'Working on'),
		(PENDING, 'Pending'),
		(COMPLETED, 'Completed'),
		(DRAFT, 'Draft'),
	]
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default=PENDING)
    image = models.ImageField(upload_to='projects/', height_field=None, width_field=None, null=True, blank=True)
