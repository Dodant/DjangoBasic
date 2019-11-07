from django.contrib import admin
from .models import Candidate, Poll, Choice, Image

admin.site.register(Candidate)
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Image)