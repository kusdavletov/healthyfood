from django.shortcuts import render
from programs.models import Program

TAGS_MAP = {
    '1': 'Lose weight',
    '2': 'Gain muscle mass',
    '3': 'Maintain result',
    '4': 'Program for moms',
}


def programs(request):
    tag = request.GET.get('tag')
    program_objects = Program.objects.all()
    if tag:
        program_objects = program_objects.filter(tag=TAGS_MAP[tag])

    context = {"programs": program_objects}
    return render(request, "programs.html", context)


def program_info(request, pk):
    program = Program.objects.get(pk=pk)
    prohibitions = program.prohibition.splitlines()
    context = {"program": program, "prohibitions": prohibitions}
    return render(request, "program_info.html", context)
