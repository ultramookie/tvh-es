#!/usr/bin/env python

import json
from elasticsearch import Elasticsearch
import sys, getopt
import datetime
from dateutil.tz import tzlocal

index = "tvh"
doc_type = "tvh"
elastichost='localhost:9200'

def main(argv):
    data = {}

    id = datetime.datetime.now(tzlocal())
    data['timestamp'] = id

    try:
        opts, args = getopt.getopt(argv,"hf:c:t:s:p:d:e:S:E:r:R:i:")
    except getopt.GetoptError:
        print 'tvh-es.py -f "%f" -c "%c" -t "%t" -s "%s" -p "%p" -d "%d" -e "%e" -S "%S" -E "%E" -r "%r" -R "%R" -i "%i"'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'tvh-es.py -f "%f" -c "%c" -t "%t" -s "%s" -p "%p" -d "%d" -e "%e" -S "%S" -E "%E" -r "%r" -R "%R" -i "%i"'
            sys.exit()
        elif opt in ("-f"):
            data['fullpath'] = arg
        elif opt in ("-c"):
	        data['channel'] = arg
        elif opt in ("-t"):
            data['title'] = arg
        elif opt in ("-s"):
	        data['subtitle'] = arg
        elif opt in ("-p"):
	        data['episode'] = arg
        elif opt in ("-d"):
            data['description'] = arg
        elif opt in ("-e"):
	        data['errormsg'] = arg
        elif opt in ("-S"):
            data['start'] = arg
        elif opt in ("-E"):
	        data['end'] = arg
        elif opt in ("-r"):
	        data['numerrors'] = arg
        elif opt in ("-R"):
	        data['numdataerrors'] = arg
        elif opt in ("-i"):
	        data['streams'] = arg

    if int(data['start']) > 0 and int(data['end']) > 0:
        data['runtime'] = (int(data['end']) - int(data['start'])) / 60

    es = Elasticsearch(elastichost)

    es.index(index=index,doc_type=doc_type,id=id,body=data) 

if __name__ == "__main__":
    main(sys.argv[1:])