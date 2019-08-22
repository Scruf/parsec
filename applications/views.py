import json
from collections import defaultdict
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from college.models import College
from utils.error_messages import error_message
from utils.success_messages import object_create
from .models import Applicant


def save_applicant(data):
    validation_fields = set(["college", "name", "score"])

    #Check to see if there is an extra field or misspleled field by taking difference of 2 sets
    data_set = set(data)
    if len(data_set) != 3:
        #Check to see if there is at least 3 fields
        return HttpResponse(**error_message("Invalid post request. Schema does not match"))

    field_difference = validation_fields - data_set
    if field_difference:
        return HttpResponse(**error_message("Invalid post request. Schema does not match"))

    #check to see if the score is in the range
    if data.get("score", 101):
        if data["score"] >= 101 and data["score"] < 0:
            return HttpResponse(**error_message("Score cannot be higher or less than 100"))
    
    #Check to see if there is college
    colleges = College.objects.filter(college_name=data["college"])
    if not colleges:
        college = College(college_name=data["college"])
        college.save()
        applicant = Applicant(**data)
        applicant.college_fk = college
        applicant.save()
        return HttpResponse(**object_create("Application submitted successfully"))
    else:
        #There is a college. So we will try to see if the applicant already applied
        college = colleges[0]

        applicants = Applicant.objects.filter(name=data['name'], college_fk=college.id)
        if applicants:
            return HttpResponse(**error_message("Application already submitted for this college/name pair"))
        
        applicant = Applicant(**data)
        applicant.college_fk = college
        applicant.save()
        return HttpResponse(**object_create("Application submitted successfully"))
    

@csrf_exempt
def index(request):
    if request.method == 'POST':
        return save_applicant(json.loads(request.body))
    else:
        return HttpResponse(**error_message("Not implemented"))