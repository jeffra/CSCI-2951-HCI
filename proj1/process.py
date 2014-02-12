import sys, re, string
from collections import defaultdict
nameIdx = 32-5

# Taken from: http://stackoverflow.com/questions/7160737/python-how-to-validate-a-url-in-python-malformed-or-not
urlRegex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

fd = open(sys.argv[1])
lines = fd.readlines()
lines = map(lambda t: t.split('","'), lines)
schoolNamesFile = sys.argv[2]
schoolNames = open(schoolNamesFile).readlines()[1:]
#schoolNames = ["Duke University"]

fd = open('data.csv', 'w')
fd.write('professor, university, urls\n')
for schoolName in schoolNames:
    schoolName = schoolName.strip()
    print schoolName, 
    schoolData = filter(lambda t: schoolName in t[nameIdx], lines)
    print len(schoolData)

    data = defaultdict(set)
    for hit in schoolData:
        i = nameIdx+1
        while True:
            name = string.lower(hit[i]).rstrip('"').lstrip('"')
            if "," in name:
                parts = name.split(",", 1)
                name = parts[1] + " " + parts[0]
                name = name.strip()
            url = hit[i+1].strip().replace("https","http").rstrip('"').lstrip('"').rstrip("/")
            m = re.match(urlRegex, url)
            if 'brown' in url and 'browne' not in url:
                print "brown?!", name, url
            elif m is not None:
                data[name].add(url)
            elif '' != url:
                print hit[i], "Not a url:", hit[i+1] 
            i += 2
            if (i+1) >= len(hit):
                break
    names = data.keys()
    names.sort()

    for name in names:
        urls = map(lambda t: "<a href='%s'>%s</a>" % (t,t), data[name])
        urls = " or ".join(urls)
        fd.write('"%s", "%s", %s\n' % (name, schoolName, urls))
        #print name, ",", schoolName, ",", " ".join(data[name])
