from django.shortcuts import render
from .forms import ElementaryForm, HighSchoolForm, SeniorHighForm

def elementary_view(request):
    if request.method == "POST":
        form = ElementaryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = ElementaryForm()

    return render(request, "enroll.html", {"form": form})


def highschool_view(request):
    if request.method == "POST":
        form = HighSchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = HighSchoolForm()

    return render(request, "enroll.html", {"form": form})


def seniorhigh_view(request):
    if request.method == "POST":
        form = SeniorHighForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = SeniorHighForm()

    return render(request, "enroll.html", {"form": form})
