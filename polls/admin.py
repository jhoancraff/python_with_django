from django.contrib import admin

from .models import Choice, Nombre, Question

# Register your models here.

class LhoiceInline(admin.StackedInline):
    model = Choice
    extraa = 6

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "quiestion_text"]
    inlines = [LhoiceInline]
    list_display = ("quiestion_text", "pub_date", "was_plublished_recently" )
    list_filter = ["pub_date"]
    search_fields = ["quiestion_text"]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Nombre)
