from rest_framework import viewsets, status
from ..models import (QuickSeqs )
from ..serializers import (QuickSeqsSerializer)
from rest_framework.response import Response


import logging
logger = logging.getLogger('django.server')

class QuickSeqsAPI(viewsets.ModelViewSet):
    queryset = QuickSeqs.objects.all()
    serializer_class = QuickSeqs 

    def testFunc(self, request):
        validated_data= {"fk_quick_id":1}
        ttt = QuickSeqsSerializer.create( validated_data )
        print(ttt)
        
    
    def createFunc(self, request):
        try:
            validated_data = {"fk_quick_id":1}
            result = QuickSeqsSerializer.create( validated_data )
            return Response({'result : ': result}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)        
    
    def readFunc(self, request):
        try:
            result = QuickSeqs.objects.get(index='1')
            return Response({'result : ': result}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)        
        
    
    def updateFunc(self, request):
        try:
            result = QuickSeqs.objects.filter(index=1).update(fk_quick_id=5 )
            return Response({'result : ': result}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def deleteFunc(self, request):
        try:
            result = QuickSeqs.objects.filter(index=6).delete()
            return Response({'result : ': result}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)