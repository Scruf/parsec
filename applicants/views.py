import json
from collections import defaultdict
from django.http import HttpResponse, HttpResponseNotFound
from applications.models import Applicant
from utils.success_messages import success_message
from utils.error_messages import error_message, not_found_message

def index(request):
    applicants = Applicant.objects.all()
    grouped_appicants = defaultdict(list)
    for applicant in applicants:
        grouped_appicants[applicant.name].append({"college":applicant.college, "score":applicant.score})

    return HttpResponse(json.dumps(grouped_appicants), content_type="application/json")


def applications_by_name(request, applicant_name):
    applications = Applicant.objects.filter(name=applicant_name)
    if not applications:
        return HttpResponseNotFound(**not_found_message("No applications exists for that name"))

    response = {
        "name"        : applications[0].name,
        "applications": []
    }
    for application in applications:
        response["applications"].append({"college": application.college, "score": application.score})
    
    return HttpResponse(**success_message(response))