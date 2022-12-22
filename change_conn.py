import urllib3.util.connection as urllib3_cn
import socket


def allowed_gai_family():
    """
     https://github.com/shazow/urllib3/blob/master/urllib3/util/connection.py
    """
    family = socket.AF_INET6
    if urllib3_cn.HAS_IPV6:
        family = socket.AF_INET # force ipv4 only if it is available
    return family

urllib3_cn.allowed_gai_family = allowed_gai_family

