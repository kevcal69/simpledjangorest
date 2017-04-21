# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from rest_framework.views import View


class SimpleView(View):
    def get(self, request):
        return JsonResponse(
            {"data": "This is the data", "isPython": 1})
