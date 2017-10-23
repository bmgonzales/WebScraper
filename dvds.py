import requests

response = requests.get('https://www.moviefone.com/dvd/')

import bs4
soup = bs4.BeautifulSoup(response.text, "html.parser")
titles = soup.find_all('a', attrs={'class': 'movie-title'})

dvds = []

for a in titles:
	a = a.text
	dvds.append(a)

dvds = '\n'.join(dvds)

import smtplib
user = 'sending_email'
pwd = 'email_pwd'
FROM = 'sending_email'
TO = ['my_email']
SUBJECT = 'New DVD Releases'
TEXT = dvds

message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
try:
    server = smtplib.SMTP("SMTP.GMAIL.COM", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(user, pwd)
    server.sendmail(FROM, TO, message)
    server.close()
    print ('successfully sent the mail')
except smtplib.SMTPException:
    print ('failed to send mail')