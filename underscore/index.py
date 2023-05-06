class Underscore:
    def map(self, iterable, callback):
        result = [] 
        for i in iterable:
            result.append(callback(i))
        return result

    def find(self, iterable, callback):
        for i in iterable:
            if callback(i):
                return i

    def filter(self, iterable, callback):
        result = []
        for i in iterable:
            if callback(i):
                result.append(i)
        return result

    def reject(self, iterable, callback):
        result = []
        for i in range(len(iterable)):
            if not callback(iterable[i]):
                result.append(iterable[i])
        return result

# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore

print(_.map([1,2,3], lambda x: x*2)) # should return [2,4,6]
print(_.find([1,2,3,4,5,6], lambda x: x>4)) # should return the first value that is greater than 4
print(_.filter([1,2,3,4,5,6], lambda x: x%2==0)) # should return [2,4,6]
print(_.reject([1,2,3,4,5,6], lambda x: x%2==0)) # should return [1,3,5]