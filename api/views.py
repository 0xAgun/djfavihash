import mmh3
import requests
import codecs
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

@api_view(['POST'])
def data(request):
    url = request.data['urls']
    try:
        response = requests.get(url, verify=False)
        if (response.status_code != 404):
            favicon = codecs.encode(response.content,"base64")
            hash_favicon = mmh3.hash(favicon)
            print(hash_favicon)
            return Response(hash_favicon)
    except Exception as e:
        pass

    
    return Response("Enter a valid site for a valid favicon hash")


order_by = openapi.Parameter('urls', openapi.IN_QUERY,
                             description="field you want to order by to",
                             type=openapi.TYPE_STRING)



class favicon(APIView):

    @swagger_auto_schema(
        operation_description="enter urls for the hash. use json urls key",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['urls'],
            properties={
                'urls': openapi.Schema(type=openapi.TYPE_STRING)
            },
        ),
        security=[],
    )
    def post(self, request):
        url = request.data['urls']
        try:
            response = requests.get(url, verify=False)
            if (response.status_code != 404):
                favicon = codecs.encode(response.content,"base64")
                hash_favicon = mmh3.hash(favicon)
                print(hash_favicon)
                return Response(hash_favicon)
        except Exception as e:
            varialbe = {"failed": "there was an error to generating hash"}
            return Response(varialbe)