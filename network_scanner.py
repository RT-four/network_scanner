

import scapy.all as scapy #bibl dla scana setey

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)#sozdaem arp paket peredaem nash deapazon ip
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")#sozdaem shirokoveshatelny adres
    arp_request_broadcast = broadcast/arp_request#obyedinaem pokety
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False )[0]#funkcia dla otpravei poeta [0] vozvrashaem tolko pervy spisok
#spryatali lishuu infu
    print("")
    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for element in answered_list:
        print(element[1].psrc + "\t\t" +  element[1].hwsrc)#vivodim v pervom elemente info
    print("")

scan("192.168.1.1/24")#ishem takoy ip
input('Press ENTER to exit')