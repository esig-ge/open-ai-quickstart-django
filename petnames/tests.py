from unittest.mock import patch

from django.test import TestCase
#  from openai.openai_object import OpenAIObject

from petnames.views import _generate_prompt


class PetnamesViewTest(TestCase):

    @patch('petnames.views.openai.Completion.create')
    def test_service_is_called_with_correct_prompt(self, mock_create):
        #  If we need to simulate a return value:
        #  mock_create.return_value = OpenAIObject.construct_from(
        #  {'choices': [OpenAIObject.construct_from({'text': 'Truc muche, Machin truc'})] })
        self.client.post('/', {'animal': 'cat'})
        mock_create.assert_called_with(model='text-davinci-002', prompt=_generate_prompt('cat'), temperature=0.6)
