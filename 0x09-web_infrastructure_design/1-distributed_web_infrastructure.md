# ADDITIONAL ELEMENTS

1. HAproxy Load Balancer

High availability proxy (HAproxy) provides load balancing for TCP and HTTP-based applications.
This improves performance and reliability by directing traffic to the primary and replica nodes hence distributing the load effectively.

# DISTRIBUTION ALGORITHM USED

The Round-Robin scheduling is used to distribute traffic where requests are distributed evenly between the primary and replica server.

In the design, the load balancer is enabling an Active-Active setup since both the primary and replica server are handling requests.

In active-active setup both the primary and replica server are actively handling requests simultaneously, while in an active-passive setup only the primary server handles requests while the replica server is on standby to take charge if the primary server fails.

# HOW A DATABASE PRIMARY-REPLICA (MASTER-SLAVE) CLUSTER WORKS

This is a common for scaling read operations and providing redundancy in case of failures.

The primary node is responsible for all write operations such as INSERT, UPDATE & DELETE. It maintains the authoritative copy of the data and changes made to it are logged and sent to the replica nodes.

The replica nodes on the other hand are responsible for read operations (SELECT). They recieve updates from the primary node to keep their data synchronized. Changes to the primary node are sent to the replica node through a process called replication.

# DIFFERENCE BETWEEN THE PRIMARY NODE AND THE REPLICA NODE IN REGARD TO THE APPLICATION

The primary node handles are write operations(INSERT, UPDATE, DELETE).It keep the authoritative copy of the data to maintain data integrity. It can handle read operations too but focuses on write operations.

The replica node handles read operations(SELECT) to offload the primary node. All changes need to come from the primary node as it does not handle write operations. It continously recieves and applies updates from the primary node to stay in sync.

# ISSUES WITH THIS INFRASTRUCTURE

    Single Point Of Failure(SPOF): It can happen in two levels.
    1. Load Balancer  SPOF

Here when the load balancer fails the whole system becomes inaccessible as it is responsible for traffic distribution. 2. Primary Database SPOF
If the primary database fails, write operations cannot be performed.

    Security issues
    1. Lack of firewalls: this makes the infrastructure vulnerable to unathorized access.

    2. No HTTPS: since data transmitted over http is not encrypted it posses a risk of data interception.
