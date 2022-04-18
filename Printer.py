def solution(priorities, location):
    #Queue
    answer = 0
    q = [(i,p) for i,p in enumerate(priorities)]

    while True:         
        tmp = q.pop(0)  

        if q and (tmp[1] < max(j for i,j in q)):
            q.append(tmp)        
        
        else:      
            answer += 1
            if tmp[0] == location:
                return answer
