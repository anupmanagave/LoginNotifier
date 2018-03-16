import getpass, datetime,smtplib, requests, json,time, socket
from uuid import getnode as get_mac
#Get UserName, Time and Date
uname=getpass.getuser()
dt=datetime.datetime.now()
datetimestr=str(dt)
mydate=datetimestr[:11]
mytime=datetimestr[11:19]

#Get IP and MAC ID
mac = get_mac()
ipadd=socket.gethostbyname(socket.gethostname())
macid=':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))

#Get Geo locatioin Details
send_url = 'http://freegeoip.net/json'
r = requests.get(send_url)
j = json.loads(r.text)
state=j['region_name']
city=j['city']
lat = j['latitude']
lon = j['longitude']
zipc=j['zip_code']
details='\nIP Address: '+str(ipadd)+'\nMAC ID:  '+str(macid)+'\nLocation:'+city+', '+str(zipc)+', '+state+'\nLattitude:('+str(lat)+'), Longitude:('+str(lon)+')'

#Prepare msg
msg='Subject: Alert!! Your PC has been logged in\n\nHello User,\nYour PC has been accessed recently on '+mydate+' at '+mytime+'. Please find the details below:\nUser: '+uname+details;
time.sleep(120)
#Login to Mail and send
conn=smtplib.SMTP('smtp.gmail.com',587)
conn.ehlo()
#Start encryption
conn.starttls()
#give credentials
conn.login('***Gmail login ID goes here','your password goes here')
conn.sendmail('Your gmail','Receiver email ID',msg)
#End Connection
conn.quit()
