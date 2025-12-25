# Cloud Network Fundamentals
## Sample Cloud Network Architecture

## Deliverables

- Cloud network conceptual diagram
- Explanation of core cloud networking principles
- Subnet and routing explanation


## Purpose
This document demonstrates foundational cloud networking concepts, including virtual network design, segmentation, routing, and security boundaries.

The architecture presented is a conceptual example used to illustrate best practices in cloud-based networking environments.

---

## Methodology

This architecture is a conceptual representation demonstrating key cloud network concepts. It is vendor-neutral and focuses on logical design principles without implementation-specific details.



## Cloud Concepts Covered
- Virtual Private Cloud (VPC / VNet)
- Public and private subnet separation
- Internet gateway
- Route tables
- Security groups / network security rules

---

## Architecture Overview
The cloud network consists of:
- A virtual private cloud
- A public subnet hosting internet-facing resources
- A private subnet hosting internal services
- An internet gateway providing controlled external access
- Route tables governing traffic flow

![Cloud Network Topology](diagrams/cloud-network-topology.png)
- Security groups / network security rules applied at the subnet boundary

---

## Traffic Flow Explanation
-External traffic enters the virtual network through the internet gateway, where it can be routed to public resources or controlled to reach internal services.
- Public subnet resources handle external communication
- Private subnet resources are isolated from direct internet access
- Internal traffic is restricted by routing and security rules

---

## Security Considerations
- Separation of public and private subnets reduces attack surface
- Security groups enforce least-privilege access
- Private resources are not directly exposed to the internet
- Security groups (or network security rules) restrict access within and between subnets.


---

## Conclusion
This architecture demonstrates foundational cloud networking principles required for secure and scalable deployments. These concepts form the basis for more advanced cloud and hybrid networking designs.

---

### 📄 Document Information

**Author:** Ronique Young  
**Diagram Tool:** Topology diagram created using draw.io (diagrams.net)


