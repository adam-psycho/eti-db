import pytz
import datetime
import albatross
from django.http import HttpResponse
from etidb import models;

etiConn = albatross.Connection(username="podrick", password="luelinks")

def query_users(request):
    literally_all_users = etiConn.users().search(recurse=True)
    eti_users = [];
    for user in literally_all_users:
        eti_user = models.EtiUser(id=user.id, name=user.name)
        print ('{}: {}'.format(user.id, user.name))
        eti_users.append(eti_user)

    models.EtiUser.objects.bulk_create(eti_users)

    return HttpResponse();


def query_topics(request):
    # November 1st 2018, set to Eastern timezone
    tz = pytz.timezone('US/Pacific')
    activeSince = datetime.datetime.strptime(
        request.GET.get('start_time'), '%Y-%m-%d').replace(tzinfo=tz)
    maxTime = datetime.datetime.strptime(
        request.GET.get('end_time'), '%Y-%m-%d').replace(tzinfo=tz)

    topics = etiConn.topics(allowedTags=["LUE"], forbiddenTags=["Anonymous"]).search(
        activeSince=activeSince, maxTime=maxTime, recurse=True)

    eti_topics = []
    created = 0
    updated = 0
    for topic in topics:
        t = models.EtiTopic.objects.filter(id=topic.id)
        if (len(t)):
            updated += 1
            t.update(
                id=topic.id,
                title=topic.title,
                closed=topic.closed,
                post_count=topic.postCount,
                eti_user=models.EtiUser(topic.user.id),
                created=topic.lastPostTime)
        else:
            created += 1
            models.EtiTopic.objects.create(
                id=topic.id,
                title=topic.title,
                closed=topic.closed,
                post_count=topic.postCount,
                eti_user=models.EtiUser(topic.user.id),
                created=topic.lastPostTime)



    return HttpResponse("Created: {}\nUpdate: {}".format(created, updated))
