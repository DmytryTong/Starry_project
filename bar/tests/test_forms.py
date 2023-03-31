from django.test import TestCase

from bar.forms import VisitorCreationForm


class FormsTests(TestCase):

    def test_visitor_creation_form_first_last_names_correct(self):
        form_data = {
            "username": "test_username",
            "password1": "pass688uJH",
            "password2": "pass688uJH",
            "first_name": "First",
            "last_name": "Last",
        }
        form = VisitorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
