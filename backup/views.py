import os, json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from college.models import College
from applications.models import Applicant
from utils.success_messages import success_message
# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'POST':
        colleges = College.objects.all()

        response = []

        for college in colleges:
            college_name = college.college_name
            
            applicants = Applicant.objects.filter(college_fk=college)
            
            college_dcit = {college_name:[]}

            college_dcit[college_name] = [{"Name":applicant.name, "score":applicant.score} for applicant in applicants]
            response.append(college_dcit)
     
        with open(os.environ["EGORS_TEST_BACUP"], "w") as f:
            json.dump(response, f)
        
        return HttpResponse(**success_message({"message":"Backup successful"}))
