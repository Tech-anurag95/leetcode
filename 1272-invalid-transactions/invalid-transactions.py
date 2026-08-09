class Solution:
    def invalidTransactions(self,transactions:List[str])->List[str]:
        ans=[]
        for i in range(len(transactions)):
            name,time,amount,city=transactions[i].split(",")
            time=int(time)
            amount=int(amount)
            if amount>1000:
                ans.append(transactions[i])
                continue
            for j in range(len(transactions)):
                if i==j:
                    continue
                name2,time2,amount2,city2=transactions[j].split(",")
                time2=int(time2)
                if name==name2 and abs(time-time2)<=60 and city!=city2:
                    ans.append(transactions[i])
                    break
        return ans