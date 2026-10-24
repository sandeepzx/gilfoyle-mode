
# Session 3: Routers and Connecting Networks

## 1. What Is a Router?

A **router connects different IP networks** and forwards packets between them.

For example, a home network may contain:
- A laptop
- A phone
- A printer

These devices are connected to the home LAN. A router can forward traffic from that LAN toward another network, such as the ISP's network.

A router does not need an internet connection to function. If configured appropriately, it can route traffic between two private networks even when neither network has internet access.

### Switch vs. Router

A **switch** mainly connects devices within the same LAN and forwards Ethernet frames using destination MAC addresses.

A **router** forwards IP packets between networks using destination IP addresses and its routing table.

| Switch | Router |
|---|---|
| Connects devices within a LAN | Connects different IP networks |
| Uses destination MAC addresses for normal Ethernet forwarding | Uses destination IP addresses and routing information |
| Forwards Ethernet frames | Routes IP packets and places them in an appropriate frame for the next link |

A typical home Wi-Fi router often combines several functions in one device:

- **Router:** forwards traffic between networks.
- **Switch:** connects wired devices on the LAN.
- **Wireless access point:** connects Wi-Fi devices to the LAN.

These are distinct functions, even when one physical device performs all of them.

## 2. What Is a Gateway?

A **gateway** is a point through which traffic passes to reach another network. In an ordinary IP network, this is often a router.

A computer's **default gateway** is the next-hop device it uses when sending traffic to a destination that is not covered by a more specific route in its own routing table.

In a typical home network, the default gateway is the home router's LAN IP address.

For example:

- Laptop IP: `192.168.1.20`
- Router's LAN IP: `192.168.1.1`
- Website's IP: an address outside the home LAN

When the laptop needs to reach that website, it sends the traffic to its default gateway, `192.168.1.1`.

The laptop decides to use the gateway by checking **its own routing table**. The router then makes its own forwarding decision using **the router's routing table**.

## 3. What Is a Routing Table?

A **routing table** contains information that helps a router decide where to forward IP packets.

Routes usually describe destination networks, rather than storing one route for every individual website.

A route can tell the router:

- Which destination network a packet belongs to.
- Which next hop to use, if one is needed.
- Which outgoing network interface to use.

### How a Router Chooses a Route

When a router receives a packet:

1. It reads the packet's destination IP address.
2. It checks its routing table for routes that match the destination.
3. If multiple routes match, it normally chooses the most specific matching route (the longest-prefix match).
4. It forwards the packet using the selected route.

If no specific route matches, the router may use a **default route**, if one exists. A home router's default route commonly points toward the ISP.

If the router has neither a matching route nor a usable default route, it generally drops the packet. It does not automatically flood the packet through every port like a switch.

### Do Routes Disappear Automatically?

It depends on how a route was created:

- **Connected routes** generally depend on the relevant network interface being active and configured.
- **Dynamic routes** can be added, updated, or withdrawn by routing protocols.
- **Static routes** generally remain until an administrator changes or removes them, or a relevant condition makes them unusable.

Do not confuse a routing table with a switch's MAC address table. Learned MAC entries can age out after inactivity; route lifetimes and removal depend on the route's source and configuration.

## 4. Ethernet Frames and IP Packets

When a computer sends IP traffic over Ethernet, the IP packet is carried inside an Ethernet frame.

A simplified structure is:

```text
Ethernet frame
┌────────────────────────────────────────────────────┐
│ Ethernet header │ IP packet (payload) │ FCS trailer│
└────────────────────────────────────────────────────┘
```

The Ethernet header includes:

- Source MAC address
- Destination MAC address
- Other Ethernet header information

The IP packet includes:

- Source IP address
- Destination IP address
- Other IP header information
- The packet's payload

MAC and IP addresses are both represented as bits, but they belong to different headers and serve different purposes.

- **MAC address:** identifies a network interface at the link layer for local Ethernet delivery.
- **IP address:** identifies an IP endpoint and helps networks route packets toward their destination.

### Why Are Both Addresses Needed?

Suppose laptop A sends a packet to a website outside its LAN.

- The IP destination is the website's IP address.
- The Ethernet destination MAC on the first local link is normally the router's LAN MAC address, because the router is the next hop.

The laptop is sending the packet toward the router, not directly across the local Ethernet link to the remote website's MAC address.

## 5. What Happens When a Router Forwards a Packet?

Imagine a laptop sending a request to a remote server.

1. **The laptop creates an IP packet.** Its destination IP is the remote server's IP.
2. **The laptop puts the packet in an Ethernet frame.** The frame's destination MAC is the local router's MAC address.
3. **The switch forwards the frame locally.** It uses the destination MAC address to decide which port should receive the frame.
4. **The router receives the frame.** Its network interface receives the physical signal and recovers the bits. The router processes the Ethernet frame and extracts the IP packet.
5. **The router checks the destination IP.** It consults its routing table to select the next hop and outgoing interface.
6. **The router prepares a new link-layer frame.** It places the IP packet inside a frame appropriate for the next network link, using the appropriate link-layer addresses for that link.
7. **The frame travels to the next hop.** The process repeats at subsequent routers until the packet reaches the destination network.

At each routed hop, the link-layer frame is replaced for the next link. The IP packet is generally carried onward, although some IP header fields change. For example, routers reduce IPv4 TTL or IPv6 Hop Limit. NAT, when used, can also change IP addresses and related fields.

At the physical layer, network interfaces transmit and receive signals. Conceptually:

- Sending: bits are encoded into signals.
- Receiving: signals are recovered into bits.

Actual hardware integrates these operations, but this model helps explain how data moves between physical links and network protocols.

## 6. How Does the Reply Return?

If the remote server replies, the response is sent back through the network toward the laptop.

At each router, the router examines the response packet's destination IP and uses its own routing table to choose the next hop. On each Ethernet link, the packet is carried inside a frame addressed to the next hop's MAC address.

The response follows routes that lead back toward the laptop; the exact return path does not have to be identical to the outbound path.

## 7. What If a Router Has No Route?

If a router receives a packet for a destination network and has:

- No matching route, and
- No usable default route,

it generally **drops the packet** because it has no route to forward it.

A router does not flood unknown IP destinations through all ports in the way an Ethernet switch may flood a frame when its destination MAC address is unknown.

## 8. How a Home Network Reaches the Internet

A home router is connected to the home LAN and to an upstream network, usually the ISP's network.

The ISP connects to other networks, which connect onward to remote destinations. The internet is a **network of interconnected networks**.

The home router does not need to know every website individually. It can use a default route to send traffic toward the ISP when no more specific route matches.

If the home network is connected only to another private network and has no path to the wider internet, it can still communicate with reachable internal devices and services. It cannot reach external websites without a suitable path to those destinations.

## Quick Reference

- **Switch:** forwards Ethernet frames within a LAN using destination MAC addresses.
- **Router:** forwards IP packets between networks using destination IP addresses and routing information.
- **Default gateway:** the usual next hop for destinations outside the local network when no more specific route applies.
- **Routing table:** information used to choose a route or next hop.
- **Ethernet frame:** carries data across one local link; it is replaced when a router forwards the packet onto another link.
- **IP packet:** carries source and destination IP addresses and is generally forwarded across multiple networks.
- **No matching route or default route:** the router generally drops the packet.
