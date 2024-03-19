CompTIA Network + Exam
https://www.youtube.com/watch?v=qiQR5rTSshw&ab_channel=freeCodeCamp.org
# Introduction to Network Devices

- Layer 1 Devices
  - Analog Modem. 
	  - Modularor Demodulartor.
	  - Single connection to network
	  - Concerned about wire
  - Hub
	- Takes in a single on a wire and broadcasts it.
	- Not common now adays
- Layer 2 Devices
	- Switch 
		- Application specific integrated circuit(ASIC) chip
		- Smart enough to know about whos "on" the network
		- Has few or many ports
		- Smarter than a hub, but can be both dumb & smart
		- Only LAN devices
	- Wireless Access Point(WAP):
		- Only LAN devices
- Layer 3 Devices
	- Multilayer Switch
		- Layer 2 network switching services
		- OSI layer 3 or higher
		- ASIC chip(handles routing)
		- Can communicate with non network devices 
		- Highly programable, complex
		- Few or many ports
		- Super expensive
	- Router:
		- Most common device for connecting multiple networks together.
		- Logical network information
		- Programming for decision making instead of switches
		- LAN & non local
		- Fewer ports than a switch(generally).

## OSI Model

Developed to help disparate computing systems communicate with one another.

Layer 7 - Application
Layer 6 - Presentation
Layer 5 - Session
Layer 4 - Transport
Layer 3 - Network
Layer 2 - Data Link
Layer 1 - Physical




## Security Devices

### Firewall
- Police Force of network
- \Can be on routers(software)
- Can be it's own device
- Operates on layers 2,3,4,7.
- Can block packets from entering or leaving(stateless inspection).
	- Examines every packet and compares to a set of rules
- State of connection between networks
	- Connection to internal to external.
### Intrusion Detection System(IDS)
- Passive system 
- Designed to inform network admin
- Log files, text messages, email.
- Cannot stop or prevent.
- Recieves copy of all traffic and compares to set of standards
	- Signature: Evaluates for known malware or attack signatures
	- Anomaly: Evaluates network traffic for suspicious changes
	- Policy: Evalutes network traffic against a specific declared security policy.
 - May be deployed at host level:
	 - Host based intrusion detection system(HIDS)


### Intrustion Prevention System(IPS)
- Automated system to stop things
- Informs network admins though log files
- All traffic must flow through IPS
- Like IDS, all traffic is compared to standards
- Programmed to actively do something
	- Block offending IP addresses
	- Close vulnerable interface
	- Terminate network session
	- Redirect attack
	- more

### VPN Concentrator
- Allows for secure VPN connections to network
- Provide tunneling & encryption depending on config
- Layers 2, 3, 7
- Mostly use network layer, providing IPsec encryption through a secure tunnel.


## Optimizartion and performance devices
### Load Balancer
- Content switch/filter
- Spreads out workload between multiple hosts with same data.
- Distribute requests between servers in the server farm
### Proxy Server
- Makes requests on behalf of a client machine
- Often used to retrieve data on behalf of machines in networks.



## VPN
- Encrypted tunnel
- Once connection made, no longer seen as remote, viewed as local(even though remote).
- Cost is cheaper because no dedicated line required
- Types
	- Site to Site
	- Remote access VPN(host to site VPN): Allows specific users to connect. Must use VPN client software
	- Host to Host: SSL VPN


## VPN Protocols
- IPsec
	- Entire set
	- Layer 3 or above
	- Authentication Header(AH)
		- Transparent/Tunnel: Between two devices or between two sites
	- Encapsulating Security Payload(ESP)
		- Transparent/Tunnel: Between two devices or between two sites
		- Most popular
	- Internet Security Association and Key Management(ISAKMP)
		- Provides method for transferring security key and authentication data between systems outside of security key generating process, much more secure.
	- Generating Routing Encapsulating(GRE):
		- Can use wide variety of other network layer protocols
		- Often used to create subtunnel within IPsec connection. Only transfer IPsec packets. 
	- Point to Point Tunneling Protocol(PPTP):
		- Supports dial up VPN connections
		- Wasn't secure, but it's been updated by Microsoft
	- Transport Layer Security(TLS) Protocol:
		- Cryptographic protocol 
			- Asymmetric cryptograpgy
			- Negotiates a symmetrical security key
			- Largely replaced it's cousin secure socket layer protocol
			- Layer 5 and above
			- Most commonly creates secure encrypted internet session. SSL VPN
	- Secure Socket Layer(SSL) Protocol:
		- Largely been replaced.
		- v3.3 been to address issues but it may never catch up with TLS


## Network Access Services
### Network interface controller
- How devices connect to the internet
- Layer 2. Functional means of network communication.
	- Decides which protcol to us
	- Ethernet, point to point
	- Provides LAN node address through it's burned in physical MAC address
- Layer 1: Determines how the network data traffic will be converted to an electrical signal. Provides connection to the network.

### RADIUS(Remote Authentication Dial in User Service)
- Remote Access Service
- Authenticate remote users & grant access
- AAA(Authentication, Authorization and Accounting)
	- Ensures only people allowed to access can access
### TACACS+(Terminal Access Controller Access-Control System Plus)
- Used for authenticating remote devices
- Also AAA


## Other Services & Applications

### RAS(Remote Access Services)

- Not a protocol but a roadmap.
- Description of the combo of software & hardware required for remote access connection.

### Web Services
- XML format.
- Means for communication between disparate platforms(web)

### Unified Voice Services
- VOIP.
- Software & Hardware required to make voice communications work.




## DHCP in the Network

### Static vs Dynamic IP Addressing
- Computer told it's IP config from 
- DHCP(Dynamic Host Configuration Protocol)
- Isn't require to be on the same local network segment.
- It'll get it from one of two ways
	- Statically(manually set)
		- Works fine for small & stable.
		- Error prone when larger.
		- Admin assigns IP & subnet mask to each host(PC, router, etc)
		- Admin also sssigns default gateway location & DNS server location to each host(required if access to outside networks are allowed or human friendly names are used)
		- Each time a change is made(new gateway established), each ip config on each host must be updated. Thus cumbersome
	- Dynamically(through a service like DHCP).
		- Config DHCP
		- Automates
		- Listens on specific port for IP info requests. 
			- Responds with requested info
	- 

### How DHCP works
- Upon boot PC sends DHCP discovery packet.
	- Broadcasts to 255.255.255.255:67 UDP
- DHCP listens on that port. Once it receives it responds with offer packet. Sent back to the MAC address of the machine requesting help. Sent on port UDP 68.
- If the device uses network, it'll send request packet
- The DHCP server receives request packet then responds with acknowledgement packet
- Once device receives acknowledgement packet it updates it's IP config to reflect the info in the packet.  


#### Address Scope
- Admin configures the IP address range with one that is available to be handed out.
- Should only be used on devices that don't change IP addresses

#### Leases 
- Hands out info
- But limits the time for the config
- Admin can configure how long that config is good for
- Config
	- Default Gateway Location
	- DNS server addresses
	- Time server address
	- Many additional options
#### Preferrered IP Config
- Devices generally prefer previous IP Address

### Components and processes of DHCP