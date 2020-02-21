from django.http import JsonResponse
from django.views import View

from options.models import Option


class OptionListView(View):
    def get(self, request):
        options = Option.objects.all()
        option_list = []
        for o in options:
            option_list.append({"key": o.key, "value": o.value})
        return JsonResponse({"Status": 200, "Options": option_list})
