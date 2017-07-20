'''
 @uthor ="ARCHIT AGRAWAL"
 written on=6-4-2017"
 A SIMPLE SCRIPT TO SHOW DESKTOP NOTIFICATION OF LIVE CRICKET MATCH'''
while True:
    from pycricbuzz import Cricbuzz
    import json
    import time
    import datetime as dt
    c = Cricbuzz()
    matches = c.matches()
    for match in matches:
    	if(match['mchstate'] != "nextlive"):
    	    s= c.livescore(match['id'])
            scor=s['batting']['score']
            b1= s['batting']['batsman'][0]['name']
            r1=s['batting']['batsman'][0]['runs']
            b2=s['batting']['batsman'][1]['name']
            r2=s['batting']['batsman'][1]['runs']
            team=s['batting']['team']
            output= team + " " + scor[0]['runs'] +"-"+ scor[0]['wickets']+"("+scor[0]['overs']+")"+"\n"+ b1 +" "+ r1 + "\n" +b2 +" "+ r2
            #print b2 +" "+ r2
            break
            
            #print scor[0]['runs'] +"-"+ scor[0]['wickets']
    
    import time 
    import notify2
    ipath="home/Desktop"
    notify2.init("LIVE SCORE")
    n = notify2.Notification("Cricket",output, icon = ipath)
    n.show()
    time.sleep(150)    

        
        #print(match['score'])