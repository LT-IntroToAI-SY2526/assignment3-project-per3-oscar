from cards import cards_db
from match import match
from typing import List, Tuple, Callable, Any

def get_rarity(card: Tuple[str, str, int, List[str]]) -> str:
    return card[0]


def get_type(card: Tuple[str, str, int, List[str]]) -> str:
    return card[1]


def get_cost(card: Tuple[str, str, int, List[str]]) -> int:
    return card[2]


def get_cards(card: Tuple[str, str, int, List[str]]) -> List[str]:
    return card[3]