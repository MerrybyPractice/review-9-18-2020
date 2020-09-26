def insert_interval(intervals, newInterval): 
    if intervals: 
        for i in range(len(intervals)): 
            compareInterval = intervals[i]

            if compareInterval[0] > newInterval[0]: 
                if compareInterval[0] > newInterval[1]: 
                    intervals = insert_specific_position(i-1, newInterval, intervals)
                elif compareInterval[0] < newInterval[1]: 
                    compareInterval = merge_intervals(compareInterval, newInterval); 
                
            elif compareInterval[0] < newInterval[0]: 
                if compareInterval[1] > newInterval[0]: 
                    compareInterval = merge(compareInterval[1], newInterval[0])
                elif compareInterval[1] < newInterval [0]: 
                    intervals = insert_specific_position(i+1, newInterval, intervals)
            
            elif compareInterval[1] > newInterval[1]: 
                if compareInterval[0] > newInterval[1]: 
                    print("The unthinkable happened") #Dont do this on a whiteboard, if you dont think a case will come up, leave it off .
                elif compareInterval[0] < newInterval[1]: 
                    compareInterval = merge(compareInterval, newInterval)

            elif compareInterval[1] < newInterval[1]: 
                insert(i+1, newInterval, intervals)
            else: 
                return intervals 
                
        return intervals
                
    else: 
        return [newInterval]

merge_intervals(compareInterval, newInterval): 
    sortInterval = compareInterval.join(newInterval)
    sortInterval.sort()

    returnInterval = [sortInterval[0], sortInterval[3]]

    return returnInterval
    
insert_specific_position(index, newInterval, intervals): 
    interval1, interval2 = intervals.split(index)
    interval1 = interval1.append(newInterval)
    intervals = interval1.join(interval2)
    return intervals
