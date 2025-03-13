import csv
import sys

class Sched:
    def __init__(self, processes, arrivalT, burstT, priority):
        self.process = int (processes)
        self.arrival = int (arrivalT)
        self.burst = int (burstT)
        self.priority = int (priority)
        self.wait_time = 0
        self.ta_time = 0
        self.total_wait_time = 0
        self.total_turnaround = 0
        self.exit = 0

print("----------------- FCFS -----------------","\n")
current_t = 0
process = []

#Reads the csv file entered from the first argument in the command line
with open(sys.argv[1], "r") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    line_ittr = 0
    for row in reader:
        if line_ittr == 0:
            line_ittr += 1
        else:
            process.append(Sched(row[0], row[1],row[2],row[3]))

g_chart = []
#Creating the Gantt chart by sorting the process with its arrival time
process.sort(key = lambda x: (x.arrival, x.process)) 
str = ""
for i in process: 
    if (current_t < i.arrival):
        str = "[{0}-{1}] Process {2}" .format(current_t, i.arrival, "IDLE")
        g_chart.append(str)

    if (current_t > i.arrival):
        str = "[{0}-{1}] Process {2}" .format(current_t, current_t + i.burst, i.process)
        g_chart.append(str)
        current_t += i.burst
        i.exit = current_t

    else:
        str = "[{0}-{1}] Process {2}" .format(i.arrival, i.arrival + i.burst, i.process)
        g_chart.append(str)
        current_t += (i.burst + i.arrival) - current_t
        i.exit = i.arrival + i.burst

print( "Process ID  |" + " Waiting time  |" + " Turnaround Time", "\n")
process.sort(key = lambda x: (x.process))
numb = 0
total_wait_time = 0
total_turnaround = 0
#Calculates the total  turnaround time and wait time, as well as the average time and throughput of the processes
for i in process:
    numb += 1
    i.ta_time = i.exit - i.arrival 
    total_turnaround += i.ta_time
    i.wait_time = i.ta_time - i.burst
    total_wait_time += i.wait_time
    
    print ("    ",i.process,"\t    |    ", i.wait_time,"\t    |    ", i.ta_time,"\n" )

print("Average Waiting Time: ", total_wait_time /numb,"\n" )
print("Average Turnaround Time: ", total_turnaround /numb ,"\n" )
print("Throughput: ", numb/current_t,"\n" ) 

#Gantt chart is created
for i in g_chart:
    print(i)


print("------------------- PS -------------------","\n")
current_t = 0
process = []
#Reads the csv file entered from the first argument in the command line
with open(sys.argv[1], "r") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    line_ittr = 0

    for row in reader:
        if line_ittr == 0:
            line_ittr += 1
        else:
            process.append(Sched(row[0], row[1],row[2],row[3]))

g_chart = []
#Sorts the arrival and priority time
process.sort(key = lambda x: (x.arrival, x.priority)) 
str = ""

for i in process:
    if (current_t < i.arrival):
        str = "[{0}-{1}] Process {2}" .format(current_t, i.arrival, "IDLE")
        g_chart.append(str)

    if (current_t > i.arrival):
        str = "[{0}-{1}] Process {2}" .format(current_t, current_t + i.burst, i.process)
        g_chart.append(str)
        current_t += i.burst
        i.exit = current_t

    else:
        str = "[{0}-{1}] Process {2}" .format(i.arrival, i.arrival + i.burst, i.process)
        g_chart.append(str)
        current_t += (i.burst + i.arrival) - current_t
        i.exit = i.arrival + i.burst

print( "Process ID  |" + " Waiting time  |" + " Turnaround Time","\n")
process.sort(key = lambda x: (x.process))
psnumb = 0
total_wait_time = 0
total_turnaround = 0
for i in process:
    psnumb+= 1
    i.ta_time = i.exit - i.arrival
    total_turnaround += i.ta_time
    i.wait_time = i.ta_time - i.burst
    total_wait_time += i.wait_time    
    print ("    ",i.process,"\t    |    ", i.wait_time,"\t    |    ", i.ta_time,"\n" )
    
print("Average Waiting Time: ", total_wait_time/psnumb,"\n" )
print("Average Turnaround Time: ", total_turnaround / psnumb ,"\n" )
print("Throughput: ", psnumb/current_t,"\n" ) 

for i in g_chart:
    print(i)
