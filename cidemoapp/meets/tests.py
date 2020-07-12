from django.test import TestCase
from .models import Event

class MeetsTestCase(TestCase):
    @classmethod
    def setUp(cls):
        Event.objects.create(name="Tom" , description="Jerry")

    def test_event_name(self):
        event=Event.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Name')


