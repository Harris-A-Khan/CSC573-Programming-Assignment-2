# Programming Assignment 2
# Author: Robert English, Harris Khan, Jackson Skyes, Madeline Wise
# Date: November 28th, 2023
# Description: This is a packet sniffing program that will sniff packets and count the number of packets in a specific protocol (IP, TCP, UDP, and DNS)

# Importing the necessary libraries
from socket import socket, AF_PACKET, SOCK_RAW, htons

# GLOBAL VARS
ALL_PROTOCOLS = 0x0003

# Create a low-level socket that listens to all packets on the machine
rawSocket = socket(AF_PACKET, SOCK_RAW)


def main(): 
    print("Starting packet sniffer...")

if __name__ == "__main__":
    main()