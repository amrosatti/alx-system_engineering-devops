# Three-Server Web Infrastructure for foobar.com

![Distributed Infrastructure Design](images/Distributes_web_infrastructure.jpg)

**Scenario:** A user tries to access "www.foobar.com"

## Components
* **User's Computer:** Initiates the request by typing the website URL
* **Internet:** Carries the request from the user
* **Domain Name System (DNS):** Translates "www.foobar.com" into the server's IP address "8.8.8.8"
* **Load Balancer (HAproxy):** Acts as a traffic cop, distributing incoming requests evenly across two web servers. It uses a Round Robin algorithm by default, sending requests to each server sequentially
* **Web Server (Nginx) (x2):** Two web servers are configured to handle incoming requests from the load balancer. They retrieve static website files and communicate with the application server
* **Application Server:** Handles dynamic content generation (using the codebase) and interacts with the database
* **Application Files (The Codebase):** Contains the website's functionality and appearance code
* **Database (MySQL) - Primary-Replica Cluster:**
	- **Primary Node (Master):** The master database that stores all the original data and handles write operations (inserts, updates, deletes)
	- **Replica Node (Slave):** A copy of the primary database that receives updates periodically and is used for read operations (retrieving data)


## Communication
1. The user's computer sends a request to the server's IP address via the internet
2. The DNS server translates the domain name to the IP address
3. The request reaches the load balancer
4. The load balancer distributes the request to one of the available web servers using its algorithm (Round Robin)
5. The web server retrieves static files and communicates with the application server
6. The application server might interact with the primary database to retrieve or store data
7. The application server sends the website content back to the web server
8. The web server sends the complete website content back to the user's computer
9. The user's computer displays the website content in the browser


## Simple Web Stack vs. Distributed Web Infrastructure
- **Increased Availability:** If one web server fails, the load balancer redirects traffic to the other, minimizing downtime
- **Improved Scalability:** By adding more web servers behind the load balancer, it can handle increased traffic
- **Database Read Performance:** Replica nodes can handle read requests, offloading the primary database and improving overall performance


### Active-Passive vs. Active-Active Load Balancers
- **Active-Passive:** One load balancer is active, routing traffic. The other is passive, acting as a backup and taking over if the primary fails.
- **Active-Active:** Both load balancers are actively distributing traffic, providing higher availability but requiring more complex configuration.


### Database Primary-Replica Cluster
- The primary node handles all write operations and replicates data periodically to the replia node(s).
- Applications connect to the primary node for write operations and can choose to connect to either primary or replica nodes for read operations. This distributes the load and improves read performance.


### Security Issues
* **No Firewall:** The current setup lacks a firewall to filter incoming and outgoing traffic, potentially exposing vulnerabilities.
* **No HTTPS:** Communication is not encrypted, making data transfer susceptible to interception.
* **No Monitoring:** The infrastructure lacks monitoring to track server health and identify potential issues.


### Where are SPOFs?
* While this setup is more resilient, there are still potential SPOFs:
	- The load balancer: If it fails, no traffic reaches the web servers.
	- The application server: A critical failure could prevent website functionality.
	- The primary database: If the primary node fails and there's no functioning replica, data loss might occur.
