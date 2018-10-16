#!/usr/bin/python3
from datetime import datetime

ARP_JSON = './scans/arp_results_' + datetime.now().strftime('%d_%b_%y') + '.json'
ARP_CSV = './scans/arp_results_' + datetime.now().strftime('%d_%b_%y') + '.csv'
ARP_DELAY = 30

DEPLOY_DELAY = 10
DEPLOY_CMD = 'broctl deploy'
STATUS_CMD = 'broctl status'
SERVICE_LOCK = 'ssh'
NETWORK_CONF = '/usr/local/bro/etc/network.cfg'
NODE_CONF = '/usr/local/bro/etc/node.cfg'

