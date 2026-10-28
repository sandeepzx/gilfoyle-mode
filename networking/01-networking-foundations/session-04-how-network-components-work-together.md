
# Session 4: How Network Components Work Together

## Goal

Understand how a PC sends traffic to a remote website and how the PC, switch, router, IP packet, Ethernet frame, and ARP work together.

## 1. The PC Has Its Own Routing Table

A routing table is not only found on routers. Your PC also has one, maintained by its operating system.

On Linux, view it with:

```bash
ip route
```

### Default route

```text
default via 192.168.1.1
```

If no more-specific route matches a destination, the PC sends traffic to `192.168.1.1`, commonly the home router.

### Local-network route

```text
192.168.1.0/24 dev wlp2s0 scope link
```

This says destinations within the local subnet can be reached directly through the Wi-Fi interface `wlp2s0`, without sending them to the default gateway first.

The PC generally selects the most specific matching route.

| Destination | Route normally used |
|---|---|
| `192.168.1.20` on the same subnet | Local-network route |
| A remote website's IP address | Default route via `192.168.1.1`, assuming no more-specific route exists |

Useful details in the example:

- `src 192.168.1.7`: the source IP address Linux will normally use for this route.
- `proto dhcp`: the default route was installed through DHCP.
- `dev wlp2s0`: the network interface used for the route.
- `metric 600`: a route preference value; lower metrics are generally preferred when otherwise comparable.

The PC's routing table and the router's routing table are separate. The PC makes the first routing decision. The router makes its own forwarding decision after receiving the traffic.

## 2. Understanding `192.168.1.0/24`

An IPv4 address contains 32 bits, divided into four octets of 8 bits each.

`192.168.1.0/24` means:

- `192.168.1.0` is the network address.
- `/24` means the first 24 bits identify the network.
- The remaining 8 bits are available for host addresses.

Eight bits can represent values from 0 to 255, so this subnet covers:

```text
192.168.1.0 – 192.168.1.255
```

For a typical IPv4 `/24` subnet:

- `192.168.1.0` is the network address.
- `192.168.1.1` through `192.168.1.254` are the usual usable host addresses.
- `192.168.1.255` is the broadcast address.

These are possible host addresses, not proof that every address is assigned to a connected device.

### The prefix length can vary

`/24` is common, but it is not always used.

IPv4 has 32 bits in total:

```text
Host bits = 32 − prefix length
```

For example, with `/26`:

```text
32 − 26 = 6 host bits
2^6 = 64 total addresses
```

A typical `/26` subnet has 64 total addresses, of which 62 are normally usable by hosts. The network and broadcast addresses account for the other two.

The prefix length tells you how many bits belong to the network portion. It does not always align with the end of an octet.

## 3. Destination IP vs Destination MAC

When your PC accesses a remote website, two different addresses are important:

- **Destination IP address:** identifies the remote destination at the network layer.
- **Destination MAC address:** identifies the next device to receive the frame on the current local link.

For a remote destination, the PC normally sends the local frame to its default gateway.

The outgoing traffic from your PC typically has:

- Destination IP: the remote website's IP address.
- Destination MAC: the router's MAC address on your local network.

The remote website's MAC address is not used on your local Wi-Fi link.

## 4. ARP Finds a Local MAC Address

Your PC may know the router's IP address, such as `192.168.1.1`, without currently knowing its MAC address.

For IPv4, **ARP (Address Resolution Protocol)** can discover the MAC address associated with an IPv4 address on the local network.

If the mapping is not already cached:

1. The PC broadcasts an ARP request asking which device has `192.168.1.1`.
2. The router replies with its MAC address.
3. The PC can cache the mapping and use the router's MAC address in its outgoing frame.

ARP resolves local IPv4-to-MAC mappings. It does not discover the remote website's MAC address across the internet.

## 5. What the Switch Does

A switch connects devices within a local network and forwards Ethernet frames.

It uses:

- The frame's destination MAC address.
- Its MAC address table, which maps learned MAC addresses to switch ports.

If the destination MAC address is known, the switch forwards the frame toward the associated port. If the destination is unknown, a switch generally floods the frame out eligible ports in the same VLAN, except the port on which it arrived.

A switch normally forwards frames using MAC addresses; a router forwards IP packets using IP routing information.

## 6. What the Router Does

When the router receives the frame, it processes the incoming link-layer frame and examines the IP packet inside it.

The router uses the destination IP address and its routing table to decide where to forward the packet next.

A router can connect different IP networks; it does not have to connect directly to the public internet to perform routing.

## 7. Frames and Packets Across Routers

An Ethernet frame carries an IP packet inside it.

When a router forwards a packet onto another link, it removes the incoming link-layer framing and creates a new link-layer frame appropriate for the next link.

Usually:

- The link-layer frame and its MAC addresses change at each routed link.
- The destination IP generally remains the remote website's IP address.
- The source and destination IP addresses generally remain the same unless a function such as NAT changes them.
- The IPv4 TTL decreases at each router hop.

The frame is for the current link. The IP packet carries the network-layer information across routed networks.

## 8. The Journey to a Remote Website

A simplified journey looks like this:

1. **PC checks its routing table.** It determines that the website is remote and selects the default gateway.
2. **PC resolves the gateway's MAC address if necessary.** For IPv4, it can use ARP if the mapping is not already cached.
3. **PC sends a frame to the router.** The frame's destination MAC is the router's local MAC address, while the IP packet's destination IP is the website.
4. **Switch forwards the frame.** It uses the destination MAC address and its MAC address table.
5. **Router checks the IP packet.** It uses the destination IP and its routing table to choose the next hop.
6. **Router creates a new frame.** It encapsulates the IP packet for the next link.
7. **The process repeats at later routers** until the packet reaches the destination network.

## Quick Revision

- A PC and a router each have their own routing table.
- The PC selects a route before sending traffic.
- The default route is used when no more-specific route matches.
- `/24` means 24 network bits and 8 host bits; it does not mean addresses 0 through 24.
- ARP discovers a local MAC address for an IPv4 address when needed.
- A switch forwards Ethernet frames using MAC addresses.
- A router forwards IP packets using the destination IP and its routing table.
- The destination MAC changes across routed links; the destination IP generally stays the same.
