import json



file = open("dragon world.txt", 'r')
txtfile = file.read()
file.close()
output={}
output['order']=[]
output['patterns']={}
curpattern =None
for line in txtfile.split("\n"):
	if("ORDER" in line[:7]): # loading orders
		output['order'].append(line.split(": ")[-1].split(" "))
	if("PATTERN" in line[:7]):
		curpattern = line[8:10]
		output['patterns'][curpattern]=[]
	if("ROW" in line[:3]): #loading patterns
		for channel in line.split(": ")[1:]:
			entry={}
			for i,param in enumerate(channel.split(" ")):

				row = line[4:6]
				if(i==0 and param!="..."): #note
					entry['note']=param
				if(i==1 and param!=".."): #instrument
					entry["instrument"]=param
				if(i==2 and param!="."): #volume
					entry['volume']=param
				if(i>2 and param!="..." and len(param)==3): # effect
					if 'fx' not in entry:
						entry['FX']=[]
					entry['FX'].append(param)
			if entry!={}:
				output['patterns'][curpattern].append([row, entry])


# loading patterns


finaltext = json.dumps(output)
f = open("output.json","w")
f.write(finaltext)
f.close()