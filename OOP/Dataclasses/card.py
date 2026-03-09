from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Card:
    rank: str = "Q"
    suit: str = "hearts"

    def to_json(self):
        return self.to_json()


card = Card()
print(card.to_json())
