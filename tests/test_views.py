from django.test import Client, TestCase
from django.urls import reverse

from options.models import Option


class OptionListViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.key = "key"
        self.key2 = "key2"
        self.value = "value"
        self.value2 = "value2"
        self.option = Option.objects.create(key=self.key, value=self.value)
        self.option2 = Option.objects.create(key=self.key2, value=self.value2)

    def test_view(self):
        expected = self.option.serialize()
        expected.update(self.option2.serialize())
        response = self.client.get(reverse("options:option-list"))
        self.assertEqual(response.json(), expected)
