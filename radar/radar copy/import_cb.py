from import_init import *

import grequests
import time
import json
import urllib

#https://api.crunchbase.com/v/3/organizations/wetpaint/investors?user_key=bb9bdd625fbb708759f70c49b38dbfa8
USER_KEY = "bb9bdd625fbb708759f70c49b38dbfa8"

def save_startup_from_data(startup, result):
    if not result.get("data") or not result["data"].get("properties") or not result["data"].get("relationships"):
        return
    result = result["data"]
    props = result["properties"]
    if result["relationships"].get("primary_image"):
        startup.logo = result["relationships"]["primary_image"]["item"]["properties"]["asset_url"]
    #print "logo: " + startup.logo
    if props["short_description"]:
        startup.short_description = props["short_description"]
    if props["description"]:
        startup.description = props["description"]
    #print "desc: " + startup.description
    
    if result["relationships"].get("websites"):
        for item in result["relationships"]["websites"]["items"]:
            site = item["properties"]["website"]
            url = item["properties"]["url"]
            #print "site: " + site, "url: " + url
            if site == "twitter" and url:
                startup.twitter_url = url
            elif site == "facebook" and url:
                startup.facebook_url = url
            elif site == "linkedin" and url:
                startup.linkedin_url = url

    if result["relationships"].get("current_team"):
        team = []
        for item in result["relationships"]["current_team"]["items"]:
            name = item["relationships"]["person"]["properties"]
            name = name["first_name"] + " " + name["last_name"]
            team.append(name)
        startup.team = ', '.join(team)

    if result["relationships"].get("investors"):
        investors = []
        for item in result["relationships"]["investors"]["items"]:
            name = item["properties"]
            if name.get("name"):
                name = name["name"]
            else:
                name = name["first_name"] + " " + name["last_name"]
            investors.append(name)
        startup.investors = ', '.join(investors)
        
    if type(props["num_employees_min"]) is int and type(props["num_employees_max"]) is int:
        startup.num_employees_min = props["num_employees_min"]
        startup.num_employees_max = props["num_employees_max"]
    #print "emp min: " + str(startup.num_employees_min)
    startup.last_updated = time.time()
    try:
        startup.save()
    except Exception:
        pass
    
def get_cb_url(permalink):
    return "https://api.crunchbase.com/v/3/organizations/" + permalink + "?user_key=" + USER_KEY

def get_startups_remaining():
    timestamp = time.time() - (30 * 86400)
    startups = Startup.objects.filter(last_updated__lt=timestamp)
    return startups.count()

def update_startups(num, max_concurrent):
    timestamp = time.time() - (30 * 86400)
    startups = Startup.objects.filter(last_updated__lt=timestamp)
    
    urls = []
    for i in range(0, min(num, len(startups))):
        urls.append(get_cb_url(startups[i].permalink))
    if len(urls) > 0:
        rs = [grequests.get(u) for u in urls]
        results = grequests.map(rs, size=max_concurrent)
        i = 0
        for result in results:
            startup = startups[i]
            try:
                result = json.loads(result.content)
                if result.get("data"):
                    save_startup_from_data(startup, result)
            except Exception:
                pass
            startup.last_updated = time.time()
            try:
                startup.save()
            except Exception:
                pass
            i += 1
        return True
    else:
        return False
    
    
print "Downloading info for " + str(get_startups_remaining()) + " startups..."
i = 1
while True:
    if not update_startups(150, 50):
        break
    print i, "Updated %s" % (i * 150), get_startups_remaining(), "left"
    i += 1