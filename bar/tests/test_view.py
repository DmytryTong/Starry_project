from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from bar.models import (
    Position,
    Genre,
    Musician,
    Rockband,
)

POSITION_URL = reverse("bar:position-list")
GENRE_URL = reverse("bar:genre-list")
MUSICIAN_URL = reverse("bar:musician-list")
ROCKBAND_URL = reverse("bar:rockband-list")
VISITOR_URL = reverse("bar:visitor-list")
POSITION_AFTER_SEARCH_URL = reverse("bar:position-list") + "?name=u"
GENRE_AFTER_SEARCH_URL = reverse("bar:genre-list") + "?name=u"
MUSICIAN_AFTER_SEARCH_URL = reverse("bar:musician-list") + "?last_name=u"
ROCKBAND_AFTER_SEARCH_URL = reverse("bar:rockband-list") + "?band_name=a"
VISITOR_AFTER_SEARCH_URL = reverse("bar:visitor-list") + "?username=a"


class PublicPositionTests(TestCase):
    def test_login_required(self):
        res = self.client.get(POSITION_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivatePositionTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="passwordtest6567",
            is_superuser=True,
        )
        self.client.force_login(self.user)

    def test_retrieve_position(self):
        Position.objects.create(
            name="drummer",
        )
        Position.objects.create(
            name="vocal",
        )

        res = self.client.get(POSITION_URL)

        positions = Position.objects.all()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context["position_list"]),
            list(positions)
        )
        self.assertTemplateUsed(res, "bar/position_list.html")

    def retrieve_position_after_search(self):
        positions = Position.objects.filter(
            name__icontains="u"
        )
        res = self.client.get(POSITION_AFTER_SEARCH_URL)
        self.assertEqual(
            list(res.context["position_list"]),
            list(positions)
        )
        self.assertTemplateUsed(res, "taxi/position_list.html")


class PublicGenreTests(TestCase):
    def test_login_required(self):
        res = self.client.get(GENRE_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateGenreTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="passwordtest6567",
        )
        self.client.force_login(self.user)

    def test_retrieve_genre(self):
        Genre.objects.create(
            name="drummer",
            description="description",
        )
        Genre.objects.create(
            name="vocal",
            description="description",
        )

        res = self.client.get(GENRE_URL)

        genres = Genre.objects.all()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context["genre_list"]),
            list(genres)
        )
        self.assertTemplateUsed(res, "bar/genre_list.html")

    def retrieve_genre_after_search(self):
        genres = Genre.objects.filter(
            name__icontains="u"
        )
        res = self.client.get(POSITION_AFTER_SEARCH_URL)
        self.assertEqual(
            list(res.context["genre_list"]),
            list(genres)
        )
        self.assertTemplateUsed(res, "bar/genre_list.html")


class PublicMusicianTests(TestCase):
    def test_login_required(self):
        res = self.client.get(MUSICIAN_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateMusicianTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="passwordtest6567",
            is_superuser=True,
        )
        self.client.force_login(self.user)

        self.position = Position.objects.create(
            name="Drummer",
        )

        self.musician = Musician.objects.create(
            first_name="First_name",
            last_name="Last_nume",
        )
        self.musician.position.set([self.position,])
        self.musician.save()

    def test_retrieve_musician(self):
        musicians = Musician.objects.all()
        res = self.client.get(MUSICIAN_URL)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context["musician_list"]),
            list(musicians)
        )
        self.assertTemplateUsed(res, "bar/musician_list.html")

    def test_retrieve_after_search_musician(self):
        musicians = Musician.objects.filter(
            last_name__icontains="u"
        )
        res = self.client.get(MUSICIAN_AFTER_SEARCH_URL)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context["musician_list"]),
            list(musicians)
        )
        self.assertTemplateUsed(res, "bar/musician_list.html")


class PublicRockbandTests(TestCase):
    def test_login_required(self):
        res = self.client.get(ROCKBAND_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateRockbandTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="passwordtest6567",
            is_superuser=True,
        )
        self.client.force_login(self.user)

        self.position = Position.objects.create(
            name="Drummer",
        )

        self.genre = Genre.objects.create(
            name="Psychorock",
            description="description",
        )

        self.musician = Musician.objects.create(
            first_name="First_name",
            last_name="Last_nume",
        )
        self.musician.position.set([self.position,])
        self.rockband = Rockband.objects.create(
            band_name="UniBand",
            genres=self.genre,
        )
        self.position.musicians.set([self.musician,])

    def test_retrieve_rockband(self):
        rockbands = Rockband.objects.all()
        res = self.client.get(ROCKBAND_URL)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context["rockband_list"]),
            list(rockbands)
        )
        self.assertTemplateUsed(res, "bar/rockband_list.html")

    def test_retrieve_after_search_rockband(self):
        rockbands = Rockband.objects.filter(
            band_name__icontains="a"
        )
        res = self.client.get(ROCKBAND_AFTER_SEARCH_URL)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context["rockband_list"]),
            list(rockbands)
        )
        self.assertTemplateUsed(res, "bar/rockband_list.html")


class PublicVisitorTests(TestCase):
    def test_login_required(self):
        res = self.client.get(VISITOR_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateVisitorTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="passsyh7y6",
            is_superuser=True,
        )
        self.client.force_login(self.user)

    def test_create_visitor(self):
        form_data = {
            "username": "test_username",
            "password1": "pass688uJH",
            "password2": "pass688uJH",
            "first_name": "Test First",
            "last_name": "Test Last",
        }
        self.client.post(
            reverse("bar:visitor-create"),
            data=form_data
        )
        new_user = get_user_model().objects.get(
            username=form_data["username"]
        )

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])

    def test_retrieve_visitor_after_search(self):
        visitors = get_user_model().objects.filter(
            username__icontains="a"
        )
        res = self.client.get(VISITOR_AFTER_SEARCH_URL)

        self.assertEqual(
            list(res.context["visitor_list"]),
            list(visitors)
        )
        self.assertTemplateUsed(res, "bar/visitor_list.html")
