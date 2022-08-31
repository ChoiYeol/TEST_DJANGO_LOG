from ..models import (QuickSeqs )
from ..serializers import (QuickSeqsSerializer)
import logging
logger = logging.getLogger('django.server')


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions, status, generics

#FBV
@api_view(['GET', 'POST']) 
def apiViewTest(request):
    print('gogo :'+request)
    return Response('data', status=status.HTTP_200_OK)


#CBV
class QuickSeqsGeneric(generics.GenericAPIView):

    def testFunc(self, request):
        
        print(self)
        print(request)
        print('가즈아 ~~~')
        
#CBV
class QuickSeqsAPI(viewsets.ModelViewSet):
    queryset = QuickSeqs.objects.all()
    serializer_class = QuickSeqs 
    
    def createFunc(self, request):
        try:
            result = QuickSeqs.objects.create(fk_quick_id=123 )
            return Response({'result': result}, status=status.HTTP_200_OK)

        except Exception as e:
            
            return Response(status=status.HTTP_400_BAD_REQUEST)        
    
    def readFunc(self, request):
        try:
            result = QuickSeqs.objects.get(index='1')
            return Response({'result': result}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)        
        
    
    def updateFunc(self, request):
        try:
            result = QuickSeqs.objects.filter(index=1).update(fk_quick_id=5 )
            return Response({'result': result}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def deleteFunc(self, request):
        try:
            result = QuickSeqs.objects.filter(index=6).delete()
            return Response({'result': result}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)