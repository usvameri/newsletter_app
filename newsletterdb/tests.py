from django.test import TestCase
from . import models
# Create your tests here.


class NewsletterTestCase(TestCase):

    def setUp(self):
        models.Newsletter.objects.create(title="Test Newsletter", description="This is a test newsletter",
                                         content="This is the content of the test newsletter")

    def test_newsletter_content(self):
        newsletter = models.Newsletter.objects.get(id=1)
        expected_object_name = f'{newsletter.title}'
        print('(Created by test)Newsletter title: ', newsletter.title)
        self.assertEquals(expected_object_name, 'Test Newsletter')



