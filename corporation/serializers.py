from rest_framework import serializers
from .models import Recruitment

class RecruitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruitment
        fields = '__all__'
        # extra_kwargs= {
        #     "corporation": {"write_only": True},
        #     "corporation": {"write_only": True},
        # }