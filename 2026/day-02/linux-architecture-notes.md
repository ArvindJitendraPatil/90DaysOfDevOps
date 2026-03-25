# What is linux?
Linux is a free, open‑source operating system used in servers, cloud, and embedded systems.
# Core components of Linux :
- Hardware :
The physical component where OS is installed.
- Kernel :
The heart of Linux. The central core that directly controls hardware, processes, memory. Interface between hardware and software. Machine understands kernel language.
- Shell :
Interactive way to talk to kernel using commands.
- GUI :
Graphical user interface for visual interaction.
- System Libraries : 
Collections of pre-written functions that applications use to request services from the kernel.
- System Utilities : 
Programs and tools (like ls, cp, grep) that perform specific tasks, managing files, users, and system operations.
- User Space :
User space is where applications run, separate from the kernel, using system calls to access hardware.
- Init/Systemd :
The first process that starts when Linux boots. It starts services and manages them.

#  How processes are created and managed
A new process is created using fork() (copy of parent).
Then exec() replaces it with the actual program.
- The kernel manages process ID, CPU time, memory.
- Systemd or commands like ps, top, kill help manage processes.

# What systemd does and why it matters
Systemd starts all services when Linux boots.
It monitors, restarts, and controls services.
It helps troubleshoot Linux because you can check logs, service status, and failures.

# 5 Commands used daily 
- ps or top : Provides process ID, memory usage, CPU time and command name which is crucial for monitoring system performance
              and troubleshooting.
- chmod : Changing permission of files.
- systemctl : Managing system services (starting, stopping).
- df /du : df is used to monitor disk space usage and du is used to estimate size of a specific directory.
- ls -l : show file and file permission.



