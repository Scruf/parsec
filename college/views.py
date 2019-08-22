from django.http import HttpResponse, HttpResponseNotFound
from .models import College
from applications.models import Applicant
from utils.success_messages import success_message
from utils.error_messages import not_found_message

def index(request):
    colleges = College.objects.all()

    response = []

    for college in colleges:
        college_name = college.college_name
        
        applicants = Applicant.objects.filter(college_fk=college)
        
        college_dcit = {college_name:[]}

        college_dcit[college_name] = [{"Name":applicant.name, "score":applicant.score} for applicant in applicants]
        response.append(college_dcit)
        
    return HttpResponse(**success_message(response))


def applicants_by_college(request, college_name):
    applicants = Applicant.objects.filter(college=college_name)

    if  not applicants:
        return HttpResponseNotFound(**not_found_message("No applications exists for that college"))
    
    response = {"college": college_name, "applications":[{"name":applicant.name, "score":applicant.score} for applicant in applicants]}
    return HttpResponse(**success_message(response))
