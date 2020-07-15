from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Test APIView """

    def get(self, request, format=None):
        """ Returns a list of APIView features """
        an_apiview = [
            'Uses HTTP methods as function (get, put, post, patch, and delete)',
            'Is similar to a traditional Django View',
            'Gives us the most control over our application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
