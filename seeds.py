from ADT import Game
# Add all the games,then we can export it into the main
def getGames():
    return games

games = [
        # Action
    Game("Cyberpunk 2077", 2999, ["Action","Adventure","RPG"], 9, 1,{"LigmaMaster":"Amazing game. This sure has a great story","Linkmon99":"I really love the furturistic setting of the game"}),
    Game("Grand Theft Auto V", 999, ["Action","Adventure","Multiplayer"], 9, 2,{"St.Kkpop":"This game is very good, although the machine configuration is slightly low FPS, but when setting is very smooth. In the end, this game is great, top -notch graphics, true character, 100 points","toN.A.T.O":"I recommend this game it is very fun. Idk about the online mode tho, I haven't played it"}),
    Game("The Last Of Us 2", 3499, ["Action","Adventure"], 6, 3,{"Luis Rosario":"Copied from another review because this is 100% accurate. Pushing a political agenda. I only played the first maybe 30 minutes like 25 was all cut scenes and was so disappointed that I went online to check reviews to see if it was just me but no, it seems everyone else agree with this review and its true. Sad because I loved the first game, but the second part its just garbage.","Trevor Thomas":"I was excited until I played the game it sucks and this was well said"}),
    Game("Ghost Of Tsushima DIRECTOR'S CUT", 3299, ["Action","Adventure"], 9, 4,{"trip2017":"Great game. Great graphics and impressive melee gameplay. Can’t skip cutscenes so keep that in mind or just don’t be impatient.","Autistic Master":"Ghost of Tsushima is probably one of the best games that I've ever played. The story is fantastic, the graphics are even better and the combat is immaculate. I recommend strongly if you have a good pc and a 2k oled monitor."}),
    Game("Control Ultimate Edition", 1999, ["Action","Adventure","RPG"], 8, 5,{"TheGrievenge":"Mystic/ horror atmosphere without any jumpscares. Fight mechanics are good but not the reason I like this game. Its more about said atmosphere and always being on the edge, without having to worry for some jumpscare bs. The storyline is nice too. As an SCP fan my expectations on the supernatural items and co. fell a bit short, but if I wouldn't have known SCPs beforehand, this would definitely have been good enough to get into SCPs after playing it.","Amogus":"Great game that explores the idea of trying to change an institution from within, and how that institution changes you in turn."}),
    Game("God of War Ragnarök", 4999, ["Action","Adventure"], 8, 6,{"Omaha":"Bigger and better than before although it suffers a bit from pacing issues. All in all, its a great single player experience.","Jinn":"The days of searching for Spider-Man PC, Uncharted PC, Ghost of Tsushima PC, God of War PC a million times are finally over."}),

    # Free To Play
    Game("The First Descendant", 0, ["Free To Play","Multiplayer","Action"], 7, 7,{"Bensley":"Warframe but made by Nexxon","Bod Dock":"The Micro transactions make this game bad"}),
    Game("Destiny 2", 0, ["Free To Play","Multiplayer","Action"], 8, 8,{"chop or be chopped":"This is the greatest, and also the worst game i have ever played. There's just no end to it.","AbstractArtemis":"Over 1200+ hours wasted on Destiny 2 across 3 different platforms. It was an addiction and at many times, and also a joy. Was it worth it?"}),
    Game("Warframe", 0, ["Free To Play","Multiplayer","Action"], 9, 9,{"Khasuri":"fun and addicting game but stay FAAAAAR away from the chat features and jobless freaks who moderate it.","Its_Darkar":"this game is like cocaine but worse since you can at least run out of cocaine"}),
    Game("Genshin Impact", 0, ["Free To Play","RPG","Multiplayer"], 9, 10,{"Erie":"I spend countless hours of my useless life in this game","Yun":"I blame the game"}),
    Game("Honkai Star Rail", 0, ["Free To Play","RPG"], 8, 11,{"Nao":"The game has so many beautiful characters","Ayane":"This game is really good but i wish it was Open world"}),

    # Indie
    Game("A Plague Tale: Innocence", 1499, ["Indie","Adventure"], 9, 12,{"TheBunnyKiller":"The game and graphics is amazing, started out pretty normal and fun but after 10-15 min damm they just threw u in the story and bum u are stunned!! the story was amazing, easy, a little challenging but fun. having all of these thoughts like what the hell is going on but the same time im freaking ready for whatever happens, come at me!! 10/10","JigsawYeager":"Monsters are those things to which we have never given a name."}),
    Game("It Takes 2", 2499, ["Indie","Multiplayer"], 10, 13,{"Caragolaire":"It was an amazing game and if you play it with the proper person, it is the greatest game ever.","I Organize Illegal Bug Fights":"Played with GF, we broke up, now i'll never finish. Good game tho 10/10."}),
    Game("Hellblade: Senua's Sacrifice", 1299, ["Indie","Action"], 9, 14,{"Yoshii":"9/10 it's mental illness simulator and a bit of combat. I enjoy the story and the puzzle is the only thing that keep me sane, the combat is a bit disappointing because this is a story focus game tho this game worth the time also do your sanity check after playing.","Mr.Fish":"This isn't a video game. It's an interactive panic attack.Play alone in the dark with headphones, and don't feel ashamed if you have to step away and take a break."}),
    Game("Omori", 699, ["Indie","RPG"], 9, 15,{"Yashieee":"I've been recomended this game a lot and it certainly didn't disappont","kummyache":"i got this game tattooed on me. i will never love a game the way i loved this painful experience. i want to play it again but it hurt me so badly that i don't know if i can go through the joys and sufferings a second time - but god, is this game brilliant. what an experience."}),

    # Multiplayer
    Game("Valorant", 0, ["Multiplayer","Action"], 9, 16,{"V1CHU":"Amazing game but never solo queue","Elite Gamer":"You'll neverclimb rank with all these braindead teammates"}),
    Game("Counter Strike 2", 0, ["Multiplayer","Action"], 8, 17,{"P RAGEan":"I sucked at Valo but this seems more fitting for me","S1MPLE":"The game still has a lot of bugs"}),
    Game("League Of Legends", 0, ["Multiplayer","Action"], 9, 18,{"Nikker":"The game is free but it costs your meantal health","I Miss Her":"Now i know why she left me"}),
    Game("BattleField 1", 2000, ["Multiplayer"], 9, 19, {"Anon9201": "The game is really good, but the devs doesn't care about banning hackers, peoples should not buy this product since it's nearly unplayable, BFV is in a even worse state.", "Pandoro ":"The graphics are amazing and the gameplay is really fun, but the game is plagued by hackers."}),
    Game("Call Of Duty : Modern Warfare 2", 2500, ["Multiplayer","Action"], 7, 20, {"HolyKnight": "Hands down one of the best call of duty's ever made. I know I only have 9 hours, but this is brilliant, and it is so much better than the reboot.", "FevreDream ":"The campaign is really good, but the multiplayer is a bit too chaotic for my taste."}),
    Game("Apex Legends", 0, ["Multiplayer"], 8, 21, {"Posedion11": "The champion of Battle Royales.", "RandomGUy ":"I love the fast-paced action and the variety of legends to choose from."}),
    Game("Players Unknown Battlegrounds", 0, ["Multiplayer","Free To Play"], 9, 22, {"RedBaron": "This is the best possible praise for this great battle-royale-genre shooter. What a pity there are so many bugs, mad vehicle physics and occasional cheaters.", "SoulfulJoe ":"The game is a bit dated now, but it's still a lot of fun."}),

    # Adventure 
    Game("Horizon Forbidden West", 3599, ["Adventure","Action"], 10, 23, {"Alienatic": "The new and updated machines are pretty cool and it's generally good fun to figure out how to fight them. And just as in the first game, the visuals are just stunning.", "MissileMan ":"The story is a bit weak and the gameplay is repetitive, but the visuals are amazing."}),
    Game("Detroit:Become Human", 2599, ["Adventure"], 8, 24, {"The_Silencer": "Arguably the best 'choices matter' game out there. Great all round. Brilliant voice acting, great branching story, tight combat sequences. Can't wait for their next game.", "KindKoala ":"The story is a bit predictable, but the characters are well-developed and the acting is superb."}),
    Game("Subnautica", 1599, ["Adventure"], 9, 25, {"USA00t": "Best survival game ever made. Well balanced. The tech tree feels natural and encourages exploration to find resources. The game feels challenging and never too frustrating.", "TeeVee4 ":"The game is a bit scary at times, but the atmosphere is really immersive."}),
    Game("Uncharted : Legacy Of Thieves", 2099, ["Adventure","Action"], 9, 26, {"Tristesse": "Overall, the story feels very safe, it doesn't take many risks, and there aren't many surprises (excluding the fact that Nathan now has a brother he never knew about).", "Lucky11 ":"The graphics are amazing and the gameplay is smooth, but the story is a bit predictable."}),
    Game("Red Dead Redemption 2", 1099, ["Adventure","Action"], 10, 27, {"Bitingbull": "I haven't yet completed the read dead and I'm still on chapter 2 but from what I've played so far The game is great with a story being set up from the start, I love the detail and the world.", "BeastMaster420 ":"The world is incredibly detailed and the story is very engaging, but the game can be a bit slow at times."}),

    # Sports
    Game("EAFC 25", 3599, ["Sports"], 3, 28, {"CR7SUIIIIII": "EA SPORTS FC™ 25 ... Horrible! Crashes all the time on career mode. The game ends, the other game results are displayed, and the game just never loads back.", "AnthonyTheGoat":"The game is a bit buggy, but the gameplay is still fun."}),
    Game("F124", 599, ["Sports"], 4, 29, {"Dudududu...MaxVerstoopen": "The game is great, but the AI is a bit too easy. It's easy to win races and the game is not challenging enough.", "BatteryVoltas ":"The game is a bit too arcadey, but it's still a lot of fun."}), 
    Game("Forza Horizon 5", 1899, ["Sports","Adventure"], 8, 30, {"TheWidow": "The best racing game ever made. The graphics are amazing, the gameplay is smooth, and the world is huge. The game is a must-have for any racing fan.", "RazerBlayd ":"The game is a bit too focused on open-world exploration, but the racing is still excellent."}),
    Game("NFS Unbound", 1799, ["Sports"], 5, 31, {"Silverbullets": "The game is pretty good, but the graphics are a bit too cartoonish. The game is a bit too arcadey, but it's still fun to play.", "Judithrex ":"The game is a bit too focused on style over substance, but it's still a fun arcade racer."}),
    Game("NBA 2k25", 2899, ["Sports"], 6, 32, {"LeBronJames": "The game is fun to play, but the microtransactions are a bit too much. The game is a bit too grindy, but it's still a good basketball game.", "Sk8erboi ":"The game is a bit too focused on microtransactions, but the gameplay is still fun."}),

    # RPG
    Game("Baldur's Gate 3", 3099, ["RPG","Adventure"], 9, 33, {"Bloodstone": "I've been playing this game for over 100 hours and I'm still not done! The game is so good, I can't put it down.", "Needlepoint ":"The game is a bit buggy, but the story is so good that it's easy to overlook the flaws."}),
    Game("Witcher 3", 1799, ["RPG","Action"], 10, 34, {"DavyJones": "The Witcher 3 is a masterpiece. The story is amazing, the characters are well-developed, and the world is beautiful.", "Esmereldaxx ":"The game is a bit long, but the story is so good that it's easy to get lost in the world."}),
    Game("Diablo IV", 4099, ["RPG","Action"], 4, 35, {"SlayRide": "The game is fun, but it's too grindy. The game is too repetitive, and the endgame is a bit boring.", "Thingymagic ":"The game is a bit too focused on loot grinding, but the combat is still fun."}),
    Game("Elden Ring", 3099, ["RPG","Action"], 9, 36, {"CaptainAwesome": "The game is challenging, but rewarding. The world is vast and beautiful, and the combat is intense and exciting.", "TotalGamer ":"The game is incredibly difficult, but the sense of accomplishment when you finally beat a boss is amazing."}),
    Game("The Elder Scrolls V:Skyrim", 999, ["RPG","Adventure"], 8, 37, {"CrissCross": "The game is a classic for a reason. The world is huge, the characters are interesting, and the story is compelling.", "TrollQueen ":"The game is a bit dated now, but it's still a lot of fun to explore the world and create your own character."}),

]
