from django.contrib import admin
from programs.models import Program


class ProgramAdmin(admin.ModelAdmin):
    pass


admin.site.register(Program, ProgramAdmin)
