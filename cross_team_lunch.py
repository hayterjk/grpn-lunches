import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import csv
import sys

f = open(sys.argv[1], 'rt')
schedule = [];
week = sys.argv[2]
try:
  reader = csv.reader(f)
  for row in reader:
    schedule.append(row)
finally:
  f.close()

team_hash = {}
team_hash['Performance'] = 'performance@groupon.com'
team_hash['App Ops Support'] = 'appops-support@groupon.com'
team_hash['FED'] = 'fed@groupon.com'
team_hash['EDW'] = 'edw-chicago@groupon.com'
team_hash['App Ops Dev'] = 'appops-dev@groupon.com'
team_hash['Supply Intel'] = 'supply-intelligence@groupon.com'
team_hash['Deal Estate'] = 'dealestate-dev@groupon.com'
team_hash['User Sessions'] = 'vsood@groupon.com' #team email?
team_hash['Bemod'] = 'bemod@groupon.com'
team_hash['Ion'] = 'ion@groupon.com'
team_hash['Salesforce'] = 'sfdc-chicago-team@groupon.com'
team_hash['Connection'] = 'connection-eng@groupon.com'
team_hash['Goods CIM GDP'] = 'gbuenzli@groupon.com' #team email?
team_hash['RAPT'] = 'rapt@groupon.com'
team_hash['Deal Platform'] = 'deal-platform@groupon.com'
team_hash['Optimize'] = 'optimize@groupon.com'
team_hash['Local Third Party Feed'] = 'local-third-party-feed@groupon.com'
team_hash['Coupons'] = 'coupons-eng@groupon.com'
team_hash['Flux'] = 'flux-engineering@groupon.com'
team_hash['Users'] = 'users-team@groupon.com'
team_hash['Tronicon'] = 'tronicon@groupon.com'
team_hash['Funnel'] = 'funnel-dev@groupon.com'

def send_emails(team_hash, team1, team2):
	fromaddr = "" #insert email here
	toaddr = team_hash[team1]
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Cross Team Lunch"
	 
	body = "Hey " + team1 + "! You've been matched with " + team2 + "! (" + team_hash[team2] + ") Please reach out and try to schedule a lunch within the next two weeks."
	msg.attach(MIMEText(body, 'plain'))
	 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "") #insert password here
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
	return;

for x in schedule:
	if x[0] == week:
		send_emails(team_hash, x[1], x[2])
		send_emails(team_hash, x[2], x[1])
