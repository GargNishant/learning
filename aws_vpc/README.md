# VPC
1. Logically Isolated network which isolates from all other networks. Default VPC is **172.31.0.0/16**
2. IPv4 CIDR Blocks can be of RFC 1918 between /16 and /28 Prefix. CIDR Block can be added/removed after creation
3. Dedicated Tenancy ensures only Dedicated instances can be launched
4. Multiple VPCs per region possible. Possible of re-using CIDR blocks within different VPCs
5. **DNS Resolution:** Determines whether the VPC supports DNS resolution through the Amazon provided DNS server.
6. **DNS Hostnames:** Determines whether the VPC supports assigning public DNS hostnames to instances with public IP addresses.

# Subnet
1. A VPC can have multiple non-coliding Subnets. Subnet is always inside single AZ
2. The resources are launched inside Subnets.
3. All subnets within the same VPC can communicate with each other. Communication should be made via private IP address of the resources, to ensure that the traffic stays within the VPC.
4. Security Groups and Network ACLs should be configured to allow communication between Subnets.
5. Subnet must be associated with Route Table for communicating even with local resources.

# Route Table
1. Routes determine where network traffic from your subnet or gateway is directed.
2. Needs to be attached to Subnet / Gateway to be affective. When associated with IGW it becomes Gateway route table. When associated with TGW it becomes Transit gateway route table
3. 0.0.0.0/0 indicates target for all IPv4 and ::/0 for all IPv6
4. Every route table contains a local route for communication within the VPC. This route is added by default to all route tables. If your VPC has more than one IPv4 CIDR block, your route tables contain a local route for each IPv4 CIDR block.
5. Target as Local means it redirects to resources on associated subnets.
6. The route is choosen based on higher precision that matched the Target IP Address.

# Security Groups
1. Controls which traffic (Source/Destination IP Address) is allowed for inbound-outbound to resources which are associated with them
2. Stateful. If you send a request, the response traffic for that request is allowed to reach the instance regardless of the inbound security group rules. Responses to allowed inbound traffic are allowed to leave the instance, regardless of the outbound rules.
3. One instance can have multiple Security Groups, even though it is not recommened. The rules from each security group are effectively aggregated to create one set of rules
4. Cannot create rules to deny traffic. It is implicit deny or explicit allow

# Network ACLs
1. Allows or denies specific inbound or outbound traffic at the subnet level.
2. Stateless when controlling traffic. A subnet can be associated with only one network ACL at a time
3. Not recommended to modify default. Use Security Groups instead.