from django.shortcuts import render

from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.decorators import api_view, renderer_classes
#from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

import pandas as pd

# Create your views here.
'''
View to upload a file to the server
'''
class FileUploadView(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request, format=None):
        try:
            file_obj = request.data['file']
            path = default_storage.save('SpectroData/Data/data.xlsx', ContentFile(file_obj.read()))
        except KeyError:
            print('No file attached')
            return Response(status=403)
        return Response(status=204)

@api_view(('GET',))
def read_file(self):

    try:
        file_data = pd.read_excel('SpectroData/Data/ab.xlsx')
        print(type(file_data))
    except FileNotFoundError:
        print("File not uploaded")
        return Response(status=412)
    except:
        print('Something went wrong')
        return Response(status=410)
    return Response(status=200)


@api_view(('GET',))
def filter(self):

    #TODO: Create 3 files with corresponding Coumpund ID endings
    try:
        file_data = pd.read_excel('SpectroData/Data/ab.xlsx')
    except FileNotFoundError:
        print("File not uploaded")
        return Response(status=412)
    except:
        print('Something went wrong')
        return Response(status=410)
    return Response(status=200)


@api_view(('GET',))
def roundoff(self):

    try:
        file_data = pd.read_excel('SpectroData/Data/data.xlsx')
        file_data['Retention Time Roundoff (in mins)'] = round(file_data['Retention time (min)'])
        file_data.to_excel('SpectroData/Data/roundoffdata.xlsx')
    except FileNotFoundError:
        print("File not uploaded")
        return Response(status=412)
    except:
        print('Something went wrong')
        return Response(status=410)

    #TODO: Return roundoffdata.xlsx
   
    return Response(status=200)