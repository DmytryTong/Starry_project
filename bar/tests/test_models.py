from django.contrib.auth import get_user_model
from django.test import TestCase

from bar.models import (
    Position,
    Genre,
    Musician,
    Rockband,
    Event,
)


class ModelTests(TestCase):

    def test_position_str(self):
        position_ = Position.objects.create(
            name="test",
        )

        self.assertEqual(
            str(position_),
            f"{position_.name}"
        )

    def test_genre_str(self):
        genre_ = Genre.objects.create(
            name="test",
        )

        self.assertEqual(
            str(genre_),
            f"{genre_.name}"
        )

    def test_musician_str(self):
        position_ = Position.objects.create(
            name="test",
        )
        musician_ = Musician.objects.create(
            first_name="first_test",
            last_name="last_test",
        )
        musician_.position.set([position_,])
        self.assertEqual(
            str(musician_),
            f"Name: {musician_.first_name} {musician_.last_name} ("
            f"{', '.join(musician_.position.values_list('name', flat=True))})"
        )

    def test_rockband_str(self):
        position_ = Position.objects.create(
            name="test",
        )
        genre_ = Genre.objects.create(
            name="test",
        )
        musician_ = Musician.objects.create(
            first_name="first_test",
            last_name="last_test",
        )
        musician_.position.set([position_,])
        rockband_ = Rockband.objects.create(
            band_name="test_band_name",
            genres=genre_,
        )
        rockband_.musicians.set([musician_,])
        self.assertEqual(
            str(rockband_),
            f"{rockband_.band_name}"
        )

    def test_event_str(self):
        position_ = Position.objects.create(
            name="test",
        )
        position_.save()
        genre_ = Genre.objects.create(
            name="test",
        )
        musician_ = Musician.objects.create(
            first_name="first_test",
            last_name="last_test",
        )
        musician_.position.set([position_,])
        musician_.save()
        rockband_ = Rockband.objects.create(
            band_name="test_band_name",
            genres=genre_,
        )
        rockband_.musicians.set([musician_,])
        rockband_.save()
        visitor_ = get_user_model().objects.create_user(
            username="test_user",
            password="testpassword8766",
        )
        event_ = Event.objects.create(
            show_time="2023-03-29 14:30:45.123456",
            name="TestName",
            ticket_cost=200.00,
        )
        event_.bands.set([rockband_,])
        event_.visitors.set([visitor_,])

        self.assertEqual(
            str(event_),
            f"{event_.name}"
        )

    def test_create_visitor(self):
        username = "test username"
        password = "testFry27uw"
        first_name = "Test-name First"
        last_name = "Test-name Last"
        visitor_ = get_user_model().objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        self.assertEqual(visitor_.username, username)
        self.assertTrue(visitor_.check_password(password))
