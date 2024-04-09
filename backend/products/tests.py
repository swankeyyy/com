from django.test import TestCase
from django.urls import reverse

class ProductListViewTestCase(TestCase):

    def test_main_view(self):
        path = reverse('main_page_view')
        response = self.client.get(path)
        self.assertEquals(response.status_code, 200)

    def test_detail_view(self):
        path = reverse("sorted_view")
        response = self.client.get(path)
        self.assertEquals(response.status_code, 200)

