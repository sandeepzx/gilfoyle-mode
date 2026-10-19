# Master Engineering Study Roadmap

## 1. CS Fundamentals
*Understand what is happening underneath code. Goal: Stop treating the computer as a black box.*

### Part 1: System Architecture & Memory
* **Session 1:** Memory, Stack / heap
* **Session 2:** CPU basics, Processes

### Part 2: Concurrency & Operating Systems
* **Session 3:** Threads, Concurrency basics
* **Session 4:** Files, OS concepts

### Part 3: Algorithmic Foundations
* **Session 5:** Data structures, Algorithms, Big-O

---

## 2. Python — Deep Python
*Not just Django Python. Goal: You should understand why Python behaves the way it does.*

### Part 1: Core Fundamentals & Functions
* **Session 1:** Objects and references, Mutable vs immutable
* **Session 2:** Functions, Scope

### Part 2: Advanced Flow & Control
* **Session 3:** Iterators / generators
* **Session 4:** Decorators, Exceptions, Context managers

### Part 3: Object-Oriented & Architecture
* **Session 5:** Classes / OOP, Modules / packages

### Part 4: Concurrency & Performance
* **Session 6:** async / await, Threads / multiprocessing
* **Session 7:** Python memory behavior, Profiling and optimization

---

## 3. Linux / Systems
*Major pillar for investigation: "I have a server problem" $\rightarrow$ "I can investigate it myself."*

### Part 1: Foundations
* **Session 1:** Users/groups, Permissions
* **Session 2:** Filesystems

### Part 2: System Management
* **Session 3:** Processes, `ps`, `top`, `htop`, Process monitoring, Resource usage
* **Session 4:** Signals, `systemd`, Services

### Part 3: Data & Environment
* **Session 5:** Pipes, Redirection
* **Session 6:** `grep`, `awk`, `sed`, Environment variables

### Part 4: Connectivity & Automation
* **Session 7:** SSH, Networking commands
* **Session 8:** Logs, Bash scripting

---

## 4. Networking
*Going much deeper than basic definitions.*

### Part 1: Networking Foundations
* **Session 1:** Network basics, nodes, NICs, cables, Layer 1
* **Session 2:** Ethernet, MAC addresses, frames, hubs, switches
* **Session 3:** Routers and connecting networks
* **Session 4:** How all network components work together

### Part 2: Addressing & Local Networks
* **Session 5:** IPv4, IPv6, subnet masks, CIDR
* **Session 6:** Local vs. remote communication, default gateway
* **Session 7:** ARP and IPv6 Neighbor Discovery
* **Session 8:** DHCP

### Part 3: Routing & Packet Flow
* **Session 9:** Routing tables and route selection
* **Session 10:** Packet flow, encapsulation, MTU, TTL
* **Session 11:** NAT and firewalls

### Part 4: Transport & Applications
* **Session 12:** TCP and UDP
* **Session 13:** Ports and sockets
* **Session 14:** DNS
* **Session 15:** HTTP, HTTPS, TLS

### Part 5: Networking at Scale
* **Session 16:** Proxies and load balancers
* **Session 17:** CDN, caching, redundancy, and failover

*Data Flow Path:* Browser $\rightarrow$ DNS $\rightarrow$ IP $\rightarrow$ Router $\rightarrow$ NAT $\rightarrow$ Internet $\rightarrow$ Load Balancer $\rightarrow$ Server $\rightarrow$ Application

---

## 5. DSA / Algorithms
*Keep this small and practical: Problem $\rightarrow$ Brute force $\rightarrow$ Complexity $\rightarrow$ Find bottleneck $\rightarrow$ Optimize $\rightarrow$ Understand why*

---

## 6. Databases

### Part 1: Fundamentals & Design
* **Session 1:** SQL, Normalization

### Part 2: Indexing & Performance
* **Session 2:** Indexes, B-tree, Query execution, Query optimization

### Part 3: Concurrency & Safety
* **Session 3:** Transactions, ACID, Locks, Isolation, Deadlocks

### Part 4: Internals & Scale
* **Session 4:** PostgreSQL/MySQL internals, Connection pooling, Replication, Backups

---

## 7. Backend Engineering
*Now Django becomes part of the bigger picture.*

### Part 1: Foundations & Framework
* **Session 1:** HTTP APIs, REST, Django, DRF

### Part 2: Security & Auth
* **Session 2:** Authentication, Authorization, Sessions, JWT

### Part 3: Performance, Caching & Async
* **Session 3:** Caching, Redis, Background jobs, Celery

### Part 4: Real-Time, Files & Reliability
* **Session 4:** WebSockets, File handling
* **Session 5:** API performance, Rate limiting, Idempotency, Error handling

---

## 8. Security

### Part 1: Identity & Sessions
* **Session 1:** Authentication, Authorization, Password hashing, Sessions/cookies, JWT security

### Part 2: Web Vulnerabilities
* **Session 2:** XSS, CSRF, CORS, SQL injection, Command injection, SSRF, Secure headers

### Part 3: Infrastructure & Transport Security
* **Session 3:** Linux permissions, Secrets, SSH, TLS, Firewalls, Network security

### Part 4: Security Strategy
* **Session 4:** Basic threat modeling

---

## 9. System Architecture / System Thinking
*Core Questions to Answer:*
* Where does the data live?
* What happens when 10 users become 10 million?
* What happens when the DB goes down / network fails / server crashes?
* Where is the bottleneck / should we cache, queue, or split services?

*Architecture Flow:* Browser $\rightarrow$ DNS $\rightarrow$ CDN $\rightarrow$ Load Balancer $\rightarrow$ Application Servers $\rightarrow$ Redis $\rightarrow$ Database $\rightarrow$ Storage $\rightarrow$ Background Workers

---

## 10. Infrastructure / DevOps

### Part 1: Version Control & Server Foundation
* **Session 1:** Git deeply, SSH, Linux servers

### Part 2: Containers & Application Serving
* **Session 2:** Containers, Docker, Gunicorn/Uvicorn, `systemd`
* **Session 3:** Reverse proxies, Nginx

### Part 3: Observability & Reliability
* **Session 4:** Logs, Monitoring, Metrics, Backups

### Part 4: Automation & Cloud Deployment
* **Session 5:** CI/CD, AWS/cloud basics, Deployment

---

## 11. Performance / Debugging

---

## 12. Build From Scratch
*Projects grouped by domain*

### Part 1: Networking & Protocols
* TCP client/server
* HTTP server
* DNS lookup tool
* Reverse proxy

### Part 2: Data & Storage Systems
* Mini database
* Cache
* URL shortener

### Part 3: Concurrency, Real-Time & Systems
* Chat server
* Task queue
* Monitoring tool
* CLI application

### Part 4: Security & Application Logic
* Authentication system

---

**Master Progression Order:**
CS Fundamentals $\rightarrow$ Deep Python $\rightarrow$ Linux/Systems $\rightarrow$ DSA $\rightarrow$ Networking $\rightarrow$ Databases $\rightarrow$ Backend $\rightarrow$ Security $\rightarrow$ System Architecture $\rightarrow$ DevOps $\rightarrow$ Performance $\rightarrow$ Build From Scratch