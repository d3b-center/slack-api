import sys
import json
from datetime import datetime

dict = {}

with open(sys.argv[1]) as data_file:
    data = json.load(data_file)

for each_msg in data:
    date = datetime.fromtimestamp(float(each_msg['ts'])).strftime('%Y-%m-%d')
    try:
        dict[date]
    except KeyError:
        dict[date] = []
    dict[date].append(each_msg)

for each_date in dict:
    json_text = json.dumps(dict[each_date], indent=4)
    f = open(each_date + '.json', 'w')
    f.write(json_text)
    f.close()
