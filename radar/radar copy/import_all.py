from import_init import *

import tablib
from import_export import resources
from radar_access.models import Startup

startup_resource = resources.modelresource_factory(model=Startup)()

f = open("startups_all.csv")
csv = ""
for line in f:
    csv += line
dataset = tablib.Dataset()
dataset.csv = csv

result = startup_resource.import_data(dataset, dry_run=False)