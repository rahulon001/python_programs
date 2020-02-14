"""
Example 1 : Consider the following 3 activities sorted by
by finish time.
     start[]  =  {10, 12, 20};
     finish[] =  {20, 25, 30};
A person can perform at most two activities. The
maximum set of activities that can be executed
is {0, 2} [ These are indexes in start[] and
finish[] ]

Example 2 : Consider the following 6 activities
sorted by by finish time.
     start[]  =  {1, 3, 0, 5, 8, 5};
     finish[] =  {2, 4, 6, 7, 9, 9};
A person can perform at most four activities. The
maximum set of activities that can be executed
is {0, 1, 3, 4} [ These are indexes in start[] and
finish[] ]
"""

def activitySelection(start_time, end_time):
    activityList = list(zip(start_time, end_time))
    activityList.sort(key=lambda x: x[1])
    print(activityList[0], end=" ")
    for activity_index in range(1, len(activityList)):
        if activityList[activity_index][0] > activityList[activity_index-1][1]:
            print(activityList[activity_index][0])


start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
activitySelection(start, finish)



# strip removes only from begining and end
