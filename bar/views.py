from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from bar.forms import (
    PositionSearchForm,
    GenreSearchForm,
    MusicianSearchForm,
    RockbandSearchForm,
    EventSearchForm,
    VisitorCreationForm,
    VisitorSearchForm,
    EventForm,
    RockbandForm,
    MusicianForm
)
from bar.models import (
    Genre,
    Event,
    Rockband,
    Position,
    Musician,
    Visitor
)


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of this site"""

    num_events = Event.objects.count()
    num_bands = Rockband.objects.count()
    num_musicians = Musician.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_events": num_events,
        "num_bands": num_bands,
        "num_musicians": num_musicians,
        "num_visits": num_visits + 1,
    }

    return render(request, "bar/index.html", context=context)


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PositionListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = PositionSearchForm(initial={
            "name": name
        })

        return context

    def get_queryset(self):
        queryset = Position.objects.all()
        form = PositionSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )

        return queryset


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("bar:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("bar:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("bar:position-list")


class GenreListView(LoginRequiredMixin, generic.ListView):
    model = Genre
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GenreListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = GenreSearchForm(initial={
            "name": name
        })

        return context

    def get_queryset(self):
        queryset = Genre.objects.all()
        form = GenreSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )

        return queryset


class GenreDetailView(LoginRequiredMixin, generic.DetailView):
    model = Genre


class GenreCreateView(LoginRequiredMixin, generic.CreateView):
    model = Genre
    fields = "__all__"
    success_url = reverse_lazy("bar:genre-list")


class GenreUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Genre
    fields = "__all__"
    success_url = reverse_lazy("bar:genre-list")


class GenreDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Genre
    success_url = reverse_lazy("bar:genre-list")


class MusicianListView(LoginRequiredMixin, generic.ListView):
    model = Musician
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MusicianListView, self).get_context_data(**kwargs)

        last_name = self.request.GET.get("last_name", "")

        context["search_form"] = MusicianSearchForm(initial={
            "last_name": last_name
        })

        return context

    def get_queryset(self):
        queryset = Musician.objects.all()
        form = MusicianSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                last_name__icontains=form.cleaned_data["last_name"]
            )

        return queryset


class MusicianDetailView(LoginRequiredMixin, generic.DetailView):
    model = Musician


class MusicianCreateView(LoginRequiredMixin, generic.CreateView):
    model = Musician
    form_class = MusicianForm
    success_url = reverse_lazy("bar:musician-list")


class MusicianUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Musician
    form_class = MusicianForm
    success_url = reverse_lazy("bar:musician-list")


class MusicianDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Musician
    success_url = reverse_lazy("bar:musician-list")


class RockbandListView(LoginRequiredMixin, generic.ListView):
    model = Rockband
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RockbandListView, self).get_context_data(**kwargs)

        band_name = self.request.GET.get("band_name", "")

        context["search_form"] = RockbandSearchForm(initial={
            "band_name": band_name
        })

        return context

    def get_queryset(self):
        queryset = Rockband.objects.all()
        form = RockbandSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                band_name__icontains=form.cleaned_data["band_name"]
            )

        return queryset


class RockbandDetailView(LoginRequiredMixin, generic.DetailView):
    model = Rockband


class RockbandCreateView(LoginRequiredMixin, generic.CreateView):
    model = Rockband
    form_class = RockbandForm
    success_url = reverse_lazy("bar:rockband-list")


class RockbandUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Rockband
    form_class = RockbandForm
    success_url = reverse_lazy("bar:rockband-list")


class RockbandDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Rockband
    success_url = reverse_lazy("bar:rockband-list")


class VisitorListView(LoginRequiredMixin, generic.ListView):
    model = Visitor
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VisitorListView, self).get_context_data(**kwargs)

        username = self.request.GET.get("username", "")

        context["search_form"] = VisitorSearchForm(initial={
            "username": username
        })

        return context

    def get_queryset(self):
        queryset = Visitor.objects.all()
        form = VisitorSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )

        return queryset


class VisitorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Visitor
    queryset = Visitor.objects.prefetch_related("events__visitors")


class VisitorCreateView(generic.CreateView):
    model = Visitor
    form_class = VisitorCreationForm
    success_url = reverse_lazy("bar:event-list")


class VisitorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Visitor
    fields = "__all__"
    success_url = reverse_lazy("bar:index")


class VisitorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Visitor
    success_url = reverse_lazy("bar:index")


class EventListView(LoginRequiredMixin, generic.ListView):
    model = Event
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = EventSearchForm(initial={
            "name": name
        })

        return context

    def get_queryset(self):
        queryset = Event.objects.all()
        form = EventSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )

        return queryset


class EventDetailView(LoginRequiredMixin, generic.DetailView):
    model = Event


class EventCreateView(LoginRequiredMixin, generic.CreateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy("bar:event-list")


class EventUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy("bar:event-list")


class EventDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Event
    success_url = reverse_lazy("bar:event-list")


@login_required
def toggle_assign_to_events(request, pk):
    visitor = Visitor.objects.get(id=request.user.id)
    if (
        Event.objects.get(id=pk) in visitor.events.all()
    ):
        visitor.events.remove(pk)
    else:
        visitor.events.add(pk)
    return HttpResponseRedirect(reverse_lazy("bar:event-list"))
