# Physical Network Topology – Foundation

## Overview
This document describes the **physical network design** for a small-to-mid size enterprise environment.  
The goal is to demonstrate understanding of **real-world infrastructure layout**, device roles, and physical connectivity from the ISP demarcation point to end-user devices.

This design focuses on **how the network is physically built**, not how traffic is logically segmented.

---

## Objectives
- Understand enterprise physical network layering
- Identify correct device placement and roles
- Demonstrate proper cabling concepts
- Create a reusable baseline for logical and security design

---

## Physical Topology Diagram

![Physical Network Topology](./screenshots/physical-topology.drawio.png)

---

## Network Layers Explained

### 1. Internet / ISP
- Represents the external service provider
- Includes the **ISP demarcation point (handoff)** into the customer network
- Connection type: WAN uplink (typically fiber or Ethernet)

---

### 2. Edge Layer
**Devices:**
- Edge Router
- Firewall

**Purpose:**
- WAN routing
- Network Address Translation (NAT)
- Security policy enforcement
- Acts as the boundary between public and private networks

---

### 3. Core Layer
**Device:**
- Core Switch

**Purpose:**
- Aggregates traffic from access switches
- Provides high-throughput switching
- Central connection point for internal networks

---

### 4. Access Layer
**Devices:**
- Access Switches

**Purpose:**
- Connect end devices to the network
- Provide VLAN access
- May support Power over Ethernet (PoE) for phones and access points

---

### 5. Endpoints
**Examples:**
- Workstations
- Servers
- Printers
- IP Phones
- Wireless Access Points

---

## Cabling Considerations
- WAN uplinks may use **single-mode fiber** or Ethernet depending on ISP
- Internal LAN connections typically use **Cat6 Ethernet**
- Trunk links between switches support VLAN tagging
- Physical cabling choices impact performance, scalability, and reliability

---

## Design Notes
- This diagram intentionally excludes logical elements such as VLANs and IP addressing
- Redundancy and high availability are not shown at this stage
- The physical design serves as a **foundation** for logical topology, security policy, and routing decisions

---

## Next Steps
- Create a **Logical Network Topology**
- Define VLAN segmentation
- Plan IP addressing
- Introduce security zones and traffic flow rules

