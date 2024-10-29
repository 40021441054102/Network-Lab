# Network-Lab
Network Lab Project, Papers and Other Stuff

# Last Exercise of Network Lab [here](https://github.com/40021441054102/Network-Lab/blob/main/Exercises/ex03/README.md)
<div align="center">
  <img src="https://github.com/40021441054102/Network-Lab/blob/main/Exercises/ex03/network.png" width="52%"/>
</div>

### GUI Interface
For a 4-router network connected in a square topology, where each router has a switch with a single PC connected, We must configure the IP addresses for each router, interface, and PC using GUI interface of ```Packet Tracer```.
<!-- $$\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$ -->

## Network Diagram
First must design topology like :
* $$Router_1$$ connects to $$Router_2$$ and $$Router_4$$.
* $$Router_2$$ connects to $$Router_1$$ and $$Router_3$$.
* $$Router_3$$ connects to $$Router_2$$ and $$Router_4$$.
* $$Router_4$$ connects to $$Router_1$$ and $$Router_3$$.

Each router has a local network connected via a switch with one PC attached.

## Router Serial Connections (Point-to-Point Links) IP Address Configuration
We can use both ```/30``` and ```/24``` subnet masks for each serial link to optimize IP address usage on point-to-point links, but i used /30 subnet masks because it is ```common for router p2p links```.

### What is a Subnet Mask?
A subnet mask is a ```32-bit``` number that separates the network part of an IP address from the host part. By dividing an IP address, the subnet mask defines the size of each subnet and the number of ```usable IP addresses``` within each subnet.
For example, Subnet Mask of ```/30 (255.255.255.252)``` uses the first 30 bits for the network portion, leaving only 2 bits for host addresses.
The result is very small subnets with only 4 IP addresses each :

### How a ```/30``` Subnet Reserves IPs
A ```/30``` subnet provides 4 IP addresses ```per subnet```, but only ```2 of these IPs are usable```. Here’s why:
1. ```Network Address``` : The first IP in any subnet is reserved as the network address (e.g., 192.168.1.0 in 192.168.1.0/30). This address identifies the subnet itself and is not assignable to devices.
2. ```Usable IP Addresses``` : The next two IPs can be assigned to devices (e.g., 192.168.1.1 and 192.168.1.2 in the 192.168.1.0/30 subnet).
3. ```Broadcast Address``` : The last IP in the range is reserved as the broadcast address (e.g., 192.168.1.3 in 192.168.1.0/30). This address is used to send data to all hosts on the subnet and is also not assignable to devices.

So for topology we need 4 subnets for each router like :
* Subnet 1 : 192.168.1.0/30 (0 to 3)
  * ```Network``` $${\color{orange}192.168.1.0/30}$$
  * ```Usable``` $${\color{lime}192.168.1.2/30}$$, $${\color{lime}192.168.1.3/30}$$
  * ```Broadcast``` $${\color{orange}192.168.1.3/30}$$
* Subnet 2 : 192.168.1.4/30 (4 to 7)
  * ```Network``` $${\color{orange}192.168.1.4/30}$$
  * ```Usable``` $${\color{lime}192.168.1.5/30}$$, $${\color{lime}192.168.1.6/30}$$
  * ```Broadcast``` $${\color{orange}192.168.1.7/30}$$
* Subnet 3 : 192.168.1.0/30 (8 to 11)
  * ```Network``` $${\color{orange}192.168.1.8/30}$$
  * ```Usable``` $${\color{lime}192.168.1.9/30}$$, $${\color{lime}192.168.1.10/30}$$
  * ```Broadcast``` $${\color{orange}192.168.1.11/30}$$
* Subnet 4 : 192.168.1.0/30 (12 to 15)
  * ```Network``` $${\color{orange}192.168.1.12/30}$$
  * ```Usable``` $${\color{lime}192.168.1.13/30}$$, $${\color{lime}192.168.1.14/30}$$
  * ```Broadcast``` $${\color{orange}192.168.1.15/30}$$

### for configuration we use 2 usable IPs for each router's serial port
* Link between $$Router_1$$ and $$Router_2$$:
  * $$Router_1$$ Serial 0/0: ```192.168.1.1``` ```255.255.255.252```
  * $$Router_2$$ Serial 0/0: ```192.168.1.2``` ```255.255.255.252```
* Link between $$Router_2$$ and $$Router_3$$:
  * $$Router_2$$ Serial 0/1: ```192.168.1.5``` ```255.255.255.252```
  * $$Router_3$$ Serial 0/0: ```192.168.1.6``` ```255.255.255.252```
* Link between Router3 and Router4:
  * $$Router_3$$ Serial 0/1: ```192.168.1.9``` ```255.255.255.252```
  * $$Router_4$$ Serial 0/0: ```192.168.1.10``` ```255.255.255.252```
* Link between Router4 and Router1:
  * $$Router_4$$ Serial 0/1: ```192.168.1.13``` ```255.255.255.252```
  * $$Router_1$$ Serial 0/1: ```192.168.1.14``` ```255.255.255.252```

⚠️ ```Clock Rate``` for both side of serial cable must be same (64000 is Common)

### Router 1 Configurations
<div align="center">
  <img src="https://github.com/40021441054102/Network-Lab/blob/main/Exercises/ex03/router1_serial_0.png" width="41%"/>
  <img src="https://github.com/40021441054102/Network-Lab/blob/main/Exercises/ex03/router1_serial_1.png" width="41%"/>
</div>

### Router 2 Configurations
<div align="center">
  <img src="https://github.com/40021441054102/Network-Lab/blob/main/Exercises/ex03/router2_serial_0.png" width="41%"/>
  <img src="https://github.com/40021441054102/Network-Lab/blob/main/Exercises/ex03/router2_serial_1.png" width="41%"/>
