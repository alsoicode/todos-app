from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    user = models.ForeignKey(User, editable=False)
    title = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.title
