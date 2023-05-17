from django.test import TestCase
from django.urls import reverse


class GetCookieViewTestCase(TestCase):
    def test_get_cookie_view(self):
        response = self.client.get(reverse("myauth:cookie-get"), HTTP_USER_AGENT='test-agent')
        self.assertContains(response, "Cookie value")

class FooBarViewTestCase(TestCase):
    def test_foo_bar_view(self):
        response = self.client.get(reverse("myauth:foo-bar"), HTTP_USER_AGENT='test-agent')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            response.headers['content-type'], 'application/json',
        )
        expected_data = {"foo": "bar", "span": "eggs"}
        self.assertJSONEqual(response.content, expected_data)
