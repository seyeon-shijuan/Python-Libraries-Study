import json
from pathlib import Path
from typing import Any, Mapping

import numpy as np


def main(filepath: Path):
    people = get_people(filepath)
    friends_difference = get_account_difference(people)
    print(friends_difference)


def get_account_difference(people: Mapping[str, Mapping[str, Any]]) -> Mapping[int, float]:
    result = {}
    for person in people.values():
        if person["friends"] is not None:
            friends_account = [
                people[friend]["bank_account"] for friend in person["friends"]
            ]
            median = np.median(friends_account)
        else:
            median = None

        if median is None:
            result[person["id"]] = 0
        else:
            result[person["id"]] = person["bank_account"] - median

    return result


def get_people(filepath: Path) -> Mapping[str, Mapping[str, Any]]:
    with open(filepath) as fp:
        people = json.loads(fp.read())
    id2person = {}
    for person in people:
        id2person[person["id"]] = person
    return id2person


if __name__ == "__main__":
    main(Path("people.json"))

'''
1. main을 실행시키는데 Path로 windowpath를 인자로 보냄
2. get_people이 실행되는데 아까 들어온 people.json 파일이 인자로 보내짐
3. get_people: 파일열어서 JSON 정리하기
  1) file 열어서 json으로 로드함
  2) id2person 빈 dict 놓기
  3) people (json)에서 element 1개씩 for문을 돌림
     지금 element(변수명: person)에서 key값이 "id"인 것의 value를
     id2person 빈 dict의 key값으로 놓고 그 element를 통째로 value로 놓음
     -> 이게 people의 element 개수만큼 실행됨
  4) 다 되면 id2person dict를 리턴시켜서 main method안의 people에 담김
4. get_account_difference에 정리된 people dict가 인자로 보내짐
5. get_account_difference:
   1) people.values() -> 키말고 밸류값만 추려서 for문을 돌림
   2) person["friends"] 가 있으면 (id로 있음 ex:"friends": [2, 3, 4] 이렇게) 
   people[friend]["bank_account"] for friend in person["friends"]
   이 리스트를 for문으로 돌려서 people 전체 dict에서 2의 bank_account 금액 ("bank_account": 0.1)
   이런 방식으로 [0.1, 9007199254740993.0, 9007199254740993]를 만들어서 friends_account에 list로 담음
   3) numpy로 median 값인 중간 값 9007199254740993.0 이거를 골라서 median에 담음 / 없으면 None함
   4) median값이 있으면
   result[person["id"]] = person["bank_account"] - median
   rsult 빈 dict에 id를 key값으로 value값은 그사람의 bank_account에서 median 값을 빼서 저장
   5) for문이 다 돌아가면 result에는 dict가 이렇게 생기고 main method로 리턴됨
   {1: -9007199254740980.0, 2: 0, 3: 0.0, 4: 4503599627370490.0}
6. friends_difference에 리턴된 dict가 담기고 print됨
'''

## pydantic 없이 쓴 예시