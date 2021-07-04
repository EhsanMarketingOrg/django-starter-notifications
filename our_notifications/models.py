from django.db import models
from notifications.base.models import AbstractNotification


class Notification(AbstractNotification):
    # custom field example
    category = models.CharField(max_length=20, null=True, blank=True)

    class Meta(AbstractNotification.Meta):
        abstract = False
        app_label = 'our_notifications'