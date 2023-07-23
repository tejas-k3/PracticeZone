# https://leetcode.com/problems/hand-of-straights/
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        countMap = {}
        for card in hand:
            countMap[card] = countMap.get(card, 0) + 1
        hand.sort()
        for i in range(len(hand)):
            if countMap[hand[i]] == 0:
                continue
            for j in range(groupSize):
                currCard = hand[i] + j
                if countMap.get(currCard, 0) == 0:
                    return False
                countMap[currCard] -= 1
        return True