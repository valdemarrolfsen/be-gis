from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from beGis.utils.mixins import Descriptable, Timestampable


# Tutorial models
class Tutorial(Descriptable, Timestampable):
    number = models.IntegerField(
        _('number')
    )

    steps = models.ManyToManyField(
        'Step',
        verbose_name=_('steps'),
        blank=True
    )

    @property
    def step_count(self):
        return self.steps.count()

    def __str__(self):
        return '{}'.format(self.title)


class Step(Descriptable):
    objective = models.ForeignKey(
        'Objective',
        verbose_name=_('objective')
    )

    def __str__(self):
        return '{}'.format(self.title)


class Objective(models.Model):
    type = models.CharField(
        _('type'),
        max_length=255
    )

    case = models.CharField(
        _('case'),
        max_length=255
    )

    value = models.IntegerField(
        _('value')
    )

    def __str__(self):
        return '{}, {}'.format(self.type, self.case)


class Result(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_('user')
    )

    tutorial = models.ForeignKey(
        'Tutorial',
        verbose_name=_('tutorial')
    )
