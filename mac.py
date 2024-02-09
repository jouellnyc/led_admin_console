import binascii

def get_peer_mac(mac_addr):
    mac_address_string = mac_addr.replace(":", "").upper()
    mac_address_bytes = binascii.unhexlify(mac_address_string)
    return mac_address_bytes

def get_my_mac():
    import network
    import ubinascii
    mymac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
    return(mymac)

if __name__ == "mac":
    print(get_my_mac())



