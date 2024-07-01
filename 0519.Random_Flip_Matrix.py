class Solution:

    def __init__(self, m: int, n: int):
        self.m=m
        self.n=n

        self.used=set()

    def flip(self) -> List[int]:
        while True:
            y = random.randint(0, self.m*self.n-1)
            if y in self.used:
                continue
            self.used.add(y)
            return [y//self.n, y% self.n]

    def reset(self) -> None:
        self.used=set()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
