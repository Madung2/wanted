from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recruitment, TechStack, Position
from .serializers import RecruitmentSerializer
# Create your views here.
class RecruitmentView(APIView):
    def get(self, request):
        recruitments = Recruitment.objects.all()
        serializer = RecruitmentSerializer(recruitments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        # user = request.user
        # request.data['user'] = user.id
        request.data['position'] = Position.objects.get(name=request.data['position']).id
        print(TechStack.objects.get(name=request.data['tech_stack']).id)

        request.data['tech_stack']=TechStack.objects.get(name=request.data['tech_stack']).id
        serializer = RecruitmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyRecruitmentView(APIView):
    def get(self, request, pk):
        recruitment = Recruitment.objects.get(pk=pk)
        serializer = RecruitmentSerializer(recruitment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):    

        if request.data['position']:
            request.data['position'] = Position.objects.get(name=request.data['position']).id
        if request.data['tech_stack']:
            request.data['tech_stack']=TechStack.objects.get(name=request.data['tech_stack']).id
        recruitment = Recruitment.objects.get(pk=pk)
        serializer = RecruitmentSerializer(recruitment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        recruitment = Recruitment.objects.get(pk=pk)
        recruitment.delete()
        return Response({"massege" : "삭제 성공"},status=status.HTTP_200_OK)



