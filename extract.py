import json

with open('/Users/tianayang/Desktop/audio-files/content.json','r') as f:
	data = json.load(f)
	data1 = data['results'][0]
        z = data1['alternatives']
        j = z[0]['transcript']
	print(j)
        f.close
