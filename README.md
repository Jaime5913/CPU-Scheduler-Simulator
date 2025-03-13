
# CPU Scheduler Simulator

## Notes
- The program handles cases where the CPU might be idle (when no processes are available)
- Processes are sorted by arrival time and then by process ID (for FCFS) or priority (for PS)
- Lower priority values indicate higher priority in the priority scheduling algorithm

## Overview
This Python program implements a CPU scheduling simulator that compares two common scheduling algorithms: First-Come-First-Served (FCFS) and Priority Scheduling (PS). The simulator reads process data from a CSV file, executes both scheduling algorithms, and generates detailed performance metrics and Gantt charts for each algorithm.

## Features
- Implementation of two CPU scheduling algorithms:
  - First-Come-First-Served (FCFS): Processes are executed in order of arrival
  - Priority Scheduling (PS): Processes are executed based on priority values (lower values indicate higher priority)
- Performance metrics calculation:
  - Waiting time for each process
  - Turnaround time for each process
  - Average waiting time
  - Average turnaround time
  - Overall system throughput
- Visual Gantt chart generation for process execution timelines
- Support for idle CPU time handling

## File Description
### scheduler.py
This is the main program file that:
- Reads process data from a CSV file specified as a command-line argument
- Implements a `Sched` class to represent process information including:
  - Process ID
  - Arrival time
  - Burst time (execution time)
  - Priority
  - Wait time
  - Turnaround time
  - Exit time
- Simulates the FCFS scheduling algorithm
- Simulates the Priority Scheduling algorithm
- Calculates and displays performance metrics for both algorithms
- Generates Gantt charts showing the execution timeline

## Input Format
The program uses a CSV file with the following format:
```
Process ID, Arrival Time, Burst Time, Priority
1, 0, 5, 2
2, 3, 3, 1
...
```
- First row should contain headers
- Each subsequent row represents a process with its attributes

## Usage
```bash
python scheduler.py input_file.csv
```

## Output
For each scheduling algorithm (FCFS and PS), the program outputs:
1. A table showing:
   - Process ID
   - Waiting time
   - Turnaround time
2. Average waiting time across all processes
3. Average turnaround time across all processes 
4. System throughput (processes completed per unit time)
5. A Gantt chart showing the execution timeline with format:
   `[start_time-end_time] Process ID`

## Example Output
```
----------------- FCFS -----------------

|Process ID  | Waiting time  | Turnaround Time 

     1       |     0        |     5

     2       |     2        |     5

Average Waiting Time:  1.0

Average Turnaround Time:  5.0

Throughput:  0.25

[0-5] Process 1
[5-8] Process 2

------------------- PS -------------------

Process ID  | Waiting time  | Turnaround Time 

     1       |     0        |     5

     2       |     2        |     5

Average Waiting Time:  1.0

Average Turnaround Time:  5.0

Throughput:  0.25

[0-5] Process 1
[5-8] Process 2
```

