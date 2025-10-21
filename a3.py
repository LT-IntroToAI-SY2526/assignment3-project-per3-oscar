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

def cards_by_type(matches: List[str]) -> List[List[str]]:
    troop = matches[0]
    result = []

    for cards in cards_db:
        if get_type(cards) == troop:
            for card in get_cards(cards):
                result.append([card])
    return result

def cards_by_cost(matches: List[str]) -> List[List[str]]:
    troop = int(matches[0])
    result = []

    for cards in cards_db:
        if get_cost(cards) == troop:
            for card in get_cards(cards):
                result.append([card])
    return result

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

def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    print("Welcome to the Album database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")

if __name__ == "__main__":

    assert rarity_by_type(match(["what", "rarity", "does", "the", "_", "type", "have"], ["what", "rarity", "does", "the", "building", "type", "have"])) == [
        "common", "common", "rare", "rare", "rare", "rare", "rare", "epic", "epic"
    ], "test rarity_by_type failed"

    assert rarity_by_cost(match(["what", "rarity", "costs", "_", "elixir"], ["what", "rarity", "costs", "6", "elixir"])) == [
        "common", "rare", "rare", "epic", "epic", "epic", "legendary", "champion"
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
        2, 2, 3, 3, 4, 4, 4, 5, 6, 6, 6, 7, 8
    ], "test cost_by_rarity failed"

    assert cost_by_type(match(["how", "much", "does", "a", "_", "type", "card", "cost"], ["how", "much", "does", "a", "building", "type", "card", "cost"])) == [
        3, 4, 3, 4, 5, 6, 7, 4, 6
    ], "test cost_by_type failed"

    assert cost_by_cards(match(["how", "much", "does", "%", "cost"], ["how", "much", "does", "skeletons", "cost"])) == [
        1
    ], "test cost_by_cards failed"

    assert cards_by_rarity(match(["what", "cards", "are", "_"], ["what", "cards", "are", "champion"])) == [
        ["little prince"],
        ["mighty miner", "skeleton king", "golden knight"],
        ["archer queen", "monk", "goblinstein"],
        ["boss bandit"]
    ], "test cards_by_rarity failed"

    assert cards_by_type(match(["what", "cards", "are", "the", "_", "type"], ["what", "cards", "are", "the", "spell", "type"])) == [
        ["zap"], ["giant snowball"],
        ["arrows"], ["royal delivery"],
        ["earthquake"],
        ["fireball"],
        ["rocket"],
        ["rage"], ["barbarian barrel"], ["goblin curse"],
        ["goblin barrel"], ["tornado"], ["clone"], ["void"], ["vines"],
        ["freeze"], ["poison"],
        ["lightning"],
        ["log"],
        ["graveyard"],
    ], "test cards_by_type failed"

    assert cards_by_cost(match(["what", "cards", "cost", "_", "elixir"], ["what", "cards", "cost", "1", "elixir"])) == [
        ["ice spirit"], ["skeletons"], ["electro spirit"], ["fire spirit"], ["heal spirit"],
    ], "test cards_by_cost failed"

print("All tests passed!")

if __name__ == "__main__":
    query_loop()
    
query_loop
