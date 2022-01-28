#Function that creates and return a dictionary with employee name as a key and their time frame as value.    
def build_schedule(contents):
    schedule={}
    for content in contents:
        list=content.split('=')
        schedule[list[0].strip().replace(" ","")]=list[1].strip().replace(" ","").split(',')
    return schedule

#Function that calculates when employees are at the same time, I use a the lists with the time frames and intersect them.       
def calculate_occurrencies(schedule_worker1, schedule_worker2):
    intersect=list(set(schedule_worker1).intersection(schedule_worker2))
    return len(intersect)        

#Function that creates and return a dictionary with the pair of employees as a key and the number of times that they where at same time as value.  
def office_occurrency(dictionary):
    occurrency={}
    workers=list(dictionary.keys())
    schedule=list(dictionary.values())
    for i in range(len(workers)):
        for j in range(i+1,len(workers)):
            try:
                occurrency[str(workers[i])+"-"+str(workers[j])]=calculate_occurrencies(schedule[i],schedule[j])
            except:
                pass
    return occurrency