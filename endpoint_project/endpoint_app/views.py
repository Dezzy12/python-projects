from django.http import JsonResponse
from datetime import datetime

def endpoint_view(request):
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')
    current_day = datetime.now().utcnow().strftime('%A')
    utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    github_file_url = "https://github.com/Dezzy12/python-projects/blob/master/endpoint_project/endpoint_app/views.py"
    github_repo_url = "https://github.com/Dezzy12/python-projects/tree/master/endpoint_project"

    response={
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return JsonResponse(response)