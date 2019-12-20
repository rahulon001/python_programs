def activitySelection(start_time, end_time):
    activityList = list(zip(start_time, end_time))
    activityList.sort(key = lambda x: x[1])
    print(activityList[0] , end= " ")
    for activity_index in range(1, len(activityList)):
        if activityList[activity_index][0] > activityList[activity_index-1][1]:
            print(activityList[activity_index][0])


start  =  [1, 3, 0, 5, 8, 5]
finish =  [2, 4, 6, 7, 9, 9]
activitySelection(start, finish)