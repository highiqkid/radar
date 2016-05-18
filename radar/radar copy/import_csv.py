from import_init import *

import csv
import json
import datetime
import time
from django.utils import timezone


def remove_row_spaces(row):
    result = {}
    for key, value in row.iteritems():
        result[sanitize_value(key)] = sanitize_value(value)
    return result
        
def sanitize_value(value):
    value = value.decode('latin-1')
    if len(value) > 1:
        if value[0] == ' ':
            value = value[1:]
        if value[-1] == ' ':
            value = value[0:-1]
    return value

def categories_list(categories):
    categories = categories.split("|")
    if len(categories) > 1:
        if len(categories[0]) < 1:
            del categories[0]
        if len(categories[-1]) < 1:
            del categories[-1]
    return categories

def get_funding(value):
    value = value.replace(",","")
    try:
        return int(value)
    except ValueError:
        return 0
    
def get_datetime(value):
    if len(value) == 10:
        try:
            value = timezone.make_aware(datetime.datetime.strptime(value, "%Y-%m-%d"))
            timestamp = time.mktime(value.timetuple())
            return timestamp
        except Exception:
            return 0
    else:
        return 0
    

def sanitize_row(row):
    row = remove_row_spaces(row)
    row["category_list"] = categories_list(row["category_list"])
    row["funding_total_usd"] = get_funding(row["funding_total_usd"])
    row["founded_at"] = get_datetime(row["founded_at"])
    row["first_funding_at"] = get_datetime(row["first_funding_at"])
    row["last_funding_at"] = get_datetime(row["last_funding_at"])
    
    return row


def save_startup_from_row(row):
    permalink = row["permalink"][14:]
    try:
        result = Startup.objects.get(permalink=permalink)
        #force_update = True
        #print "got result: " + str(result)
    except Exception:
        result = Startup()
        #force_update = False
        #print "error - new"
    result.permalink = permalink
    result.name = row["name"]
    result.website = row["homepage_url"]
    result.status = row["status"]
    result.funding_rounds = row["funding_rounds"]
    result.categories = json.dumps(row["category_list"])
    result.market = row["market"]
    result.city = row["city"]
    result.region = row["region"]
    result.state_code = row["state_code"]
    result.country_code = row["country_code"]
    result.money_raised = row["funding_total_usd"]
    result.last_funding = row["last_funding_at"]
    result.first_funding = row["first_funding_at"]
    if row["founded_at"]:
        result.founded_date = row["founded_at"]
    
    try:
        result.save()
    except Exception:
        pass
    

with open("import_data/startups.csv", 'rU') as csvfile:
    reader = csv.DictReader(csvfile, dialect=csv.excel)
    i = 0
    for row in reader:
        row = sanitize_row(row)
        #print i
        #print row
        #print '\n\n'
        save_startup_from_row(row)
        
        i += 1
        if i % 100 == 0:
            print i