</div>

### Router 3 Configurations
<div align="center">
  <img src="https://github.com/40021441054102/Network-Lab/blob/main/Exercises/ex03/router3_serial_0.png" width="41%"/>
  <img src="https://github.com/40021441054102/Network-Lab/blob/main/Exercises/ex03/router3_serial_1.png" width="41%"/>
</div>

### Router 4 Configurations
<div align="center">
  <img src="https://github.com/40021441054102/Network-Lab/blob/main/Exercises/ex03/router4_serial_0.png" width="41%"/>
  <img src="https://github.com/40021441054102/Network-Lab/blob/main/Exercises/ex03/router4_serial_1.png" width="41%"/>
</div>

## Router Ethernet Interfaces (Ethernet Configurations for PCs and Router's GigabitEthernet Ports)
We use ```/24``` subnet masks for each router’s local network :

* $$Router_1$$ Ethernet Interface (connected to $$PC_1$$ via a switch) :
  * $$Router_1$$ GigabitEthernet0/0 : ```192.168.2.1``` and ```255.255.255.0```
  * $$PC_1$$ IP : ```192.168.2.100``` and ```255.255.255.0```, Default Gateway of ```192.168.2.1```
<div align="center">
  <img src="https://github.com/40021441054102/Network-Lab/blob/main/Exercises/ex03/pc1_config.png" width="41%"/>
  <img src="https://github.com/40021441054102/Network-Lab/blob/main/Exercises/ex03/router1_gigabitEthernet.png" width="41%"/>
</div>

* $$Router_2$$ Ethernet Interface (connected to $$PC_2$$ via a switch):
  * $$Router_2$$ GigabitEthernet0/0 : ```192.168.3.1``` and ```255.255.255.0```
  * $$PC_2$$ IP : ```192.168.3.100``` and ```255.255.255.0```, Default Gateway of ```192.168.3.1```
<div align="center">
  <img src="https://github.com/40021441054102/Network-Lab/blob/main/Exercises/ex03/pc2_config.png" width="41%"/>
  <img src="https://github.com/40021441054102/Network-Lab/blob/main/Exercises/ex03/router2_gigabitEthernet.png" width="41%"/>
</div>

* $$Router_3$$ Ethernet Interface (connected to $$PC_3$$ via a switch):
  * $$Router_3$$ GigabitEthernet0/0 : ```192.168.4.1``` and ```255.255.255.0```
  * $$PC_3$$ IP : ```192.168.4.100``` and ```255.255.255.0```, Default Gateway of ```192.168.4.1```
<div align="center">
  <img src="https://github.com/40021441054102/Network-Lab/blob/main/Exercises/ex03/pc3_config.png" width="41%"/>
  <img src="https://github.com/40021441054102/Network-Lab/blob/main/Exercises/ex03/router3_gigabitEthernet.png" width="41%"/>
</div>

* $$Router_4$$ Ethernet Interface (connected to $$PC_4$$ via a switch):
  * $$Router_4$$ GigabitEthernet0/0 : ```192.168.5.1``` and ```255.255.255.0```
  * $$PC_4$$ IP : ```192.168.5.100``` and ```255.255.255.0```, Default Gateway of ```192.168.5.1```
<div align="center">
  <img src="https://github.com/40021441054102/Network-Lab/blob/main/Exercises/ex03/pc4_config.png" width="41%"/>
  <img src="https://github.com/40021441054102/Network-Lab/blob/main/Exercises/ex03/router4_gigabitEthernet.png" width="41%"/>
</div>

⚠️ Now if you ping another PC you will see ```unreachable``` error, you must config static routes for each routers to transfer data between them.

## Configuring Static Routes for Each Router
Each router needs static routes to reach the networks connected to the other routers :

* $$Router_1$$ ```Network Subnet Mast 192.168.2.0``` CLI commands :
  
  * ```bash
    Router1(config)# ip route 192.168.3.0 255.255.255.0 192.168.1.2   // Route to Router2's network
    Router1(config)# ip route 192.168.4.0 255.255.255.0 192.168.1.2   // Route to Router3's network (via Router2)
    Router1(config)# ip route 192.168.5.0 255.255.255.0 192.168.1.14  // Route to Router4's network
    ```
* $$Router_2$$ ```Network Subnet Mast 192.168.3.0``` CLI commands :
  
  * ```bash
    Router2(config)# ip route 192.168.2.0 255.255.255.0 192.168.1.1   // Route to Router1's network
    Router2(config)# ip route 192.168.4.0 255.255.255.0 192.168.1.6   // Route to Router3's network
    Router2(config)# ip route 192.168.5.0 255.255.255.0 192.168.1.1   // Route to Router4's network (via Router1)
    ```
* $$Router_3$$ ```Network Subnet Mast 192.168.4.0``` CLI commands :
  
  * ```bash
    Router3(config)# ip route 192.168.2.0 255.255.255.0 192.168.1.5   // Route to Router1's network (via Router2)
    Router3(config)# ip route 192.168.3.0 255.255.255.0 192.168.1.5   // Route to Router2's network
    Router3(config)# ip route 192.168.5.0 255.255.255.0 192.168.1.10  // Route to Router4's network
    ```
* $$Router_4$$ ```Network Subnet Mast 192.168.5.0``` CLI commands :
  
  * ```bash
    Router4(config)# ip route 192.168.2.0 255.255.255.0 192.168.1.14  // Route to Router1's network
    Router4(config)# ip route 192.168.3.0 255.255.255.0 192.168.1.14  // Route to Router2's network (via Router1)
    Router4(config)# ip route 192.168.4.0 255.255.255.0 192.168.1.10  // Route to Router3's network
    ```
