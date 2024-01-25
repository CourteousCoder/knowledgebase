import json
from dal import autocomplete
from kb.models.simple_models import TopicArea
from people_depot.models import PracticeArea, Tool, User
from kb.models import AssetGroup


class UserAutocomplete(autocomplete.Select2QuerySetView):
    model = User
    search_fields = ["username"]
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return User.objects.none()

        qs = User.objects.all()

        if self.q:
            qs = qs.filter(username__contains=self.q)

        return qs

class AssetGroupAutocomplete(autocomplete.Select2QuerySetView):
    model = AssetGroup
    # search_fields = ["title"]
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return AssetGroup.objects.none()

        qs = AssetGroup.objects.all()

        if self.q:
            qs = qs.filter(name__contains=self.q)

        return qs

class PracticeAreaAutocomplete(autocomplete.Select2QuerySetView):
    print("debug a1")
    model = PracticeArea
    # search_fields = ["title"]
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return PracticeArea.objects.none()

        qs = PracticeArea.objects.all()

        if self.q:
            qs = qs.filter(name__contains=self.q)

        return qs

class TopicAreaAutocomplete(autocomplete.Select2QuerySetView):
    print("debug a2")
    model = TopicArea
    # search_fields = ["title"]
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return TopicArea.objects.none()

        qs = TopicArea.objects.all()

        if self.q:
            qs = qs.filter(name__contains=self.q)

        return qs

class ToolAutocomplete(autocomplete.Select2QuerySetView):
    print("debug a3")
    model = Tool
    # search_fields = ["title"]
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Tool.objects.none()

        qs = Tool.objects.all()

        if self.q:
            qs = qs.filter(name__contains=self.q)

        return qs