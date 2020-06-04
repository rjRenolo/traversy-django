from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# admin.site.register(Question)
# admin.site.register(Choice)

# choices within question pages
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldSets = [(None, {'fields': ['question_text']}), 
    ('Date Information', {'fields': ['pub_date'], 'classes':['collapes']}),]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)