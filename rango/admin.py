from .models.category import Category
from .models.page import Page
from django.contrib import admin


admin.site.register(Category)
admin.site.register(Page)
