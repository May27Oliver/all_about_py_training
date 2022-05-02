from typing import Optional


class HotDog:

    def add_condiments(self, *args):
        pass


class Bun:
    def __init__(self, name) -> None:
        self.name = name

    def add_frank(self, frank: str) -> HotDog:
        return HotDog()

# Optional can remind you return value might be None


def are_buns_avaliable() -> bool:
    return True


def dispense_bun() -> Optional[Bun]:
    if not are_buns_avaliable():
        return None

    return Bun('Wheat')


def dispense_ketchup():
    return None


def dispense_mustard():
    return None


def dispense_frank() -> str:
    return "frank"


def dispense_hot_dog_to_customer(hot_dog: HotDog):
    pass


def create_hot_dog():
    bun = dispense_bun()
    if bun is None:
        print("Bun unavailable. check for bun")
        return
    frank = dispense_frank()
    if frank is None:
        print("Frank was not properly dispendsed")
        return
    hot_dog = bun.add_frank(frank)
    if hot_dog is None:
        print("Hot Dog unavaliable. Check for Hot Dog")
        return
    ketchup = dispense_ketchup()
    mustard = dispense_mustard()
    if ketchup is None or mustard is None:
        print("Check for invalid catsup")
        return
    hot_dog.add_condiments(ketchup, mustard)
    dispense_hot_dog_to_customer(hot_dog)
