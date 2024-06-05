# A One Server Web Infrastructure

**Scenario:** A user wants to visit a website "www.foobar.com"

## Components:
* **User's Computer:** Initiates the request by typing the website URL
* **internet:** Carries the request from the user
* **Domain Name System (DNS):** Acts like a phonebook for the internet, translating "www.foobar.com" into the server's IP address "8.8.8.8"
* **Server:** A physical/virtual computer running software to host the website:
	- **Web Server (Nginx):** Listens for incoming requests and retrieves the website files from the application server
	- **Application Server:** Handles dynamic content generation (using the codebase) and interacts with the database
	- **Database (MySQL):** Stores website data (e.g. user info, content...etc)
	- **Application Files (Codebase):** Contains the website's functionality and appearance code.


## Communication:
1. The user's computer sends a request to the server's IP address via the internet
2. The web server receives the request and fetches the necessary files from the application server
3. The application server might interact with the database to retrieve data
4. The application server sends the website content back to the web server
5. The web server sends the complete website content back to the user's computer
6. The user's computer displays the website content in the browser


## Issues:
- **Single Point of Failure (SPOF):** The entire website goes down if the server fails
- **Downtime during Maintenance:** The website becomes unavailable when updating the application server (e,g, new code deployment)
- **Limited Scalability:** The server can't handle large traffic, potentially leading to slowdowns or crashes
