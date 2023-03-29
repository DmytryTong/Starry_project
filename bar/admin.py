from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from bar.models import (
    Genre,
    Position,
    Musician,
    Rockband,
    Event,
    Visitor
)

# Register your models here.
admin.site.register(Genre)
admin.site.register(Position)
admin.site.register(Musician)
admin.site.register(Rockband)
admin.site.register(Event)
# admin.site.register(Visitor, UserAdmin)

@admin.register(Visitor)
class DriverVisitor(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                    )
                },
            ),
        )
    )
