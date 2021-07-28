# https://towardsdatascience.com/pydantic-688e897cfd3a

import datetime
from decimal import Decimal
from typing import List, NewType, Optional

from pydantic import BaseModel, Field

PersonId = NewType("PersonId", int)


class Person(BaseModel):
    id: PersonId
    name: str
    bank_account: Decimal
    birthdate: datetime.date
    friends: Optional[List[PersonId]] = None




