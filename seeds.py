from ADT import Game
# Add all the games,then we can export it into the main
def getGames():
    return games
games = [
        # Action
    Game("Cyberpunk 2077", 2999, ["Action"], 9, 1),
    Game("Grand Theft Auto V", 999, ["Action"], 9, 2),
    Game("The Last Of Us 2", 3499, ["Action"], 8, 3),
    Game("Ghost Of Tsushima", 3299, ["Action"], 9, 4),
    Game("Control", 1999, ["Action"], 8, 5),
    Game("God of War Ragnarök", 4999, ["Action"], 8, 6),

    # Free To Play
    Game("The First Descendant", 0, ["Free To Play"], 7, 7),
    Game("Destiny 2", 0, ["Free To Play"], 8, 8),
    Game("Warframe", 0, ["Free To Play"], 9, 9),
    Game("Genshin Impact", 0, ["Free To Play"], 9, 10),
    Game("Honkai Star Rail", 0, ["Free To Play"], 8, 11),

    # Indie
    Game("A Plague Tale: Innocence", 1499, ["Indie"], 9, 12),
    Game("It Takes 2", 2499, ["Indie"], 10, 13),
    Game("Hellblade: Senua's Sacrifice", 1299, ["Indie"], 9, 14),
    Game("Omori", 699, ["Indie"], 9, 15),

    # Multiplayer
    Game("Valorant", 0, ["Multiplayer"], 9, 16),
    Game("Counter Strike 2", 0, ["Multiplayer"], 8, 17),
    Game("League Of Legends", 0, ["Multiplayer"], 9, 18),
    Game("BattleField 1", 2000, ["Multiplayer"], 9, 19),
    Game("Call Of Duty : Modern Warfare 2", 2500, ["Multiplayer"], 7, 20),
    Game("Apex Legends", 0, ["Multiplayer"], 8, 21),
    Game("Players Unknown Battlegrounds", 0, ["Multiplayer"], 9, 22),

    Game("Horizon Forbidden West", 3599, ["Adventure"], 10, 23),
    Game("Detroit:Become Human", 2599, ["Adventure"], 8, 24),
    Game("Subnautica", 1599, ["Adventure"], 9, 25),
    Game("Uncharted : Legacy Of Thieves", 2099, ["Adventure"], 9, 26),
    Game("Red Dead Redemption 2", 1099, ["Adventure"], 10, 27),

    Game("EAFC 25", 3599, ["Sports"], 3, 28),
    Game("F124", 599, ["Sports"], 4, 29),
    Game("Forza Horizon 5", 1899, ["Sports"], 8, 30),
    Game("NFS Unbound", 1799, ["Sports"], 5, 31),
    Game("NBA 2k25", 2899, ["Sports"], 6, 32),

    Game("Baldur's Gate 3", 3099, ["RPG"], 9, 33),
    Game("Witcher 3", 1799, ["RPG"], 10, 34),
    Game("Diablo IV", 4099, ["RPG"], 4, 35),
    Game("Elden Ring", 3099, ["RPG"], 9, 36),
    Game("The Elder Scrolls V:Skyrim", 999, ["RPG"], 8, 37),

]
