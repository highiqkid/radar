from import_init import *


def get_startup_by_name(name):
    startups = Startup.objects.filter(name=name)
    if startups.count() > 0:
        return startups[0]
    else:
        startups = Startup.objects.filter(name__contains=name)
        if startups.count() > 0:
            return startups[0]
        else:
            return None

f = open('import_data/inc5000.txt', 'r')

i = 0
for line in f:
    data = line.split("\t")
    if len(data) > 3:
        startup = get_startup_by_name(data[1])
        if startup != None:
            startup.num_employees = data[7]
            startup.revenue = data[3]
            startup.growth_percent = int(data[2][:-1].replace(",", ""))
            startup.is_inc5000 = True
            startup.save()
            i += 1
            if i % 10 == 0:
                print i
            
print "Updated %s startups" % i