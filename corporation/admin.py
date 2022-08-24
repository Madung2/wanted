from django.contrib import admin
from .models import (
    Corporation,
    TechStack,
    Position,
    Recruitment,
    Recruiter,
    )
# Register your models here.
admin.site.register(Corporation)
admin.site.register(TechStack)
admin.site.register(Position)
admin.site.register(Recruitment)
admin.site.register(Recruiter)
