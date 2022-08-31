from django.urls import path 
from .views.modelCrud import (QuickSeqsAPI, apiViewTest)

urlpatterns = [
    # model 기준 crud
    path('m_apiview/', apiViewTest, name="apiViewTest"), #api_view test
    path('m_test/', QuickSeqsAPI.as_view({"post": "testFunc"})),
    path('m_create/', QuickSeqsAPI.as_view({"post": "createFunc"})),
    path('m_read/', QuickSeqsAPI.as_view({"get": "readFunc"})),
    path('m_update/', QuickSeqsAPI.as_view({"patch": "updateFunc"})),
    path('m_delete/', QuickSeqsAPI.as_view({"delete": "deleteFunc"})),
    
    # modelSerializerCrud 기준 crud
    path('ms_test/', QuickSeqsAPI.as_view({"post": "testFunc"})),
    path('ms_create/', QuickSeqsAPI.as_view({"post": "createFunc"})),
    path('ms_read/', QuickSeqsAPI.as_view({"get": "readFunc"})),
    path('ms_update/', QuickSeqsAPI.as_view({"patch": "updateFunc"})),
    path('ms_delete/', QuickSeqsAPI.as_view({"delete": "deleteFunc"})),
 

]
