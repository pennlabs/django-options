from django.http import JsonResponse
from django.views import View

from options.models import Option


class OptionListView(View):
    """
    Sends public options as json data
    """
    def get(self, request):
        options = Option.objects.filter(public=True)
        option_dict = {}
        for o in options:
            option_dict.update(o.serialize())
        return JsonResponse(option_dict)
