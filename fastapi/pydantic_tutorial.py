from datetime import datetime
from pydantic import BaseModel
from typing import List


class User(BaseModel):
    id: int  # 沒給默認值就是必填
    name: str = "John Snow"
    signup_ts: datetime
    friends: List[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2022-12-22 12:22",
    "friends": [1, 2, "3"]
}

user = User(**external_data)
print(user.id, user.friends)
