from django import forms

from .models import Person, State, District, City


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["state"].queryset = State.objects.none()
        self.fields["district"].queryset = District.objects.none()

        if "country" in self.data:
            try:
                country_id = int(self.data.get("country"))
                self.fields["state"].queryset = State.objects.filter(
                    country_id=country_id
                ).order_by("name")
                if "state":
                    state_id = int(self.data.get("state"))
                    self.fields["district"].queryset = District.objects.filter(
                        state_id=state_id
                    ).order_by("name")
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty state queryset
        elif self.instance.pk:
            self.fields["state"].queryset = self.instance.country.state_set.order_by(
                "name"
            )
