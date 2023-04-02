from django.test import TestCase

from bar.forms import (
    VisitorCreationForm,
    GenreSearchForm,
    MusicianSearchForm,
    PositionSearchForm,
    RockbandSearchForm,
    EventSearchForm,
    VisitorSearchForm
)


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

    def test_genre_search_form_valid(self):
        data = {
            'name': 'Metal',
        }
        form = GenreSearchForm(data=data)
        self.assertTrue(form.is_valid())

    def test_genre_search_form_invalid(self):
        data = {
            'name': '',
        }
        form = GenreSearchForm(data=data)
        self.assertFalse(form.is_valid())

    def test_musician_search_form_valid(self):
        data = {
            'last_name': 'Lennon',
        }
        form = MusicianSearchForm(data=data)
        self.assertTrue(form.is_valid())

    def test_musician_search_form_invalid(self):
        data = {
            'last_name': '',
        }
        form = MusicianSearchForm(data=data)
        self.assertFalse(form.is_valid())

    def test_position_search_form_valid(self):
        data = {
            'name': 'Drummer',
        }
        form = PositionSearchForm(data=data)
        self.assertTrue(form.is_valid())

    def test_position_search_form_invalid(self):
        data = {
            'name': '',
        }
        form = PositionSearchForm(data=data)
        self.assertFalse(form.is_valid())

    def test_rockband_search_form_valid(self):
        data = {
            'band_name': 'Led Zeppelin',
        }
        form = RockbandSearchForm(data=data)
        self.assertTrue(form.is_valid())

    def test_rockband_search_form_invalid(self):
        data = {
            'band_name': '',
        }
        form = RockbandSearchForm(data=data)
        self.assertFalse(form.is_valid())

    def test_event_search_form_valid(self):
        data = {
            'name': 'New Year Party',
        }
        form = EventSearchForm(data=data)
        self.assertTrue(form.is_valid())

    def test_event_search_form_invalid(self):
        data = {
            'name': '',
        }
        form = EventSearchForm(data=data)
        self.assertFalse(form.is_valid())

    def test_visitor_search_form_valid(self):
        data = {
            'username': 'john_doe',
        }
        form = VisitorSearchForm(data=data)
        self.assertTrue(form.is_valid())

    def test_visitor_search_form_invalid(self):
        data = {
            'username': '',
        }
        form = VisitorSearchForm(data=data)
        self.assertFalse(form.is_valid())
