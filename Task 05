from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(packet):
    """Callback function to process each captured packet."""
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto
        
        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
        
        if packet.haslayer(TCP):
            print(f"Protocol: TCP")
            print(f"Payload (TCP): {packet[TCP].payload}")
        elif packet.haslayer(UDP):
            print(f"Protocol: UDP")
            print(f"Payload (UDP): {packet[UDP].payload}")
        elif packet.haslayer(Raw):
            print(f"Protocol: Raw")
            print(f"Payload (Raw): {packet[Raw].load}")
        else:
            print(f"Protocol: {proto}")
        
        print("-" * 50)

def main():
    print("Starting Packet Sniffer...")
    # Capture packets and call packet_callback for each
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
