from django.contrib import admin

# Register your models here.
from .models import Query, QueryResponse
admin.site.register(Query)
admin.site.register(QueryResponse)