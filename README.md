# TCP SYN Flooding Attacks
1. Explanation how the TCP SYN flood attack works.
    - TCP SYN flooding attacks take advantage of the TCP design that requires a 3 way handshake. By continually sending SYN packets, the server will keep sending back SYN ACK packets and waiting around to recieve an ACK. But the ACK will never come because either the sender isnt responding to them, or more likely, the sender has spoofed their IP anyways. This allows a single sender to spoof many different IP addresses, and make it look to the server as if there are many valid requests coming in. The server will use up all channels waiting for the ACKs and if it times out, another one will take its place. Thus the term *"flooding"* because all inputs are flooded with SYN packets.
2. Explanation how SYN cookies work to prevent denial-of-service effect from SYN flood attack.
    - SYN Cookies allow a TCP server not be flooded when TCP SYN flood attacks happen. Normally connections will be dropped when all available inputs are in use during a flood. SYN Cookies allow the server to essentially create the original SYN queue entry when an ACK is recieved because the SYN Cookie has helped encode the necessary information to do so.
3. Follow the lab document to launch TCP SYN flooding attacks by using Scapy.
    - See attached python code or on github.
