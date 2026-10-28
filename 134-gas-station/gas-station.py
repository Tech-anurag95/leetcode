class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(cost)>sum(gas):
            return -1
        tank=0
        total=0
        start=0
        for i in range(len(gas)):
            balance=gas[i]-cost[i]
            total+=balance    
            tank+=balance
            if tank<0:      #mtlb ab tank me fuel ki kami hai to wo aage nhi jaa payeha so current start becomes invalid  so start=i+1
                start=i+1
                tank=0
        if total<0:
            return -1
        return start


#START=CURRENT STARTING POINT
#TANK=CURRENT CAPACITY OF TANK AFTER GOING FROM START TO Ith
#BALANCE=NET FUEL GAINED OR LOST 
#TOTAL=The sum of fuel balances across ALL stations




# tank tells us whether we can continue from our current start.
# total tells us whether completing the entire circuit is possible at all.

        