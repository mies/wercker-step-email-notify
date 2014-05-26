import smtplib
import sys

arglen = len(sys.argv)

if arglen < 8 :
  print 'There should be at least 8 arguments'
  sys.exit(1)

fromaddr = str(sys.argv[1])
toaddrs = str(sys.argv[2])
subject  = str(sys.argv[3])
body  = str(sys.argv[4])
username  = str(sys.argv[5])
password  = str(sys.argv[6])
host  = str(sys.argv[7])

ssl = False
if arglen >= 9 :
  ssl = sys.argv[8] in [ 'true', '1', 't', 'y', 'yes']

msg = "Subject: " + subject + "\nFrom:" + fromaddr + "\nTo: " + toaddrs + "\n\n" + body

if ssl == True :
  server = smtplib.SMTP_SSL(host)
else :
  server = smtplib.SMTP(host)
  server.starttls()

server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

