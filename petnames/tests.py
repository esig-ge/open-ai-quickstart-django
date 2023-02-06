from unittest.mock import patch
from django.test import TestCase
from petnames.views import _generate_prompt


class PetnamesViewTest(TestCase):

    @patch('openai.Completion.create')
    def test_service_is_called_with_correct_prompt(self, mock_create):
        #  If we need to simulate a return value:
        #  mock_create.return_value = OpenAIObject.construct_from(
        #  {'choices': [OpenAIObject.construct_from({'text': 'Truc muche, Machin truc'})] })
        self.client.post('/', {'animal': 'cat'})
        mock_create.assert_called_with(
            model='text-davinci-002',
            prompt=_generate_prompt('cat'),
            temperature=0.6)

    @patch('openai.Completion.create')
    def test_redirect_to_same_page(self, mock_create):

        class Object(object):
            pass

        apiresponse = Object()
        choice0 = Object()
        choice0.text = 'smurfresult'
        apiresponse.choices = [choice0]

        mock_create.return_value = apiresponse

        response = self.client.post('/', {'animal': 'smurf'})
        self.assertRedirects(response, '/smurfresult/')
