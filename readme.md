# Gilfoyle-Inspired Systems Engineering

A personal journey toward deep technical understanding, inspired by Gilfoyle from *Silicon Valley*.

Gilfoyle's understanding of infrastructure, networking, Linux, and systems engineering inspired me to pursue a similar breadth and depth of technical knowledge.

This repository documents that journey through a structured learning roadmap, detailed study notes, practical experiments, problem-solving, and projects built from scratch.

The goal is to go beyond writing code—to understand how software works underneath, investigate problems systematically, and build reliable systems.

This is an independent learning project and is not affiliated with or endorsed by *Silicon Valley* or its creators.

## Start Here

Begin with the **[Master Engineering Study Roadmap](master-roadmap.md)**.

It defines the learning path, the divisions within each subject, and the planned study sessions. Use it as the central reference for navigating the repository and deciding what to study next.

## Repository Structure

The repository is organized into three levels:

1. **Master roadmap** — the complete learning plan across all 12 divisions.
2. **Subject folders** — each major engineering subject has its own folder.
3. **Part folders and session notes** — each subject is divided into parts, with individual Markdown files for its study sessions.

Each session can cover multiple related concepts. Notes are added progressively as the material is studied, so the roadmap may include topics that have not yet been documented.

```text
gilfoyle/
├── README.md
├── master-roadmap.md
│
├── cs-fundamentals/
│   ├── 01-system-architecture-memory/
│   ├── 02-concurrency-operating-systems/
│   └── 03-algorithmic-foundations/
│
├── python-deep-dive/
│   ├── 01-core-fundamentals-functions/
│   ├── 02-advanced-flow-control/
│   ├── 03-object-oriented-architecture/
│   └── 04-concurrency-performance/
│
├── linux/
│   ├── 01-foundations/
│   │   └── session-01-users-groups-permissions.md
│   ├── 02-system-management/
│   ├── 03-data-environment/
│   └── 04-connectivity-automation/
│
├── networking/
│   ├── 01-addressing-local-networks/
│   ├── 02-transport-flow/
│   └── 03-web-scale/
│
├── dsa-algorithms/
│
├── databases/
│   ├── 01-fundamentals-design/
│   ├── 02-indexing-performance/
│   ├── 03-concurrency-safety/
│   └── 04-internals-scale/
│
├── backend-engineering/
│   ├── 01-foundations-framework/
│   ├── 02-security-auth/
│   ├── 03-performance-caching-async/
│   └── 04-realtime-files-reliability/
│
├── security/
│   ├── 01-identity-sessions/
│   ├── 02-web-vulnerabilities/
│   ├── 03-infrastructure-transport-security/
│   └── 04-security-strategy/
│
├── system-architecture/
│
├── infrastructure-devops/
│   ├── 01-version-control-server-foundation/
│   ├── 02-containers-application-serving/
│   ├── 03-observability-reliability/
│   └── 04-automation-cloud-deployment/
│
├── performance-debugging/
│
└── build-from-scratch/
    ├── 01-networking-protocols/
    ├── 02-data-storage-systems/
    ├── 03-concurrency-realtime-systems/
    └── 04-security-application-logic/
```

*This tree illustrates the organization. Individual session files will be added as the corresponding material is studied.*

## The 12 Divisions

| # | Division | Focus |
|---:|---|---|
| 01 | [CS Fundamentals](cs-fundamentals/) | The foundations beneath code: memory, CPU, processes, threads, and operating systems |
| 02 | [Python Deep Dive](python-deep-dive/) | Python's object model, language behavior, internals, and advanced programming |
| 03 | [Linux / Systems](linux/) | Filesystems, permissions, processes, services, shell tools, and troubleshooting |
| 04 | [Networking](networking/) | Addressing, TCP/IP, DNS, HTTP, sockets, routing, and communication |
| 05 | [DSA / Algorithms](dsa-algorithms/) | Data structures, algorithmic thinking, complexity, and practical problem-solving |
| 06 | [Databases](databases/) | SQL, indexing, transactions, query optimization, and database internals |
| 07 | [Backend Engineering](backend-engineering/) | APIs, Django, authentication, caching, asynchronous work, and reliable services |
| 08 | [Security](security/) | Authentication, web vulnerabilities, infrastructure security, and threat modeling |
| 09 | [System Architecture](system-architecture/) | Architecture decisions, scalability, failure handling, and distributed systems |
| 10 | [Infrastructure / DevOps](infrastructure-devops/) | Git, servers, containers, reverse proxies, CI/CD, deployment, and monitoring |
| 11 | [Performance / Debugging](performance-debugging/) | Investigation, profiling, bottleneck analysis, and optimization |
| 12 | [Build From Scratch](build-from-scratch/) | Practical implementations of networking tools, servers, storage systems, and other projects |

For the detailed parts, sessions, and planned topics, refer to the [master roadmap](master-roadmap.md).

## How to Use This Repository

1. **Read the master roadmap** to understand the complete learning path.
2. **Choose the relevant subject folder** to find its study material.
3. **Open a part folder** to explore the sessions within that section.
4. **Study the session notes** in sequence and use them for revision.
5. **Follow the roadmap's progression order** to determine what to study next.

The subjects progress in parallel rather than requiring one entire division to be completed before another begins.

## Documentation Principles

- **Understand, don't memorize.** Focus on why a concept works and how it behaves.
- **Build mental models.** Connect code with memory, operating systems, networks, databases, and infrastructure.
- **Keep notes revision-friendly.** Organize explanations so concepts can be revisited efficiently.
- **Document progressively.** Add material as it is studied instead of treating planned topics as completed work.
- **Learn by building.** Reinforce theory through coding exercises, debugging, and practical implementations.
- **Use Git as part of the journey.** Track changes, practise branching and merging, and maintain the study repository like a real engineering project.

## Project Status

**Status:** In progress

The master roadmap defines the direction. Subject folders contain the detailed notes, which will expand as more sessions are completed and more projects are built.

The objective is not simply to collect technologies or finish a list of courses. It is to develop the ability to understand systems, reason about failures, and build reliable software from first principles.

---

**Understand deeply. Debug methodically. Build from first principles.**