from django.db import models
from user.models import User

class Country(models.Model):
    name = models.CharField('국가', max_length=50)
    def __str__(self):
        return self.name
    
class Region(models.Model):
    name = models.CharField('지역', max_length=50)
    def __str__(self):
        return self.name
        
class Corporation(models.Model):
    name = models.CharField('회사', max_length=50)
    country = models.ForeignKey(Country, verbose_name='국가', on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Region, verbose_name='지역', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name
    
class TechStack(models.Model):
    name = models.CharField('기술스택', max_length=50)
    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField('채용포지션', max_length=100)
    def __str__(self):
        return self.name

class Recruitment(models.Model):
    corporation = models.ForeignKey(Corporation, verbose_name='회사명', on_delete=models.CASCADE)
    position = models.ForeignKey(Position, verbose_name='채용포지션', on_delete=models.SET_NULL, null=True)
    recompense = models.IntegerField('채용보상금')
    content = models.TextField('채용내용')
    tech_stack = models.ManyToManyField(TechStack, verbose_name='사용기술', related_name='stacks')
    def __str__(self):
        return f'{str(self.corporation)} / {str(self.position)}'
    
class Recruiter(models.Model):
    user = models.ForeignKey('user.User', verbose_name='인사담당자', on_delete=models.CASCADE)
    recruitment = models.ManyToManyField(Recruitment, verbose_name='채용공고', related_name='recruitments')
    def __str__(self):
        return str(self.user)