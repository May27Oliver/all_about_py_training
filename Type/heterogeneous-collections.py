# 異質性群組

from typing import Dict, Tuple, List, Union

AutoToCountMapping = Dict[str, int]
# 異質性元組 Tuple can insert multiple type
heterogeneous_collect = Tuple[str, int, float]
# heterogeneous_collect = List[str, int, float]  # List塞入多個型別會出錯

Ingredient = Tuple[str, int, str]
Recipe = List[Union[int, Ingredient]]

print([5])
