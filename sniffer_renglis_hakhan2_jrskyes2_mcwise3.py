# Programming Assignment 2
# Author: Robert English (renglis), Harris Khan (hakhan2), Jackson Skyes (jrskyes2), Madeline Wise (mcwise3)
# Date: November 28th, 2023
# Description: This is a packet sniffing program that will sniff packets and count the number of packets in a specific protocol (IP, TCP, UDP, and DNS)

from scapy.all import sniff, IP, TCP, UDP, DNS

def process_packet(packet):
    # Increment protocol counters based on packet type
    if IP in packet:
        protocol_counts['IP'] += 1
    if TCP in packet:
        protocol_counts['TCP'] += 1
    if UDP in packet:
        protocol_counts['UDP'] += 1
    if DNS in packet:
        protocol_counts['DNS'] += 1

def main(): 
    print("Starting sniffer...")
    
    # Initialize protocol counts dictionary
    global protocol_counts
    protocol_counts = {'IP': 0, 'TCP': 0, 'UDP': 0, 'DNS': 0}

    # Run sniff for a specific duration
    duration = 30  # Duration in seconds
    sniff(timeout=duration, prn=process_packet)
    
    # Let the user know we're finished sniffing 
    print("Finished sniffing.")

    print("Protocol counts:")
    for protocol, count in protocol_counts.items():
        print(f"{protocol}: {count}")

    # TODO: properly name the files with everyones unity ID
    print("Writing to file...")
    with open('sniffer_renglis_hakhan2_jrskyes2_mcwise3.csv', 'w') as file: 
        file.write("protocol,count\n")
        for protocol, count in protocol_counts.items():
            file.write(f"{protocol.lower()},{count}\n")


    print("Done.")

if __name__ == "__main__":
    main()
