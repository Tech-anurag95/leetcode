class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        dic = {}
        for num in hand:
            dic[num] = dic.get(num, 0) + 1
        hand.sort()
        for num in hand:
            if dic[num] > 0:
                for i in range(groupSize):
                    if dic.get(num + i, 0) == 0:
                        return False
                    dic[num + i] -= 1
        return True