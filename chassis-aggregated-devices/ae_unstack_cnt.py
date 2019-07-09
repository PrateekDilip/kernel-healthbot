import re

def run():
    dev = __proxy__['junos.conn']()
    op1 = dev.rpc.request_shell_execute(command="sysctl net.lag_health_params | grep 'AE Unstacking error count'")
    obj = re.search('\d+', op1.text)
    obj1 = int(obj.group())
    return ({'fields': {"ae_unstack_cnt": obj1}})
