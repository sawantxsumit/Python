
from typing import List , Tuple , Dict , Union

n: int=44
name: str ="sumit"

nums: list[int] = [1,2,3,4,5]
names: tuple[str, int] =("sumit",55,88)
score: dict[str, int] ={"alice" :90 , "sumit":99}



def sum(a:int, b:int):
    return a+b

print(type(nums))
print(type(score))
print(nums)
print(names)
print(score)

