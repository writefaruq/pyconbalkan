from django.db.models import Q
from django.shortcuts import render

from pyconbalkan.conference.models import CountDown, MissionStatement
from pyconbalkan.speaker.models import Speaker
from pyconbalkan.sponsors.models import Sponsor, SponsorshipLevel


def home(request):
    count_down = CountDown.objects.filter(active=True)
    keynotes = Speaker.objects.filter(active=True, conference__active=True, keynote=True).order_by("full_name")

    keystone_sponsors = Sponsor.objects.filter(level=SponsorshipLevel.keystone)
    platinum_sponsors = Sponsor.objects.filter(level=SponsorshipLevel.platinum)
    gold_sponsors = Sponsor.objects.filter(level=SponsorshipLevel.gold)
    silver_sponsors = Sponsor.objects.filter(level=SponsorshipLevel.silver)
    partners = Sponsor.objects.filter(level=SponsorshipLevel.partner)
    sidebar_sponsors = Sponsor.objects.filter(sidebar=True)

    mission_statement = MissionStatement.objects.filter(active=True)

    context = {
        "keynotes": keynotes,
        "keystone_sponsors": keystone_sponsors,
        "platinum_sponsors": platinum_sponsors,
        "gold_sponsors": gold_sponsors,
        "silver_sponsors": silver_sponsors,
        "partners": partners,
        "sidebar_sponsors": sidebar_sponsors,
        "count_down": count_down.first() if count_down else None,
        "mission_statement": mission_statement.first() if mission_statement else None,
        "meta": request.conference.as_meta(),
    }
    return render(request, "home.html", context)
