from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import decimal

"""
This function compares the current rpf tunnel id count in the system with the low threshold and high threshold and returns the result
"""

def compare_rpf_tunnel_id_cnt(rpf_tunnel_id_cnt, rpf_tunnel_id_max, **kwargs):
        val = 0
        low_thresh = decimal.Decimal(0.8)*rpf_tunnel_id_max
        high_thresh = decimal.Decimal(0.95)*rpf_tunnel_id_max
        if rpf_tunnel_id_cnt <= low_thresh:
            val = 0
        elif rpf_tunnel_id_cnt > low_thresh  and  rpf_tunnel_id_cnt <= high_thresh:
            val = 1
        elif rpf_tunnel_id_cnt > high_thresh:
            val = 2
        return val
