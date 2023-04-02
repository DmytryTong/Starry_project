from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


from bar.models import (
    Visitor,
    Rockband,
    Genre,
    Musician,
    Position,
    Event
)


class EventForm(forms.ModelForm):
    visitors = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    bands = forms.ModelMultipleChoiceField(
        queryset=Rockband.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Event
        fields = "__all__"


class RockbandForm(forms.ModelForm):

    musicians = forms.ModelMultipleChoiceField(
        queryset=Musician.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Rockband
        fields = "__all__"


class MusicianForm(forms.ModelForm):

    position = forms.ModelMultipleChoiceField(
        queryset=Position.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Musician
        fields = "__all__"


class PositionCreationForm(forms.Form):
    class Meta:
        model = Position
        fields = "__all__"


class GenreCreationForm(forms.Form):
    class Meta:
        model = Genre
        fields = "__all__"


class MusicianCreationForm(forms.Form):
    class Meta:
        model = Musician
        fields = "__all__"


class RockbandCreationForm(forms.Form):
    class Meta:
        model = Rockband
        fields = "__all__"


class VisitorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Visitor
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
        )


class EventCreationForm(forms.Form):
    class Meta:
        model = Event
        fields = "__all__"


class PositionSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by position`s name"
            }
        ),
    )


class GenreSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by genre`s name"
            }
        ),
    )


class MusicianSearchForm(forms.Form):
    last_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by musician`s last name"
            }
        ),
    )


class RockbandSearchForm(forms.Form):
    band_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by band`s name"
            }
        ),
    )


class EventSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by event`s name"
            }
        ),
    )


class VisitorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username"
            }
        ),
    )
