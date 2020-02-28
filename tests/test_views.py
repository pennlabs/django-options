from django.test import Client, TestCase
from django.urls import reverse

from options.models import Option


class OptionListViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.key = "key"
        self.key2 = "key2"
        self.key3 = "key3"
        self.value = "value"
        self.value2 = "value2"
        self.value3 = "value3"
        self.public = False
        self.public2 = True
        self.public3 = True
        self.option = Option.objects.create(key=self.key, value=self.value, public=self.public)
        self.option2 = Option.objects.create(key=self.key2, value=self.value2, public=self.public2)
        self.option3 = Option.objects.create(key=self.key3, value=self.value3, public=self.public3)

    def test_view(self):
        expected = self.option2.serialize()
        expected.update(self.option3.serialize())
        response = self.client.get(reverse("options:option-list"))
        self.assertEqual(response.json(), expected)
