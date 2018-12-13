#!/usr/bin/env python3

from subprocess import check_output
from time import sleep
from datetime import datetime

import smtplib

from auth import TO, FROM, PASSWORD


def send_email(alert):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(FROM,PASSWORD)
    BODY = '\r\n'.join(['To: %s' % TO,
            'From: %s' % FROM,
            'Subject: %s' % alert,
            '', alert])
    try:
        server.sendmail(FROM, [TO], BODY,)
    except Exception as e:
        print(e)
        return

def ping_host(host):
    try:
        cmd = 'ping -c 1 ' + host
        result = check_output(cmd, shell = True)
        if '0% packet loss' in result.decode('utf-8'):
            return False
        else:
            alert = str(datetime.now()) + ' ' + host + ' is probably down'
            return alert
    except:
        alert = str(datetime.now()) + ' ' + host + ' is probably down'
        return alert

if __name__ == '__main__':
    #alert = 'this is a test'
    #send_email(alert)
    hosts = ['de-elastic', 'de-lg', 'de-backup']

    while True:
        for host in hosts:
            alert = ping_host(host)
        
            if alert == False:
                continue
        
            else:
                send_email(alert)
        
        sleep(180)
