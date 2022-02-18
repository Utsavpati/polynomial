from app.models import pastes
import datetime

def schedule_api():
    paste = pastes.objects.all()
    for p in paste:
        if (datetime.datetime.now() - p.creation_date) > datetime.timedelta(hours=24):
        # if (datetime.datetime.now() - p.creation_date):
            paste.delete()
            print("deleted")
        else:
            pass