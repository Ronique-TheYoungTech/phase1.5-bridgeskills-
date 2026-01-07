# 07 — Monitoring (Bridge Skills)

## Objective
Implement and validate foundational network monitoring mechanisms used in enterprise environments, including:

- Syslog (centralized logging)
- SNMP (device monitoring and telemetry)
- NTP (time synchronization)

This lab emphasizes correct configuration, router-side verification, and clear documentation of Cisco Packet Tracer limitations encountered during implementation.

---

## Topology Overview

**Diagram:** `./diagrams/monitoring-architecture.png`

### Devices
- Cisco 2901 Router
- Cisco 2960 Switch
- PC (Admin workstation)
- Server-PT (Syslog server)

---

## IP Addressing (Foundational)

| Device | Interface | IP Address |
|-------|-----------|------------|
| Router0 | GigabitEthernet0/0 | 192.168.24.1 /24 |
| PC0 | NIC | 192.168.24.10 /24 |
| Syslog Server | NIC | 192.168.24.20 /24 |

**Evidence**
- `./screenshots/ip-router-config.png`

Proper Layer-3 connectivity is required for all monitoring services in this lab.

---

## Syslog Configuration

Syslog was enabled on the router and configured to forward log messages to a centralized syslog server.

### Configuration
```plaintext
logging on
logging 192.168.24.20


Verification

Syslog functionality was validated using router-side verification commands:
```bash
show logging
```

This confirmed:

Syslog logging is enabled

Logs are being sent to 192.168.24.20 over UDP port 514

Log messages are actively generated and counted

Evidence

./screenshots/syslog-simulation-proof.png

Platform Limitation (Syslog)

Cisco Packet Tracer does not reliably surface SYSLOG packets in Simulation Mode and does not consistently populate the Syslog Server GUI.
Syslog functionality was therefore validated using router-side logging status, which is the authoritative verification method used in production environments.

SNMP Configuration

SNMP was enabled on the router to allow read-only monitoring access.

Configuration
```bash
snmp-server community public RO
```

Verification
Syslog functionality was validated using router-side verification commands:
```bash
show logging 
```
This confirmed:

Syslog logging is enabled

Logging destination is 192.168.24.20 over UDP port 514

Log messages are actively generated and counted

Evidence

./screenshots/syslog-enabled.png

./screenshots/syslog-config.png

./screenshots/syslog-simulation-proof.png

Platform Limitation (Syslog)

Cisco Packet Tracer does not reliably surface SYSLOG packets in Simulation Mode and does not consistently populate the Syslog Server GUI.
Syslog functionality was therefore validated using router-side logging status, which is the authoritative verification method used in production environments.

SNMP Configuration

SNMP was enabled on the router to allow read-only monitoring access.

Configuration
```bash
snmp-server community public RO
```

Verification
```bash
show running-config | include snmp
```

This confirmed that the SNMP agent is enabled and a read-only community string is configured.

Evidence

./screenshots/snmp-config.png

./screenshots/snmp-simulation-proof.png

Platform Limitation (SNMP)

The Packet Tracer build used in this lab does not include an SNMP Manager service or SNMP polling tools.
As a result, SNMP traffic could not be generated in Simulation Mode. SNMP functionality was validated using router configuration output and SNMP agent initialization messages.

NTP Configuration

The router was configured to synchronize time using a public NTP server.

Configuration
```bash
ntp server 129.6.15.28
```

Verification
```bash
show running-config | include ntp
show ntp status
show clock
```
These commands verified correct NTP configuration and router clock operation.

Evidence

./screenshots/ntp-config.png

./screenshots/ntp-status.png

Platform Limitation (NTP)

Packet Tracer may not fully synchronize time with public NTP servers. NTP validation was performed using configuration and status commands rather than time accuracy.

Key Takeaways

Monitoring services rely on proper Layer-3 connectivity

Syslog, SNMP, and NTP require different validation approaches

Router-side verification is authoritative when external tools are unavailable

Packet Tracer limitations must be documented clearly and honestly

Platform Limitations Summary

SYSLOG packets do not reliably appear in Simulation Mode

Syslog Server GUI may remain empty despite correct configuration

No SNMP Manager or polling tools are available in this Packet Tracer build

SNMP traffic cannot be generated without a manager

NTP synchronization may remain unsynced

All services were validated using production-appropriate verification methods.

Status

✔ Router IP addressing configured
✔ Syslog enabled and verified
✔ SNMP agent enabled and verified
✔ NTP configured and validated
✔ Platform limitations documented

07-Monitoring (Bridge Skills) — COMPLETE

Author & Notes

Author: Ronique Young
Track: CAINO — Bridge Skills
Tools: Cisco Packet Tracer

This lab was completed as part of a skills-first engineering path emphasizing router-side verification, honest documentation of tool limitations, and production-aligned troubleshooting methodology.


