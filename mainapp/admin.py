from django.contrib import admin

from mainapp.models import ProgrammingLanguage, Departament, User

admin.site.register(User)
admin.site.register(Departament)
admin.site.register(ProgrammingLanguage)