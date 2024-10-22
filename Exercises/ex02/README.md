## Steps to Config Network in This Case
There are two ways, first is to do it by terminal interface, second is to do it by GUI Windows

### Terminal Interface
1. Add T2 Module (Not necessary, mostly used for route to router network)
2. Enable privileged user mode (grant access to user) :
   ```asm
   enable
   ```
3. Enter global configuration mode :
   ```asm
   conf terminal
   ```
4. Enter Configuration Mode of GigabitEthernet 0/0 :
   ```asm
   interface gigabitEthernet 0/0
   ```
5. Assign ip address and subnet mask to GigabitEthernet 0/0 :
   ```asm
   ip address 192.168.0.1 255.255.255.0
   ```
6. Activate the interface :
   ```asm
   no shutdown
   ```
7. Exit from current configuration mode :
   ```asm
   exit
   ```
8. Enter Configuration Mode of GigabitEthernet 0/1 :
   ```asm
   interface gigabitEthernet 0/1
   ```
9. Assign ip address and subnet mask to GigabitEthernet 0/1 :
   ```asm
   ip address 192.168.1.1 255.255.255.0
   ```
10. Activate the interface
    ```asm
    no shutdown
    ```
11. Exit from current configuration mode :
    ```asm
    exit
    ```

### GUI Interface
1. Open router and go to config tab
2. Click on GigabitEthernet 0/0 in left buttom of the pane
3. Set IPv4 address and subnet mask
4. Do the same for GigabitEthernet 0/1
5. Close the pane
6. Go to each computer's desktop and open IP Configuration
7. Set related IPv4
8. Set Default Gateway to router's ip
9. close and wait for connections to be established
