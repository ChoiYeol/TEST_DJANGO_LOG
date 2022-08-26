
from multiprocessing import context
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions, generics, status, viewsets
from django.conf import settings
from django.utils import timezone
from .models import (QuickSeqs, Users)
from .serializers import (QuickSeqsSerializer)
from django.contrib.auth import get_user_model
import logging
logger = logging.getLogger('django.server')


import json
from io import StringIO
from rest_framework.parsers import JSONParser




# Create your views here.
@api_view(['GET'])    
def search_medicine_price(self):
 
    try:
 
        # seqs = QuickSeqs.objects.get(index='1')
        serializer = QuickSeqsSerializer.create(index=1)
        print(serializer)
        # serializer = QuickSeqsSerializer(data= {"fk_quick_id":1}) 
        # serializer.is_valid()
        # serializer.save()

    except Exception as e:
            print(e)
    
    # print(settings.DB_NAME)
    return Response('serializer.data', status=status.HTTP_200_OK)

        # model을이용한 crud 완료
        # seqs = QuickSeqs.objects.get(index='1')
        # data = {
        #     'index': seqs.index,
        #     'fk_uuid': seqs.fk_quick_id,
        #     'createdat': seqs.createdat,
        #     'updatedat': seqs.updatedat,
        # }
        # QuickSeqs.objects.create(fk_quick_id=123 )
        # QuickSeqs.objects.filter(index=1).update(fk_quick_id=5 )
        # QuickSeqs.objects.filter(index=6).delete()



# class QuickSeqsListAPIView(generics.ListAPIView):
#     queryset = QuickSeqs.objects.all()
#     serializer_class = QuickSeqs 
 
#     def get_queryset(self):
#         seqs = QuickSeqs.objects.get(index='1')
#         data = {
#             'index': seqs.index,
#             'fk_uuid': seqs.fk_quick_id,
#             'createdat': seqs.createdat,
#             'updatedat': seqs.updatedat,
#         }
#         print(data)
#         return data
