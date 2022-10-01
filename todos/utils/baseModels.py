from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField( auto_now=True, editable=False)

    class Meta:
        abstract=True


class BaseArchiveModel(models.Model):
    is_archived = models.BooleanField(default=False)
    archived_at = models.DateTimeField(null=True)
          
    class Meta:
        abstract = True
            
    def archive(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()