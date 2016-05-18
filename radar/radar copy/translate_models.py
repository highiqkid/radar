from radar.wsgi import *

from radar_access.models import Startup, StartupRaw

import time
from datetime import datetime

raw_startups = StartupRaw.objects.all()

length = raw_startups.count()
i = 1
for r in raw_startups:
    permalink = r.permalink[:100]
    try:
        n = Startup.objects.get(permalink=permalink)
    except Exception as e:
        n = Startup()
    n.permalink = permalink
    n.last_updated = time.time()
    n.is_prefiltered = True
    n.is_my_company = False
    n.name = r.name[:200]
    n.website = r.homepage_url[:300]
    n.status = r.status
    n.categories = r.category_list[:300]
    n.market = r.market[:50]
    n.funding_rounds = 0
    n.city = r.city[:50]
    n.region = r.region[:50]
    n.state_code = ""#None
    n.country_code = r.country[:6]
    n.money_raised = r.funding
    n.last_funding = 0#None
    n.first_funding = 0#None
    try:
        n.founded_date = time.mktime(
            datetime.strptime(r.founded_date, "%Y-%m-%d").timetuple()
        )
    except Exception as e:
        n.founded_date = 0
    n.logo = r.image_url[:300]
    n.short_description = ""#None
    n.description = r.description[:1500]
    n.twitter_url = r.twitter_url[:200]
    n.facebook_url = r.facebook_url[:200]
    n.linkedin_url = r.linkedin_url[:200]
    n.num_employees_min = 0#None
    n.num_employees_max = 0#None
    n.team = r.founders[:300]
    n.investors = ""#None
    n.press_mentions = ""#None
    n.competitors = r.competitors[:300]
    n.num_employees = 0#None
    n.revenue = 0#None
    n.growth_percent = 0#None
    n.is_inc5000 = False
    n.cbase_uuid = r.cbase_uuid[:33]
    n.angellist_id = r.angellist_id
    n.angellist_url = r.angellist_url[:300]
    n.angellist_name = r.angellist_name[:100]
    n.save()
    
    if i % 100 == 0:
        print "Translated %s out of %s startup models." % (i, length)
    i += 1