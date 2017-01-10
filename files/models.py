import uuid
import os

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from beGis.utils.mixins import Timestampable

from django.utils import timezone


# Create your models here.
def file_upload_formater(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{0}.{1}'.format(uuid.uuid4(), ext)
    now = timezone.now()
    return now.strftime(os.path.join('files/%Y/%m/%d', filename))


class File(Timestampable):
    owner = models.ForeignKey(
        User,
        verbose_name=_('user')
    )

    file = models.FileField(
        blank=True, null=True,
        upload_to=file_upload_formater,
        verbose_name=_('File')
    )
