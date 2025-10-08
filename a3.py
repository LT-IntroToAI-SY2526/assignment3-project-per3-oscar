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

########################################################################

def rarity_by_type(matches: List[str]) -> List[str]:
    troop = matches[0]
    result = []

    for cards in cards_db:
        if get_type(cards) == troop:
            result.append(get_rarity(cards))
    return result

def rarity_by_cost(matches: List[str]) -> List[str]:
    troop = int(matches[0])
    result = []

    for cards in cards_db:
        if get_cost(cards) == troop:
            result.append(get_rarity(cards))
    return result

def rarity_by_cards(matches: List[str]) -> List[str]:
    troop = matches[0]
    result = []

    for cards in cards_db:
        if troop in get_cards(cards):
            result.append(get_rarity(cards))
    return result

def type_by_rarity(matches: List[str]) -> List[str]:
    rarity = matches[0]
    result = []

    for cards in cards_db:
        if get_rarity(cards) == rarity:
            result.append(get_type(cards))
    return result

def type_by_cost(matches: List[str]) -> List[str]:
    cost = int(matches[0])
    result = []

    for cards in cards_db:
        if get_cost(cards) == cost:
            result.append(get_type(cards))
    return result

def type_by_cards(matches: List[str]) -> List[str]:
    card_name = matches[0]
    result = []

    for cards in cards_db:
        if card_name in get_cards(cards):
            result.append(get_type(cards))
    return result

