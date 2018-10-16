#!/usr/bin/python3
from subprocess import check_output, Popen, STDOUT

from utils import make_node, make_conf, make_subnets
from cfg import DEPLOY_DELAY, NETWORK_CONF, NODE_CONF, DEPLOY_CMD, SERVICE_LOCK, STATUS_CMD
def lock_deploy(cmd):

    while True:
        try:
            output = check_output(cmd,shell=True, universal_newlines=True, stderr=STDOUT)
            while 'running' in output:
                print('bro running')
                continue

            #print('bro not running')
        except Exception as e:
            error = str(e.output)
            if ("crashed" in error) or ('stopped' in error):
                print(error)
                break
def deploy_bro():
    make_conf(make_subnets(), NETWORK_CONF)
    #make_conf(make_node(), NODE_CONF)
    #lock_deploy(STATUS_CMD)
    Popen(DEPLOY_CMD,shell=True)
    return 
#print(check_output('broctl status',shell=True).decode('utf=8'))
deploy_bro()
