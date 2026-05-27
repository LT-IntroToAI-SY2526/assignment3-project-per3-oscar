from typing import List, Tuple

cards_db: List[Tuple[str, str, int, List[str]]] = [
    (
        "common", #rarity
        "tower troop", #type
        0, #elixir count
        [
            "tower princess", #cards
        ],
    ),
    (
        "common",
        "troop", 
        1,
        [
            "ice spirit",
            "skeletons",
            "electro spirit",
            "fire spirit",
        ],
    ),
    (
        "common",
        "troop",
        2,
        [
            "goblins",
            "bomber",
            "spear goblins",
            "bats",
            "berserker",
        ],
    ),
    (
        "common",
        "spell",
        2,
        [
            "zap",
            "giant snowball",
        ],
    ),
    (
        "common",
        "troop",
        3,
        [
            "knight",
            "archers",
            "minions",
            "goblin gang",
            "skeleton barrel",
            "firecracker",
        ],
    ),
    (
        "common",
        "spell",
        3,
        [
            "arrows",
            "royal delivery",
        ],
    ),
    (
        "common",
        "building",
        3,
        [
            "cannon",
        ],
    ),
    (
        "common",
        "troop",
        4,
        [
            "skeleton dragons",
        ],
    ),
    (
        "common",
        "building",
        4,
        [
            "tesla",
            "mortar",
        ],
    ),
    (
        "common",
        "troop",
        5,
        [
            "barbarians",
            "minion horde",
            "rascals",
        ],
    ),
    (
        "common",
        "troop",
        6,
        [
            "elite barbarians",
            "royal giant",
        ],
    ),
    (
        "common",
        "troop",
        7,
        [
            "royal recruits",
        ],
    ),
    (
        "rare",
        "troop",
        1,
        [
            "heal spirit",
        ],
    ),
    (
        "rare",
        "troop",
        2,
        [
            "ice golem",
            "suspicious bush",
        ],
    ),
    (
        "rare",
        "troop",
        3,
        [
            "mega minion",
            "dart goblin",
            "elixir golem",
        ],
    ),
    (
        "rare",
        "building",
        3,
        [
            "tombstone",
        ],
    ),
    (
        "rare",
        "spell",
        3,
        [
            "earthquake",
        ],
    ),
    (
        "rare",
        "troop",
        4,
        [
            "valkyrie",
            "musketeer",
            "mini pekka",
            "hog rider",
            "battle ram",
            "zappies",
            "flying machine",
            "battle healer",
            "goblin demolisher",
            "furnace",
        ],
    ),
    (
        "rare",
        "building",
        4,
        [
            "bomb tower",
            "goblin cage",
            "goblin hut",
        ],
    ),
    (
        "rare",
        "spell",
        4,
        [
            "fireball",
        ],
    ),
    (
        "rare",
        "troop",
        5,
        [
            "giant",
            "wizard",
            "royal hogs",
        ],
    ),
    (
        "rare",
        "building",
        5,
        [
            "inferno tower",
        ],
    ),
    (
        "rare",
        "building",
        6,
        [
            "elixir collector",
        ],
    ),
    (
        "rare",
        "spell",
        6,
        [
            "rocket",
        ],
    ),
    (
        "rare",
        "building",
        7,
        [
            "barbarian hut",
        ],
    ),
    (
        "rare",
        "troop",
        9,
        [
            "three musketeers",
        ],
    ),
    (
        "epic", 
        "tower troop", 
        0, 
        [
            "cannoneer",
        ],
    ),
    (
        "epic",
        "troop",
        2,
        [
            "wall breakers",
        ],
    ),
    (
        "epic",
        "spell",
        2,
        [
            "rage",
            "barbarian barrel",
            "goblin curse",
        ],
    ),
    (
        "epic",
        "troop",
        3,
        [
            "skeleton army",
            "guards",
        ],
    ),
    (
        "epic",
        "spell",
        3,
        [
            "goblin barrel",
            "tornado",
            "clone",
            "void",
            "vines",
        ],
    ),
    (
        "epic",
        "troop",
        4,
        [
            "baby dragon",
            "dark prince",
            "hunter",
            "rune giant",
        ],
    ),
    (
        "epic",
        "building",
        4,
        [
            "goblin drill",
        ],
    ),
    (
        "epic",
        "spell",
        4,
        [
            "freeze",
            "poison",
        ],
    ),
    (
        "epic",
        "troop",
        5,
        [
            "balloon",
            "witch",
            "prince",
            "bowler",
            "executioner",
            "cannon cart",
            "electro dragon",
        ],
    ),
    (
        "epic",
        "troop",
        6,
        [
            "giant skeleton",
            "goblin giant",
        ],
    ),
    (
        "epic",
        "spell",
        6,
        [
            "lightning",
        ],
    ),
    (
        "epic",
        "building",
        6,
        [
            "x-bow",
        ],
    ),
    (
        "epic",
        "troop",
        7,
        [
            "pekka",
            "electro giant",
        ],
    ),
    (
        "epic",
        "troop",
        8,
        [
            "golem",
        ],
    ),
    #
    #
    # EVERYTHING BELOW IS NEW!!!!!!!!
    #
    #
    (
        "legendary", 
        "tower troop", 
        0, 
        [
            "dagger duchess",
        ],
    ),
     (
        "legendary", 
        "tower troop", 
        0, 
        [
            "royal chef",
        ],
    ),
    (
        "legendary",
        "spell",
        2,
        [
            "log",
        ],
    ),
    (
        "legendary",
        "troop",
        3,
        [
            "ice wizard",
            "princess",
            "miner",
            "bandit",
            "royal ghost",
            "fisherman",
        ],
    ),
    (
        "legendary",
        "troop",
        4,
        [
            "lumberjack",
            "inferno dragon",
            "electro wizard",
            "night witch",
            "magic archer",
            "mother witch",
            "phoenix",
        ],
    ),
    (
        "legendary",
        "troop",
        5,
        [
            "goblin machine",
            "ram rider",
        ],
    ),
    (
        "legendary",
        "spell",
        5,
        [
            "graveyard",
        ],
    ),
    (
        "legendary",
        "troop",
        6,
        [
            "sparky",
            "spirit empress",
        ],
    ),
    (
        "legendary",
        "troop",
        7,
        [
            "lavahound",
            "mega knight",        
        ],
    ),
    (
        "champion",
        "troop",
        3,
        [
            "little prince",
        ],
    ),
    (
        "champion",
        "troop",
        4,
        [
            "mighty miner",
            "skeleton king",
            "golden knight"  ,          
        ],
    ),
    (
        "champion",
        "troop",
        5,
        [
            "archer queen",
            "monk",
            "goblinstein",
        ],
    ),
    (
        "champion",
        "troop",
        6,
        [
            "boss bandit",
        ],
    ),
    (
        "evolution",
        "troop",
        1,
        [
            "skeletons",
            "ice spirit",
        ],
    ),
    (
        "evolution",
        "troop",
        2,
        [
            "bomber",
            "bats",
            "wall breakers",
        ],
    ),
    (
        "evolution",
        "spell",
        2,
        [
            "zap",
            "giant snowball",
        ],
    ),
    (
        "evolution",
        "troop",
        3,
        [
            "knight",
            "archers",
            "skeleton army",
            "skeleton barrel",
            "dart goblin",
            "firecracker",
            "royal ghost",
        ],
    ),
    (
        "evolution",
        "spell",
        3,
        [
            "goblin barrel",
        ],
    ),
    (
        "evolution",
        "building",
        3,
        [
            "cannon",
        ],
    ),
    (
        "evolution",
        "troop",
        4,
        [
            "musketeer",
            "valkyrie",
            "battle ram",
            "baby dragon",
            "furnace",
            "hunter",
            "inferno dragon",
            "lumberjack",
        ],
    ),
    (
        "evolution",
        "building",
        4,
        [
            "mortar",
            "tesla",
            "goblin drill",
        ],
    ),
    (
        "evolution",
        "troop",
        5,
        [
            "barbarians",
            "wizard",
            "witch",
            "royal hogs",
            "minion horde",
            "electro dragon",
            "executioner",
        ],
    ),
    (
        "evolution",
        "troop",
        6,
        [
            "royal giant",
            "goblin giant",
        ],
    ),
    (
        "evolution",
        "troop",
        6,
        [
            "pekka",
            "royal recruits",
            "mega knight",
        ],
    )
    
]