import re

def run():
    dev = __proxy__['junos.conn']()
    op1 = dev.rpc.request_shell_execute(command="sysctl net.lag_health_params | grep 'AE LP Backup link down count'")
    obj = re.search('\d+', op1.text)
    obj1 = int(obj.group())
    return ({'fields': {"ae_lp_link_down_cnt": obj1}})
