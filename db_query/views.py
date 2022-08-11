from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonForm
from .models import Person, State, City


def person_create_view(request):
    """creates a new user"""
    form = PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("person_add")
    return render(request, "home.html", {"form": form})


def person_update_view(request, pk):
    """updates a existing user"""
    person = get_object_or_404(Person, pk=pk)
    form = PersonForm(instance=person)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect("person_change", pk=pk)
    return render(request, "home.html", {"form": form})


def load_states(request):
    """ajax call for loading states"""
    country_id = request.GET.get("country_id")
    states = State.objects.filter(country_id=country_id).all()
    return render(request, "state_dropdown_list_options.html", {"states": states})


# # AJAX
# def load_cities(request):
#     country_id = request.GET.get("country_id")
#     cities = City.objects.filter(country_id=country_id).all()
#     return render(
#         request, "persons/city_dropdown_list_options.html", {"cities": cities}
#     )
#     # return JsonResponse(list(cities.values('id', 'name')), safe=False)
