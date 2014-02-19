import time

fd = open('prof_meta_data_raw.csv')

header = fd.readline()
header = header.split('","')

stime = header.index("SubmitTime")

lines = map(lambda t: t[stime], map(lambda i: i.strip().split('","'), fd.readlines()))

# Fri Feb 14 05:48:03 GMT 2014
tses = []
for d in lines:
    ts = time.strptime(d, "%a %b %d %H:%M:%S %Z %Y")
    ts = time.mktime(ts) #epoch seconds
    tses.append(ts)

m = min(tses)
tses.sort()
for d in tses:
    print (d-m) / 60 / 60 #hours
