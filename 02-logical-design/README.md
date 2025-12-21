# Enterprise Network Logical Design

## Overview
This repository contains an enterprise-grade logical network design demonstrating proper segmentation, security zoning, and traffic control for a small-to-mid sized organization.

The goal of this design is to clearly show how real-world enterprise networks separate users, servers, printers, voice, guest, and management traffic using VLANs and intentional security policies.

This artifact is focused on **design clarity and intent**, not device configuration.

---

## Logical Topology Diagram

![Enterprise Logical Network Topology](./screenshots/logical-topology.drawio.png)

*Figure 1: Enterprise logical topology with VLAN segmentation and security policy intent*

---

## Network Zones

- **WAN**
  - Internet / ISP
- **Perimeter Network**
  - Edge Router
  - Firewall
- **Internal Network**
  - Core Switch (Layer 3 / Inter-VLAN Routing)
  - Access Switches
  - Segmented VLANs

---

## VLAN Design

| VLAN ID | Name | Purpose | Subnet | Gateway |
|-------|------|--------|--------|--------|
| 10 | Users | Employee workstations | 192.168.10.0/24 | 192.168.10.1 |
| 20 | Servers | Application & infrastructure servers | 192.168.20.0/24 | 192.168.20.1 |
| 30 | Printers | Network printers | 192.168.30.0/24 | 192.168.30.1 |
| 40 | Voice | IP phones (QoS-aware) | 192.168.40.0/24 | 192.168.40.1 |
| 50 | Guest | Guest / BYOD devices | 192.168.50.0/24 | 192.168.50.1 |
| 99 | Management | Network device management | 192.168.99.0/24 | 192.168.99.1 |

---

## Traffic Rules (Logical Security Policy)

The following traffic rules represent **high-level security intent** enforced through routing, firewall rules, and access control lists.

- **Users → Servers**
  - `ALLOW` (required application ports only)

- **Printers → Users**
  - `RESTRICT` (print services only)

- **Voice → Data VLANs**
  - `DENY`

- **Guest → Internal Network**
  - `DENY` (internet access only via firewall)

- **Management → Network Devices**
  - `ALLOW` (Router, Firewall, Switches)

---

## Design Notes

- Inter-VLAN routing is assumed to occur at the **Core Switch using SVIs**.
- The **Firewall** enforces perimeter security and controls external access.
- Guest traffic is intentionally isolated from all internal resources.
- Voice traffic is logically separated to support security and quality-of-service.
- Management traffic is separated from user data to reduce attack surface.

---

## Artifacts

- Logical topology diagram created using **Draw.io**
- Screenshot stored under `./screenshots/`

---

## Status

✅ Logical design complete  
✅ VLAN segmentation complete  
✅ Security policy intent documented  
➡️ Next phase: implementation labs and configuration


