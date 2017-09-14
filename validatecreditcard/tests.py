import unittest

from pyramid import testing

from validatecreditcard.views import card_valid_view


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()


class FunctionalTests(unittest.TestCase):

    def test_card(self):
        from .views import my_view
        request = testing.DummyRequest()
        request.params["number"] = '4253625879615786'
        info = card_valid_view(request)
        self.assertEqual(info['message'], 'Valid Card')

