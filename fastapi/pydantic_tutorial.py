from datetime import datetime
from pydantic import BaseModel, ValidationError
from typing import List, Optional

# pydantic 提供 BaseModel 讓開發者能夠透過繼承該類別並且利用 typing 註記類別屬性的型別，就能夠擁有基本的驗證功能。


class User(BaseModel):
    id: int  # 沒給默認值就是必填
    name: str = "John Snow"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    # "id": "123",  # 這裡給string會報錯
    "id": 123,
    "signup_ts": "2022-12-22 12:22",
    "friends": [1, 2, "3"]
}

user = User(**external_data)
print("user.id, user.friends：", user.id, user.friends)
print("user.dict可以展開user：", user.dict())

'''try:
    User(id=1, signup_ts=datetime.today(),
         friends=[1, 2, "not number"])
except ValidationError as e:
    print(e.json)
'''

try:
    User(signup_ts='broken', friends=[1, 2, 'not number'])
except ValidationError as e:
    print(e.json())
