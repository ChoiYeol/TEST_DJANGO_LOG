
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions, generics, status, viewsets
from django.conf import settings
from .models import (QuickSeqs, Users)

import logging
logger = logging.getLogger('django.server')

# Create your views here.
@api_view(['GET'])
def search_medicine_price(request):
 
    try:
        seqs = QuickSeqs.objects.get(index='1')
        data = {
            'index': seqs.index,
            'fk_uuid': seqs.fk_quick_id,
            'createdat': seqs.createdat,
            'updatedat': seqs.updatedat,
        }
        print(data)
        print(Users.objects.get(index='1'))
    except Exception as e:
            print(e)
    
    # print(settings.DB_NAME)
    return Response('res', status=status.HTTP_200_OK)

class QuickSeqsListAPIView(generics.ListAPIView):
    queryset = QuickSeqs.objects.all()
    serializer_class = QuickSeqs 
 
    def get_queryset(self):
        seqs = QuickSeqs.objects.get(index='1')
        data = {
            'index': seqs.index,
            'fk_uuid': seqs.fk_quick_id,
            'createdat': seqs.createdat,
            'updatedat': seqs.updatedat,
        }
        print(data)
        return data
