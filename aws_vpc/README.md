
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

# Internet Gateway
1. For IPv4 traffic, it performs network address translation (NAT) so that instances can use private IP addresses within VPC but still access the public Internet. NAT is not needed for IPv6 traffic.
2. The internet gateway is located in the VPC and does not have an IP address of its own. It uses the Instances Public IP and perform the NAT on instance's Private IP to Public IP.
3. The instance itself doesn't actually 'know' that it has a public IP address / Elastic IP address. Instead, when traffic comes from the Internet destined for the public IP address, the Internet Gateway performs a reverse NAT and sends the traffic to the private IP address of the instance. Similarly, any traffic going from the instance to the Internet Gateway comes from the private IP address of the instance, which the Internet Gateway then forwards as coming from the instance's public IP address.
4. Elastic IP address can be reassigned to another instance and traffic will immediately flow to the new instance without any configuration changes on the 'old' or 'new' instance. They just get traffic via their private IP addresses without knowing that a public IP address was involved.

### InBound Request flow from Internet to EC2
Here are the steps for the inbound request flow when a request comes in for an EC2 instance in a public subnet:
1. A request is made to the public IP address of the EC2 instance, for example by entering the public IP in a browser. 
2. The internet gateway associated with the VPC routes the incoming request to the subnet where the EC2 instance is launched. 
3. The internet gateway performs network address translation (NAT), replacing the public IP address with the private IP address of the EC2 instance.
4. Using route tables, the internet gateway sends the traffic to the correct network interface of the EC2 instance based on its private IP address. 
5. The security group and network ACL rules are checked to determine if the request is allowed to reach the instance. 
6. If allowed, the EC2 instance is able to receive the request at its private IP address. The instance then processes the request, such as serving the website content for the URL requested. 
7. The internet gateway translates the private IP back to the public IP for the response traffic before routing back to the internet.
Sources
[1] [EC2 instance in private subnet shows IPv4 address of NAT instance] (https://repost.aws/questions/QUJHaYMIefQI6IfpquqwEikQ/ec2-instance-in-private-subnet-shows-ipv4-address-of-nat-instance)


# Egress Only Gateway
1. They only support IPv6 traffic. IPv4 traffic will not flow through an egress-only internet gateway.
2. They allow instances in the VPC to initiate IPv6 sessions to the internet, but do not allow inbound connections from the internet to instances.
3. Use an egress-only internet gateway instead of a normal internet gateway when you only need outbound communication from your VPC instances to the internet and do not require inbound access from the internet to your instances.
4. Private EC2 instances can use an egress-only internet gateway to send outbound traffic. An egress-only internet gateway allows instances in a private subnet to send traffic to destinations outside the VPC, such as the internet or AWS services, without requiring a NAT device.


# NAT Gateway
1. NAT gateways uses it's own Elastic IP addresses to allow outbound internet access for instances in private subnets. This means private IP addresses are not exposed publicly.
2. Public NAT gateway for internet access, or a private NAT gateway to route traffic between VPCs and on-premises networks through a transit gateway or VPN.
3. When creating a public NAT gateway, it must be launched in a public subnet and an Elastic IP will automatically be associated with it.
4. By Default, it only supports 55k concurrent connections. By attaching more EIP adress to it, this limit can be increased.



### Notes:
1. https://github.com/aws-samples/aws-transit-gateway-egress-vpc-pattern
2. https://aws.amazon.com/blogs/networking-and-content-delivery/building-an-egress-vpc-with-aws-transit-gateway-and-the-aws-cdk/
