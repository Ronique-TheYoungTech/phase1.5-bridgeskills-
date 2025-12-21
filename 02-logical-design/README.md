# Enterprise Network Logical Design

## Overview
This diagram represents a small-to-mid enterprise logical network design demonstrating proper segmentation, security zoning, and traffic control.

The goal of this design is to show how real-world enterprise networks separate users, servers, printers, voice, guests, and management traffic using VLANs and security policies.

---

## Network Zones
- **WAN**: Internet / ISP
- **Perimeter**: Edge Router and Firewall
- **Internal Network**: Core and Access switching infrastructure

---

## VLAN Design

| VLAN | Purpose | Subnet | Gateway |
|-----|--------|--------|--------|
| 10 | Users | 192.168.10.0/24 | 192.168.10.1 |
| 20 | Servers | 192.168.20.0/24 | 192.168.20.1 |
| 30 | Printers | 192.168.30.0/24 | 192.168.30.1 |
| 40 | Voice | 192.168.40.0/24 | 192.168.40.1 |
| 50 | Guest | 192.168.50.0/24 | 192.168.50.1 |
| 99 | Management | 192.168.99.0/24 | 192.168.99.1 |

---

## Traffic Rules (Logical Policy)

- **Users → Servers**: ALLOW (required application ports only)
- **Printers → Users**: RESTRICT (print services only)
- **Voice → Data VLANs**: DENY
- **Guest → Internal Network**: DENY
- **Management → Network Devices**: ALLOW (Router, Firewall, Switches)

---

## Design Notes
- Inter-VLAN routing is assumed to occur at the Core Switch (SVIs).
- Firewall enforces perimeter security and external access policies.
- Guest traffic is isolated and permitted internet-only access.
- Management traffic is logically separated from user data.

---

## Artifacts
- Logical topology diagram created using Draw.io

