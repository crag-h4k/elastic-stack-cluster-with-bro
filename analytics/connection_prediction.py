from datetime import timedelta
from sys import argv

from bat import bro_log_reader
from colorama import Fore, Style


class connection:
    def __init__(self, orig, dest, ts, prediction = False):
        self.orig = orig
        self.dest = dest
        self.ts = ts
        self.prediction = prediction

def get_connections(reader, cleaned=False):
    conns = []
    for row in reader.readrows():
        orig = row.get('id.orig_h')
        dest = row.get('id.resp_h')
        ts = row.get('ts')
        if cleaned == True: 
            if (orig == '192.168.230.115') and (dest == '192.168.230.135' or dest =='192.168.230.137'):
                continue
            elif (orig == '192.168.230.135' or orig =='192.168.230.137') and (dest == '192.168.230.115'):
                continue
            else:
                conns.append(connection(orig, dest, ts))
        else:
            conns.append(connection(orig, dest, ts))

    return conns

def group_unique(connections):
    unique_orig = []
    grouped = []

    for conn in connections:
        if conn.orig not in unique_orig:
            unique_orig.append(conn.orig)
        else:
            continue
    for i in range(len(unique_orig)):
        sub_group = []
        for conn in connections:
            if conn.orig == unique_orig[i]:
                sub_group.append(conn)
        grouped.append(sub_group)
        
    return grouped

def check_days_ago(string_dt):
    if '-' in string_dt:
        return string_dt.replace('-','') + ' ago'
    else:
        return 'in ' + string_dt

def predict_connection(grouped_connections):   
    
    predicted = []
    
    for conns in grouped_connections:
        try:
            # timedelta calculation found here:
            # https://stackoverflow.com/questions/3617170/average-timedelta-in-list
            timedeltas = [conns[i-1].ts - conns[i].ts for i in range(1, len(conns))]
            avg = sum(timedeltas, timedelta(0)) / len(timedeltas)
            
            origin= conns[0].orig 
            destination = conns[0].dest
            p_time = check_days_ago(str(avg))

            p = connection(origin, destination, p_time, prediction = True)
            predicted.append(p)
            
            print(Style.RESET_ALL + 'expect connection to', Fore.GREEN + origin,
                  Style.RESET_ALL + 'from', Fore.BLUE + destination,
                  Fore.RED +  p_time)
        except:
            continue
    
    return predicted

if __name__ == '__main__':
    
    log_loc = argv[1]
    reader = bro_log_reader.BroLogReader(log_loc)
    ssh_connections = get_connections(reader)

    print(len(ssh_connections), 'ssh connections')
    predict_connection(group_unique(ssh_connections))
