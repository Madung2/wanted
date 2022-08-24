from rest_framework import serializers
from .models import Recruitment



class RecruitmentSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()
    position_name = serializers.SerializerMethodField()
    stack_name = serializers.SerializerMethodField()
    # country = serializers.SerializerMethodField()
    def get_company_name(self,obj):
        return obj.corporation.name
    def get_position_name(self,obj):
        return obj.position.name
    def get_stack_name(self,obj):
        return obj.tech_stack.name

    # def get_country(self,obj):
    #     obj.corporation.name
    #     return 
    


    class Meta:
        model = Recruitment
        fields = ['id', 'company_name', 'position_name', 'country','region','stack_name', 'corporation','position','recompense','content','tech_stack']
        extra_kwargs = {
            "corporation": {"write_only": True},
            "position": {"write_only": True},
            "tech_stack": {"write_only": True},
        }

