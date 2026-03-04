# Python OS Simulator

A terminal-based operating system simulator built with **pure Python**.
This project demonstrates core programming concepts such as **Object-Oriented Programming, file handling, system simulation, and modular architecture** without relying on external frameworks.

The simulator mimics basic operating system components including **user authentication, file management, process handling, and memory simulation**.

---

## Overview

The goal of this project is to simulate how a simple operating system manages different subsystems.
Instead of focusing on UI or frameworks, the emphasis is on **core logic, system design, and clean code structure**.

This project was built as a learning exercise to strengthen understanding of:

* Python fundamentals
* OOP design
* Modular programming
* State management
* File-based persistence

---

## Features

* **User Authentication**

  * Register and login system
  * Persistent user storage

* **File System Simulation**

  * Create virtual files
  * Read stored file content
  * Delete files
  * List available files

* **Process Manager**

  * Simulate running processes
  * Assign process IDs (PID)
  * View active processes
  * Terminate processes

* **Memory Manager**

  * Simulate memory allocation
  * Track used and free memory
  * Deallocate memory

* **System Logging**

  * Track important system events
  * User login activity
  * File operations
  * Process actions

---

## Project Structure

```
project-root/
│
├── core/
│   ├── os.py
│   ├── user.py
│   ├── file_system.py
│   ├── process.py
│   └── memory.py
│
├── data/
│   ├── users.txt
│   ├── files.json
│   └── logs.txt
│
├── main.py
└── README.md
```

Each module is responsible for a specific subsystem of the simulated OS.

---

## How It Works

When the program starts, users are presented with a login/register interface.
After authentication, the main system menu allows interaction with various simulated OS components.

The simulator uses **file-based storage** to persist data between sessions.

---

## Example Usage

```
====================================
        PYTHON OS
====================================

1. Login
2. Register
3. Exit

Enter choice: 1

Login successful!

Main Menu
1. File System
2. Process Manager
3. Memory Manager
4. View Logs
5. Logout
```

---

## Technologies Used

* Python 3
* Object-Oriented Programming
* File Handling
* JSON / Text Storage

No external libraries or frameworks were used.

---

---

## Future Improvements

Potential improvements include:

* Command-line interface enhancements
* Thread-based process simulation
* Improved memory management algorithms
* Better logging system
* User permission system

---

## Author

Dhruv

Python Developer | Exploring System Design, OOP, and Low-Level Programming

GitHub: https://github.com/Dhruv-Cmds
