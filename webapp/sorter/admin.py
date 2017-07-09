from django.contrib import admin

# Register your models here.
from .models import SortedIdols, SuggestedIdols, MergeSortChoices

admin.site.register([SortedIdols, SuggestedIdols, MergeSortChoices])