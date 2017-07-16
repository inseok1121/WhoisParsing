import pythonwhois
import json


def print_domain(url):
        data = pythonwhois.get_whois(url)
	print data
	print type(data)        
	json_val = json.dumps(data, ensure_ascii=False)
	
	f=open("data.json", "w")
	f.write(data)
	f.close()

f = open("doamin", "r")
line = f.readline()

print_domain(line)

f.close()


'''
import pdb
pdb.set_trace()
'''
