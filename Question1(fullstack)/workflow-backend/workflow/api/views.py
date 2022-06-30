from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import *
from .serializers import *



class WorkflowDetailsAPIView(GenericAPIView):
    serializer_class = WorkflowDetailsSerializer
    queryset = WorkflowDetails.objects.all()


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "message": "Workflow Initiated Successfully"
            })
        else:
            return Response({
                "status": "success",
                "message": serializer.errors
            })
    

    def get(self, request):
        objects = WorkflowDetails.objects.all()
        serializer = self.serializer_class(objects, many=True)
        return Response({
            "status": "success",
            "data": serializer.data
        })
