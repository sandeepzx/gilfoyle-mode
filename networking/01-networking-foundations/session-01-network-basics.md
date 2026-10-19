# Networking — Session 1: Network Basics

## 1. What Is a Network?

A **computer network** is a group of connected devices that can communicate and share information or resources.

Devices in a network may include:
- Computers and laptops
- Phones and tablets
- Printers
- Switches and routers

A network does not necessarily require an internet connection. Devices can communicate over a local network even when internet access is unavailable.

### LAN — Local Area Network

A **LAN (Local Area Network)** connects devices within a limited area, such as a home, office, school, or building.

For example, a laptop, phone, and printer connected to the same home network can potentially communicate locally even if the broadband internet connection is down.

**Remember:**
- A network allows connected devices to communicate.
- A LAN covers a limited area.
- Internet access is not required for a network to exist.
- Local communication and internet access are different things.

## 2. Nodes and Hosts

### Node

A **node** is a broad term for a device or connection point that participates in a network.

Examples include:
- Laptop
- Printer
- Switch
- Router

A device does not need internet access to be a node. For example, a laptop can communicate with a local printer even when the internet is unavailable.

### Host

A **host** usually means an end device that sends or receives data over a network, such as a laptop, desktop, phone, or network printer.

A switch participates in network communication, but in usual networking terminology, it is generally called a network device rather than a host.

**Mental model:** A host is generally a type of node, but not every node is a host.

| Term | Meaning | Examples |
|---|---|---|
| Node | Broad term for a participating network device or connection point | Laptop, printer, switch, router |
| Host | An end device that sends or receives network data | Laptop, phone, printer |

## 3. Network Interface Card (NIC)

A **Network Interface Card (NIC)** is the hardware interface that allows a device to connect to a network and send or receive network communication.


### Wired NIC

A wired Ethernet NIC provides a network interface that communicates through an Ethernet cable. The cable commonly plugs into an Ethernet socket called an **RJ45 port**.

### Wireless NIC

A Wi-Fi NIC provides a wireless network interface. It uses radio signals and antennas to communicate with a Wi-Fi access point or wireless router.

Many laptops have both Ethernet and Wi-Fi functionality built in.


## 4. Physical Network Media

Network information must travel from one interface to another. The physical medium provides the path through which the signals travel.

### Copper Ethernet cable

Copper Ethernet cables carry information using electrical signals through copper conductors. They are commonly used to connect computers, switches, and routers.

### Fiber-optic cable

Fiber-optic cables carry information using pulses of light through optical fiber. Fiber is commonly used for high-speed links and longer-distance connections.

### Wireless radio

Wi-Fi carries information using radio waves through the air. A physical cable is not required between the wireless device and the Wi-Fi access point.

**Key idea:** Information is represented as bits, while electrical signals, light, or radio waves provide physical ways to transmit it.

## 5. How Bits Travel Physically

Computers represent information using **bits** — `0`s and `1`s. Network hardware transmits those bits using signaling methods appropriate to the medium.

A simplified wired transmission looks like this:

1. The computer's software and operating system prepare data for transmission.
2. The network interface handles its communication tasks.
3. The transmitting hardware represents the information using signals.
4. The signals travel through the cable.
5. The receiving interface detects and interprets the signals, recovering the transmitted information.

This is a simplified mental model. Real Ethernet uses defined signaling and encoding methods; it is not necessarily as simple as assigning one fixed voltage to `0` and another to `1`.

## 6. OSI Layer 1 — The Physical Layer

The **OSI model** is a conceptual framework that divides network communication into layers to make their different responsibilities easier to understand.

**Layer 1 is the Physical Layer.** It concerns the physical transmission of raw bits over a communication medium.

Examples of Layer 1 concerns include:
- Electrical, optical, or radio signals
- Cables and physical connectors
- Physical characteristics of interfaces and transmission media
- Signal timing and other transmission characteristics

Layer 1 is about **how bits are physically transmitted**. It does not decide which application should receive a message or which IP network a packet should travel through; those are concerns of higher layers.


## 8. Quick Revision

- **Network:** Connected devices that can communicate or share resources.
- **LAN:** A network covering a limited area, such as a home or office.
- **Internet:** A global network of interconnected networks; it is not required for every local network to function.
- **Node:** A broad term for a participating network device or connection point.
- **Host:** Usually an end device that sends or receives network data.
- **NIC:** Hardware that provides a device's network interface.
- **Ethernet NIC:** Provides wired network communication.
- **Wi-Fi NIC:** Provides wireless network communication using radio waves.
- **Network link:** The path used to communicate, such as an Ethernet cable or wireless link.
- **Copper Ethernet:** Uses electrical signals.
- **Fiber-optic cable:** Uses light.
- **Wi-Fi:** Uses radio waves.
- **OSI Layer 1:** The Physical Layer; concerns physical signaling and transmission of bits.

## Session 1 Complete

Session 1 covered:

1. What a network is, LANs, nodes, and hosts
2. NICs and wired versus wireless network connections
3. Physical media, signals, and OSI Layer 1


