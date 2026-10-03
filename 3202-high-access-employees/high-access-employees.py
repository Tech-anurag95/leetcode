class Solution:
    def findHighAccessEmployees(self,access_times:List[List[str]])->List[str]:
        ans=[]
        dic={}
        for employee,time in access_times:
            if employee not in dic:
                dic[employee]=[]
            dic[employee].append(time)
        for employee in dic:
            if len(dic[employee])<3:
                continue
            dic[employee].sort()
            times=dic[employee]
            for i in range(len(dic[employee])-2):
                t1=int(times[i][:2])*60+int(times[i][2:])
                t2=int(times[i+2][:2])*60+int(times[i+2][2:])
                if t2-t1<60:
                    ans.append(employee)
                    break
        return set(ans)
                

                
                          
        