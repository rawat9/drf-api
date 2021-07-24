from django.http.response import JsonResponse
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(APIView):
	def get(self, request, *args, **kwargs):
		data = {
			'name':'John',
			'age': 30
		}
		return Response(data)