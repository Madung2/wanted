from corporation.models import Recruitment
from corporation.serializers import RecruitmentSerializer


def get_job_post():
    
    recruitments = (Recruitment.objects
    .select_related("tech_stack")
    .select_related("position")
    .select_related("corporation")
    .all())
    serializer = RecruitmentSerializer(recruitments, many=True).data
    return serializer