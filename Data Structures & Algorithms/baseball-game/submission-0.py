class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []

        for oper in operations:
            if oper == "+":
                score.append(score[-1] + score[-2])
            elif oper == "D":
                score.append(score[-1] * 2)
            elif oper == "C":
                score.pop()
            else:
                score.append(int(oper))

        return sum(score)