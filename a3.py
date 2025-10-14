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
            result.append(get_cards(cards))
    return result

def cards_by_type(matches: List[str]) -> List[str]:
    troop = matches[0]
    result = []

    for cards in cards_db:
        if get_type(cards) == troop:
            result.append(get_cards(cards))
    return result

def cards_by_cost(matches: List[str]) -> List[str]:
    troop = int(matches[0])
    result = []

    for cards in cards_db:
        if get_cost(cards) == troop:
            result.append(get_cards(cards))
    return result

def average_elixir_cost(matches: List[str]) -> List[str]:
    result = []

    for troop in matches:
        for cards in cards_db:
            if troop in get_cards(cards):
                result.append(get_cost(cards))
                break

    if not result:
        return ["0"]

    avg = sum(result) / len(result)
    return [str(avg)]

######################################################################3

pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what rarity does the _ type have"), rarity_by_type),
    (str.split("what rarity costs _ elixir"), rarity_by_cost),
    (str.split("what rarity does the card % have"), rarity_by_cards),
    (str.split("what type has the _ rarity"), type_by_rarity),
    (str.split("what type does the card % have"), type_by_cards),
    (str.split("how much does a _ card cost"), cost_by_rarity),
    (str.split("how much does a _ type card cost"), cost_by_type),
    (str.split("how much does % cost"), cost_by_cards),
    (str.split("what cards are _"), cards_by_rarity),
    (str.split("what cards are the _ type"), cards_by_type),
    (str.split("what cards cost _ elixir"), cards_by_cost),
    (str.split("What is the average elixir cost for cards _"), average_elixir_cost)
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

    assert rarity_by_type(match(["what", "rarity", "does", "the", "_", "type", "have"], ["what", "rarity", "does", "the", "building", "type", "have"])) == [
        "common", "rare", "rare", "rare", "rare", "rare", "rare", "rare", "rare", "rare"
    ], "test rarity_by_type failed"

    assert rarity_by_cost(match(["what", "rarity", "costs", "_", "elixir"], ["what", "rarity", "costs", "6", "elixir"])) == [
        "rare", "rare", "epic", "epic", "legendary", "legendary", "legendary"
    ], "test rarity_by_cost failed"

    assert rarity_by_cards(match(["what", "rarity", "does", "the", "card", "%", "have"], ["what", "rarity", "does", "the", "card", "skeletons", "have"])) == [
        "common"
    ], "test rarity_by_cards failed"

    assert type_by_rarity(match(["what", "type", "has", "the", "_", "rarity"], ["what", "type", "has", "the", "champion", "rarity"])) == [
        "troop", "troop", "troop", "troop"
    ], "test type_by_rarity failed"

    assert type_by_cards(match(["what", "type", "does", "the", "card", "%", "have"], ["what", "type", "does", "the", "card", "ice spirit", "have"])) == [
        "troop"
    ], "test type_by_cards failed"

    assert cost_by_rarity(match(["how", "much", "does", "a", "_", "card", "cost"], ["how", "much", "does", "a", "epic", "card", "cost"])) == [
        4, 4, 5, 6, 7, 7, 8
    ], "test cost_by_rarity failed"

    assert cost_by_type(match(["how", "much", "does", "a", "_", "type", "card", "cost"], ["how", "much", "does", "a", "champion", "type", "card", "cost"])) == [
        3, 4, 4, 5
    ], "test cost_by_type failed"

    assert cost_by_cards(match(["how", "much", "does", "%", "cost"], ["how", "much", "does", "skeletons", "cost"])) == [
        1
    ], "test cost_by_cards failed"

    assert cards_by_rarity(match(["what", "cards", "are", "_"], ["what", "cards", "are", "rare"])) == [
        "royal giant", "royal recruits", "barbarians", "knight", "archers",
        "minions", "firecracker", "royal delivery", "goblin giant", "musketeer",
        "mini pekka", "hog rider", "battle ram", "zappies", "flying machine",
        "battle healer", "goblin demolisher", "wizard", "royal hogs",
        "three musketeers", "cannon cart", "electro dragon", "giant skeleton",
        "electro wizard", "night witch", "magic archer", "mother witch",
        "phoenix", "goblin machine", "ram rider", "sparky", "spirit empress"
    ], "test cards_by_rarity failed"

    assert cards_by_type(match(["what", "cards", "are", "the", "_", "type"], ["what", "cards", "are", "the", "spell", "type"])) == [
        "zap", "giant snowball", "rage", "barbarian barrel", "goblin curse", "log",
        "fireball", "rocket", "poison", "arrows", "freeze", "clone", "earthquake",
        "tornado", "lightning", "heal", "barbarian hut", "furnace", "goblin hut"
    ], "test cards_by_type failed"

    assert cards_by_cost(match(["what", "cards", "cost", "_", "elixir"], ["what", "cards", "cost", "1", "elixir"])) == [
        "ice spirit", "skeletons", "electro spirit", "fire spirit", "goblins", "bomber", "spear goblins", "bats", "zap", "giant snowball"
    ], "test cards_by_cost failed"

    assert average_elixir_cost(match(["What", "is", "the", "average", "elixir", "cost", "for", "cards", "_"], ["What", "is", "the", "average", "elixir", "cost", "for", "cards", "skeletons", "ice spirit"])) == [
        "1.0"
    ], "test average_elixir_cost failed"

print("All tests passed!")



print("All tests passed!")
