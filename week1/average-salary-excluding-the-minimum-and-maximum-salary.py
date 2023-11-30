class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop()
        print(salary)
        if len(salary) < 2:
            return 0
        k=sum(salary[1::])
        return k/(len(salary)-1)