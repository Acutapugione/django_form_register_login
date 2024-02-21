from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import StyleSettings, Notion

# Create your views here.
# def index(request):
#     style_settings, is_created = StyleSettings.objects.get_or_create()
#     context = {
#         "style_settings":style_settings if style_settings.is_active else None
#     }
#     return render(request, "my_app/index.html", context=context)

class IndexView(generic.ListView):
    template_name = "new_app/index.html"
    context_object_name = "items"
    def get_queryset(self) -> QuerySet[Any]:
        return Notion.objects.order_by("-pk")[:5]
    generic.ListView.dispatch
    
class DetailView(generic.DetailView):
    model = Notion
    template_name = "new_app/detail.html"