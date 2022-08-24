from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recruitment
from .serializers import RecruitmentSerializer
# Create your views here.
class RecruitmentView(APIView):
    def get(self, request):
        recruitments = Recruitment.objects.all().order_by('-created_at')[:20]
        serializer = RecruitmentSerializer(recruitments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        user = request.user
        request.data['user'] = user.id
        serializer = RecruitmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


