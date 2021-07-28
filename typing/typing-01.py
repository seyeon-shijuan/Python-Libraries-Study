# https://www.daleseo.com/python-typing/

from typing import List, Dict, Tuple, Set, Union, Optional, Callable, Iterable
from typing_extensions import Final


def my_func(nums: List[int] = [1,2,3]):
    pass


def my_func2(countries: Dict[str, str] = {"KR": "South Korea", "US": "United States", "CN" : "China"}):
    pass


def my_func3(user: Tuple[int, str, bool] = (3, "Dale", True)):
    pass


def my_func4(chars: Set[str] = {"A", "B", "C"}):
    pass


def my_func5(TIME_OUT: Final[int] = 10):
    pass


def to_string(num: Union[int, float]) -> str:
    return str(num)


def repeat1(message: str, times: Optional[int] = None) -> list:
    if times:
        return [message] * times
    else:
        return [message]

# Optional[int] = Union[int, None]


def repeat2(greet: Callable[ [str], str ], name: str, times: int =2) -> None:
    for _ in range(times):
        print(greet(name))

# Callable이면 인자가 함수임,
# 함수인데 str 파라미터가 있는 함수이고, 그 함수의 리턴값이 str이어야됨


def to_strings(nums: Iterable[int]) -> List[str]:
    return [str(x) for x in nums]

print(
    to_strings((1, 2, 3))
)
# Iterable로 놓으면 [] list여도 되고, () tuple이어도 되고, {} Set이어도 다 처리할 수 있음