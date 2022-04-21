def solution(progresses, speeds):
    answer = []
    cnt = 0
    ck=0
    check = 0
    while True:                     
        if len(progresses) == 0:
            if ck != 0:
                    answer.append(ck)
                    ck=0
                    check = 0
            return answer
            
        else:
            if check == 0:
                for i in range(len(progresses)):          
                    progresses[i] += speeds[i]
                
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                ck += 1
                check = 1
                
            else:
                if ck != 0:
                    answer.append(ck)
                    ck=0
                    check = 0
