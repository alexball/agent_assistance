from django.db import models

# Create your models here.

class Call(models.Model):
    # agent, queue, skill, duration, time it's been waiting for help, caller ID,
    agent = models.CharField(max_length=255)
    queue = models.CharField(max_length=255)
    skill = models.CharField(max_length=255)
    request_time = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    purecloud_url = models.URLField(max_length=255)

    def __str__(self):
        return self.agent
