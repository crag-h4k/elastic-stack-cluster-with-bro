class Host(hostname, ip_addr, roles, config_paths):
    __init__(self):
        self.hostname = hostname
        self.ip_addr = ip_addr
        self.roles = roles
        self.config_paths = config_paths

de_backup = Host(hostname = 'de_backup',
    ip_addr = '192.168.230.115',
    roles = [ 'prometheus backup',
        'bro_manager',
        'bro_logger',
        'filebeat export'],
    conf = ''
    )
de_es = Host(hostname = 'de_es',
    ip_addr = '192.168.230.135',
    roles = [ 'elasticsearch indexer',
        'bro_worker1', 
        'filebeat export'],
    conf = ''
    )
de_lg = Host(hostname = 'de_lg',
    ip_addr = '192.168.230.137',
    roles = [ 
        'logstash parser',
        'kibana host',
        'bro worker2', 
        'filebeat export'],
    confs = ''
    )
bro_roles = ['logger', 'manager', 'proxy', 'worker-x']
