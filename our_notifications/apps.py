# from django.apps import AppConfig
from notifications.apps import Config as NotificationConfig

class OurNotificationsConfig(NotificationConfig):
    name = 'our_notifications'
    label = 'our_notifications'
