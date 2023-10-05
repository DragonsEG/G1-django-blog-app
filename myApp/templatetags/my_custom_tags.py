from django import template
from myApp.models import *

register = template.Library() 

@register.filter(name='has_group') 
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists() 

@register.filter(name='isCompanyEmployee') 
def isCompanyEmployee(user, company_id):
    company = Company.objects.get(ID=company_id)
    userProf = UserProfile.objects.get(user=user)
    return userProf.company == company

@register.filter(name='isCompanyManager')  
def isCompanyManager(user, company_id):
    company = Company.objects.get(ID=company_id)
    return company.manager == user