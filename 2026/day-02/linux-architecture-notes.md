1. Core components of Linux (kernel, user space, init/systemd)

Kernel → The main part of Linux. It manages hardware, memory, CPU, processes.
User Space → The place where normal programs run (commands, apps, shells).
Init/Systemd → The first process that starts when Linux boots. It starts services and manages them.


2. How processes are created and managed

A new process is created using fork() (copy of parent).
Then exec() replaces it with the actual program.
The kernel manages process ID, CPU time, memory.
Systemd or commands like ps, top, kill help manage processes.

3. What systemd does and why it matters

Systemd starts all services when Linux boots.
It monitors, restarts, and controls services.
It helps troubleshoot Linux because you can check logs, service status, and failures.

1. Explain process states

Running → Process is working right now.
Sleeping → Process is waiting for something (like input).
Zombie → Process is finished but not removed yet.
Stopped → Process is paused and not running.
Waiting → Process is waiting for resources (CPU, I/O).


2. List 5 commands you use daily 

ls → Show files
cd → Change folder
ps → Show running processes
top → Live process and CPU view
cat → Read file content


