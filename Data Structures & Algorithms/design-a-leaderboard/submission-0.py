class Leaderboard:

    def __init__(self):
        self.scores = defaultdict(int)

        

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score


        

    def top(self, K: int) -> int:
        heap = []
        for score in self.scores.values():
            if len(heap) < K:
                heapq.heappush(heap, score)
            else:
                if score > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, score) 
        res = 0
        for num in heap:
            res += num
        return res 

        

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
