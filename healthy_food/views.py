from django.shortcuts import render
from programs.models import Program

TAGS_MAP = {
    '1': 'Lose weight',
    '2': 'Gain muscle mass',
    '3': 'Maintain result',
    '4': 'Program for moms',
}


def main(request):
    tag = request.GET.get('tag')
    program_objects = Program.objects.all()
    if tag:
        program_objects = program_objects.filter(tag=TAGS_MAP[tag])

    context = {"programs": program_objects}
    return render(request, "main.html", context)


def about_us(request):
    return render(request, "about-us.html")


def how_it_works(request):
    return render(request, "how-it-works.html")


def contacts(request):
    return render(request, "contacts.html")

