from django.shortcuts import render
from django.http import HttpResponse

# Importing modules
import json
from .models import Activity, User

# Create your views here.
def index(request):

    usersList = User.objects.order_by('realName')
    # users = ", ".join([user.realName for user in usersList])

    activityList = Activity.objects.all()
    # activities = ", ".join([activity.user.userId for activity in activityList])


    # Get all users as dict
    activityDict = {}
    for user in usersList:
        activityDict[user.userId] = {}
        activityDict[user.userId]["id"] = user.userId
        activityDict[user.userId]["real_name"] = user.realName
        activityDict[user.userId]["tz"] = user.timeZone
        activityDict[user.userId]["activity_periods"] = []

    # Store all activities to respective users
    for activity in activityList:
        timePeriodDict = {}
        # Format timestamp using strftime
        try:
            startTime = activity.startTime.strftime("%b %d %Y   %H:%M%p")
        except:
            print("Invalid Datetime format.")
            startTime = None

        timePeriodDict["start_time"] = startTime

        try:
            endTime = activity.endTime.strftime("%b %d %Y   %H:%M%p")
        except:
            print("Invalid Datetime format.")
            endTime = None
        timePeriodDict["end_time"] = endTime

        activityDict[activity.user.userId]["activity_periods"].append(timePeriodDict)


    finalOutput = {}
    finalOutput["ok"] = True
    finalOutput["members"] = list(activityDict.values())

    # Dump dict as string using json module
    outputStr = json.dumps(finalOutput)

    return HttpResponse(outputStr, content_type='application/json')
