import json
with open('ptt_0726_s.json','r',encoding='utf-8-sig') as f:
    article = json.load(f)
    #print(json.dumps(detail,ensure_ascii=False,indent=4))
#print(type(detail))

list_ptt = []
for i in range(len(article)):
	if "all" in article[i]["h_推文總數"].keys():
			list_ptt.append(article[i])

ptt=sorted(list_ptt, key=lambda k: k["h_推文總數"]["all"],reverse=True)
print(json.dumps(ptt,ensure_ascii=False,indent=4))

with open('ptt_0726.txt', 'w+', encoding='utf-8-sig') as g:
    for i in range(len(ptt)):
        a=[ptt[i]]
        b=str(a)
        g.write(b+'\n')
