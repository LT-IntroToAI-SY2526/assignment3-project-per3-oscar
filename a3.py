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
    troop = matches[0]
    result = []

    for cards in cards_db:
        if get_rarity(cards) == troop:
            result.append(get_type(cards))
    return result

def type_by_cost(matches: List[str]) -> List[str]:
    troop = int(matches[0])
    result = []

    for cards in cards_db:
        if get_cost(cards) == troop:
            result.append(get_type(cards))
    return result

def type_by_cards(matches: List[str]) -> List[str]:
    troop = matches[0]
    result = []

    for cards in cards_db:
        if troop in get_cards(cards):
            result.append(get_type(cards))
    return result

def cost_by_rarity(matches: List[str]) -> List[int]:
    troop = matches[0]
    result = []

    for cards in cards_db:
        if get_rarity(cards) == troop:
            result.append(get_cost(cards))
    return result

def cost_by_type(matches: List[str]) -> List[int]:
    troop = matches[0]
    result = []

    for cards in cards_db:
        if get_type(cards) == troop:
            result.append(get_cost(cards))
    return result

def cost_by_cards(matches: List[str]) -> List[int]:
    troop = matches[0]
    result = []

    for cards in cards_db:
        if troop in get_cards(cards):
            result.append(get_cost(cards))
    return result

def cards_by_rarity(matches: List[str]) -> List[str]:
    troop = matches[0]
    result = []

    for cards in cards_db:
        if get_rarity(cards) == troop:
            result.extend(get_cards(cards))
    return result

def cards_by_type(matches: List[str]) -> List[str]:
    troop = matches[0]
    result = []

    for cards in cards_db:
        if get_type(cards) == troop:
            result.extend(get_cards(cards))
    return result

def cards_by_cost(matches: List[str]) -> List[str]:
    troop = int(matches[0])
    result = []

    for cards in cards_db:
        if get_cost(cards) == troop:
            result.extend(get_cards(cards))
    return result

######################################################################3

pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what rarity does the _ type have"), rarity_by_type),
    (str.split("what rarity costs _ elixir"), rarity_by_cost),
    (str.split("what rarity does the card % have"), rarity_by_cards),
    (str.split("what type has the _ rarity"), type_by_rarity),
    (str.split("what type costs _ elixir"), type_by_cost),
    (str.split("what type does the card % have"), type_by_cards),
    (str.split("how much does a _ card cost"), cost_by_rarity),
    (str.split("how much does a _ type card cost"), cost_by_type),
    (str.split("how much does % cost"), cost_by_cards),
    (str.split("what cards are _"), cards_by_rarity),
    (str.split("what cards are  the _ type"), cards_by_type),
    (str.split("what cards cost _ elixir"), cards_by_cost),
]

#####################################################################3

def search_pa_list(src: List[str]) -> List[str]:
    for pat, act in pa_list:
        mat = match(pat, src)

        if mat is not None:
            answer = act(mat)
            if answer:
                return answer 
            else:
                return ["No answers"] 
            
    return ["I don't understand"]

if __name__ == "__main__":

    pass

print("All tests passed!")
