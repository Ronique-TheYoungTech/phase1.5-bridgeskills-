Network Troubleshooting & Performance Optimization
Mock Incident Case Study
Scenario Overview

Users reported slow network performance and intermittent connectivity when accessing internal application servers during business hours.

The issue impacted multiple departments and was most noticeable during peak usage times.

Initial Symptoms

Slow application response times

Occasional packet loss

Users reporting “network drops”

No complete outages observed

Troubleshooting Methodology

A structured troubleshooting approach was used, following a layered (OSI-informed) methodology:

Verified physical connectivity and interface status

Checked VLAN configuration and port assignments

Reviewed routing paths and gateway configuration

Analyzed traffic flow and potential congestion points

Root Cause Identified

The root cause was identified as improper VLAN trunk configuration, causing excessive broadcast traffic to traverse unnecessary segments.

This resulted in congestion and performance degradation during peak usage periods.

Resolution Steps

Corrected trunk port VLAN allowances

Restricted unnecessary VLAN propagation

Verified correct access VLAN assignments

Validated routing and gateway behavior

Performance Outcome

After remediation:

Latency was reduced

Packet loss was eliminated

Application performance returned to normal

Network stability improved during peak hours

Lessons Learned

Proper VLAN segmentation is critical for performance

Misconfigured trunks can cause widespread issues

Structured troubleshooting prevents guesswork

Documentation aids faster resolution

Optimization Recommendations

Periodic configuration reviews

Traffic monitoring during peak hours

Clear VLAN documentation

Standardized change management

📌 Note: This was a controlled mock scenario designed to demonstrate professional troubleshooting methodology.
