class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for i in range(len(nums)):
            self.result += nums[i]
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for i in range(len(nums)):
            self.result -= nums[i]
        return self

# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).add(2,3,1,1,5).subtract(1).subtract(2,2,1,4,5,3).subtract(3,2).result
print(x)	# should print -1