from django.core.management.base import BaseCommand
from manageactivity.models import User, Activity


class Command(BaseCommand):
    help = 'Update Database'

    def add_arguments(self, parser):
        parser.add_argument('--action', type=str,  help = "adduser, modifyuser, deleteuser, addactivity, modifyactivity, deleteactivity")
        parser.add_argument('--id', type=str,  default=None )
        parser.add_argument('--real_name', type=str, default=None)
        parser.add_argument('--tz', type=str, default=None)
        parser.add_argument('--start_time', type=str, default=None)
        parser.add_argument('--end_time', type=str, default=None)

    def handle(self, *args, **kwargs):

        actionToPerform = kwargs['action']
        action = getattr(Command, actionToPerform)
        action(self, **kwargs)


    def adduser(self, **kwargs):
        id = kwargs["id"]
        realName = kwargs["real_name"]
        tz = kwargs["tz"]
        userObj = User(userId = id, realName = realName, timeZone = tz)
        userObj.save()

    def deleteuser(self, **kwargs):
        id = kwargs["id"]

        usersList = User.objects.filter(userId=id)
        if len(usersList) < 1:
            # User not found.
            self.stdout.write("User " + str(id) + " not found!")
            return
        try:
            for usr in usersList:
                usr.delete()
        except Exception as ex:
            print(ex)
            pass

    def modifyuser(self, **kwargs):

        id = kwargs["id"]
        realName = kwargs["real_name"]
        tz = kwargs["tz"]

        usersList = User.objects.filter(userId=id)
        if len(usersList) < 1:
            # User not found.
            self.stdout.write("User " + str(id) + " not found!")
            return
        try:
            for usr in usersList:
                if realName is not None:
                    usr.realName = realName
                if tz is not None:
                    usr.timeZone = tz
                usr.save()

        except Exception as ex:
            print(ex)
            pass

    def addactivity(self, **kwargs):
        userid = kwargs["id"]
        startTime = kwargs["start_time"]
        endTime = kwargs["end_time"]
        usersList = User.objects.filter(userId=userid)
        if len(usersList) < 1:
            # User not found.
            self.stdout.write("User " + str(userid) + " not found!")
            return
        try:
            for usr in usersList:
                actvty = Activity(user = usr , startTime = startTime, endTime = endTime)
                actvty.save()
        except Exception as ex:
            print(ex)

    def modifyactivity(self, **kwargs):
        userid = kwargs["id"]
        startTime = kwargs["start_time"]
        endTime = kwargs["end_time"]
        activityList = User.objects.filter(userId=userid)
        if len(activityList) < 1:
            # User not found.
            self.stdout.write("User " + str(userid) + " not found!")
            return
        try:
            for actvty in activityList:
                if startTime is not None:
                    actvty.startTime = startTime
                if endTime is not None:
                    actvty.endTime = endTime
                actvty.save()
        except Exception as ex:
            pass

    def deleteactivity(self, **kwargs):
        userid = kwargs["id"]

        activityList = User.objects.filter(userId=userid)
        if len(activityList) < 1:
            # User not found.
            self.stdout.write("User " + str(userid) + " not found!")
            return
        try:
            for actvty in activityList:
                actvty.delete()

        except Exception as ex:
            pass
