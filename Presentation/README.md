## Network-Lab Presentation, [Wireshark](https://www.wireshark.org/download.html)
Presentation of Network-Lab Class by Ramtin Kosari, 11 November 2024

<div align="center">
   <img src="https://github.com/40021441054102/Network-Lab/blob/main/Presentation/Assets/1.png" width="42%"/>
   <img src="https://github.com/40021441054102/Network-Lab/blob/main/Presentation/Assets/3.png" width="42%"/>
</div>

## Wireshark
Wireshark is a free open source network packet analyzer and my presentaton was to introduce wireshark with 6 defined scenarios to see use cases of this fantastic app, Also i talked about filtering and searching in it.

### Use Cases Scenarios
1. Broadcast Message
   Steps :
   1. We have 2 source codes ```server.sh``` and ```broadcast.sh```.
   2. Open 2 terminals and in one of them run ```server.sh``` then in another run ```broadcast.sh```.
   3. Now you can broadcast message to ```Server Terminal```, Any broadcasted message will be visible.
   4. Any sent message is visible in Wireshark and we can track them and see message exactly in packet data section. 
2. Visible Password (HTTP Insecure Test)
   1. Fist you need to install required python packages by executing ```pip3 install Flask```.
   2. In this scenario we are testing ```HTTP``` request and its insecure behaviour, I created a simple login page that when you enter username and password and submit it, your username or password is visible in wireshark packets.
   3. run the backend server by executing command ```python3 main.py```.
   4. Open login page in your browser by openning ```http://127.0.0.1:5000``` address.
   5. This scenario shows that how a HTTP website can be insecure.
3. Hidden Password (HTTPS Secure Test)
   1. This scenario is like previous scenario but the difference is that the protocol is ```HTTPS```.
   2. For this, we must create ```SSL/TLS``` certificate because HTTPS needs that, Also for local testing we need to generate self-signed certificates that are free and for development purposes.
   3. In order to generate certificate you must run ```generate_ssl_cert.sh``` that runs this command :

      ```shell
      openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365
      ```
   5. When you execute that commnad, two files with name ```cert.pem``` and ```key.perm``` will be created and when you run backend server by ```python3 main.py```, Flask needs your password (entered password for generating certificates).
   6. Open login page in your browser by openning ```https://127.0.0.1:5000``` address.
   7. When you logging in you can track wireshark and you won't see any packet that has your username and password because all are ```encrypted```.
   8. Note that there are two certificate files available in related directory that you can't use them, they are just a sample.
4. Chatbot
   1. In this scenario we create a chatbot between two devices, my suggestion is to use a ```Laptop with Ubuntu``` and ```Android Device```.
   2. If you use android device, you must install linux emulator on it to run this scenario, i suggest to use [Termux](https://github.com/termux/termux-app?tab=readme-ov-file#installation) for android.
   3. After installing it, copy ```second.sh``` there.
   4. Run ```first.sh``` on your Linux Laptop and ```second.sh``` on android device Termux.
   5. Remember that the both devices must be connected to same router or network connection. 
   6. Now the chatbot is active, you can send messages in each device and the other device receives it.
   7. While sending messages you can use ```TCP Filtering``` in your ```WIFI Interface``` by writing ```tcp``` in Wireshark's filter bar and you can see send or received packages.
   8. Also you can filter by ip address, for example you want to check packets of first device ip (e.g., 192.168.0.100), you can filter it by writing ```ip.addr == 192.168.0.100``` and you can see all related packets.
   <div align="center">
      <img src="https://github.com/40021441054102/Network-Lab/blob/main/Presentation/Assets/2.png" width="42%"/>
      <img src="https://github.com/40021441054102/Network-Lab/blob/main/Presentation/Assets/4.png" width="51%"/>
   </div>
5. DOS Attack Simulation
   1. In this scenario we simulate simple ```DOS Attack```, First you need to open Wireshark on ```Local Host Interface (Usually 'lo')```.
   2. Then you must run attacker by executing command ```python3 main.py```.
   3. Now you can see large amount of packets are appearing in Wireshark.
   4. This scenario shows that how a DOS Attack can be harmful for your network interface.
6. Mail and SMTP
   1. In this scenario we test ```SMTP Protocol```, SMTP transmits over ```TCP``` so in Wireshark we must filter ```Local Host Interface``` to see related packets.
   2. We have 2 source codes ```client.py``` and ```server.py```, that server receives emails and client sends email.
   3. Open 2 terminals and in one of them run ```server.sh``` then in another run ```client.sh```.
   4. Now after running ```client.py``` you can see related TCP packets in Wireshark and exactly sent email over ```server.py```.

I presented these scenarios in several network-lab classes of teacher ```Mona Naghde Foroosha```
