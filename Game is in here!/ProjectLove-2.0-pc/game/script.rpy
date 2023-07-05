# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define me = Character('Me', color='#000080')
define bird = Character('Corvo', color='#6ececd')
define catboy = Character('Elliot', color='#2d532f')
define octolady = Character(' Aaliyah', color='#8b2650')
define unknownbird = Character('???', color='#6ececd')
define unknowncatboy = Character('???', color='#2d532f')
define unknownoctolady = Character('???', color='#8b2650')
define birdinspirit = Character('  Corvo (in spirit)', color='#6ececd', size=35)
define gamedev = Character('  Game Dev')


image bg staircase:
    "bg staircase.png"
    zoom 0.45

image bg blackout:
    "bg blackout.png"
    zoom 1.2

image bg generic:
    "bg generic.png"
    zoom 0.55

image bg alleyway:
    "bg alleyway.png"
    zoom 0.9

image bg pond:
    "bg pond.png"
    zoom 0.9

image bird normal:
    "bird normal.png"
    zoom 0.25

image bird mock:
    "bird mock.png"
    zoom 0.25

image catboy normal:
    "catboy normal.png"
    zoom 0.25

image catboy blush:
    "catboy blush.png"
    zoom 0.25

image catboy angry:
    "catboy angry.png"
    zoom 0.25

image catboy happy:
    "catboy happy.png"
    zoom 0.25

image catboy sad:
    "catboy sad.png"
    zoom 0.25

image octolady normal:
    "octolady normal.png"
    zoom 0.145

image octolady happy:
    "octolady happy.png"
    zoom 0.145

image octolady angry:
    "octolady angry.png"
    zoom 0.145

image octolady blush:
    "octolady blush.png"
    zoom 0.145

image octolady sad:
    "octolady sad.png"
    zoom 0.145

# The game starts here.

label start:
    $ Haslooped = False
    $ YouFail = False
    play music "audio/Ethereal_Harmony.mp3"
    scene bg staircase
    "Flowers? Check. Those cheesy heart shaped boxes filled with chocolates you see in every romance movie? Check. Looks like I've got everything for my date with Vanessa."
    "I still have no idea how I banked the hottest chick in class, but I'm not complaining. Her long hair, her beautiful eyes and her very big, firm  and well rounded..."
    "Personality"
    "To think she is waiting in the park for me just up ahead. Man am I nervous. I've been crushing on her ever since the start of the year."
    "I absolutely, without a doubt, can't afford to screw this up. I need her to think I'm cool and laid back. Not some stinky basement dweller playing games all day."
    "I mean, I am, but she doesn't know that yet so I might actually have a chance."
    "Alright, just gotta check the time and- OH NO I AM RUNNING LATE!"
    "Oh man I'm running late! I guess internally monologing does take up a lot of time. I better get going and fast!"
    "I just have to walk up these stairs"
    menu: 
        "I just have to walk up these stairs"
        "Walk up the stairs":
            "It will be a breeze, just a few more steps and-"
            scene bg blackout
            "Oh no, I misstepped and I can't reach the railing! Man this is going to hurt!"
            jump walkup
        "Go home like a loser":
            jump gohome

label walkup:
    scene bg generic
    "..."
    "Ah man my head feels like it's about to burst. I can barely stand up."
    "..."
    "Hold up a second. Where am I? This doesn't look anything like the park. What happened? I was walking up the stairs a minute ago!"
    "Okay lets recap. I fell down the stairs, blacked out, woke up and now I'm here. There is only 1 logical explanation."
    "Alien. Abduction."
    "They made me trip, picked me up in their spaceship, harvested my organs and dropped me back here."
    show bird normal at top
    "Wait, no. I still have my organs. But how did I get here? It doesn't feel like I was out for long."
    unknownbird "Hello there, little fellow"
    me "A bird? A speaking bird? Since when can birds speak?"
    unknownbird "My my, such an odd creature! I've never seen anyone like you before"
    me "What are you?"
    bird "I think it's better if you ask me WHO I am. The name's Corvo. I brought you here to fulfill your destiny!"
    me "What destiny? My destiny was to have a date with my smoking hot date!"
    show bird mock at top
    bird "Do you really think Vanessa would have wanted to go out with such a sad little loser like you? You've got no dating experience!"
    bird "Fwie fwie fwie fwie! Don't make me laugh! But not to fear because I am here! I will guide you and make sure you ace your dates in no time!"
    show bird normal at top
    me "What? What dates? I just want to go on my date with Vanessa!"
    bird "You see, this area is filled with cute bachelors and bachelorettes looking for love. You should practice romancing them."
    show bird mock at top
    bird "If you do that succesfully, you might have a shot with Vanessa. Fwie fwie fwie!"
    show bird normal at top
    me "How do I do that?"
    bird "Talk to them, my little fellow, make yourself out to be interesting, give them compliments to increase their love meter."
    bird "Be warned though, answering questions wrong will make the lovemeter go down."
    show bird mock at top
    bird "I think it's time to send you out to the wild now, you can do it little fellow. Or not. fwie fwie fwie."
    show bird normal at top
    bird "Regardless, I'll help you if you mess up."
    bird "There are two paths you can choose. You can choose to go towards the city or you can go to the pond in the park."
    show bird mock at top
    bird "Don't worry, in both area's are hotties who are single and ready to mingle."
    show bird normal at top
    bird "You can go to the city, or the pond. Where would you like to go?"
    menu:
        bird "You can go to the city, or the pond. Where would you like to go?"
        "Go to the City":
            hide bird
            "I can see some buildings up ahead. They don't seem to be the ones that are around here in the normal world though. Regardless, I might find a way back."
            "Hell, if that weird bird is right, I might even get to bang some chicks!"
            gamedev "(Authors note: No chicks are going to banged)"
            jump city
        "Go to the Pond":
            hide bird
            jump pond

label gohome:
    "Ah forget it. I'd rather be with my waifus. Hatsune Miku i'm coming home baby~!"
    gamedev "You go home to make out with your body pillow-- seriously what is wrong with you"
    menu:
        gamedev "You go home to make out with your body pillow-- seriously what is wrong with you"
        "Im a loser, take me back to the beginning":
            jump start

label city:
    scene bg alleyway
    "The closer I get to the city, the sketchier it looks."
    "This doesn't seem too good of a neighborhood, I have to watch my back or else I might get into trouble."
    "I can't afford to be mugged right now. I need this money to pay for rent, food the electricity bill!"
    "Ah, who am I kidding? I live at home with my parents."
    "Honestly, I do not feel safe here. This place has such a bad vibe to it. It feels like I could be kidnapped any seco-"
    me "Wow dude let go off me!"
    show catboy normal at top
    unknowncatboy "This is a robbery! Give me your money, phone and wallet. MEOW! I don't have all day!"
    me "Wha, what's happening??"
    unknowncatboy "You're being robbed, you idiot. You give me your stuff? No one gets hurt. Got it?"
    menu:
        unknowncatboy "You're being robbed, you idiot. You give me your stuff? No one gets hurt. Got it?"
        "Okay fine fine, take my money!":
            jump GOmoney
        "Flirt with him":
            jump catboyflirt


label GOmoney:
    hide catboy
    "Yeah thats right, now beat it!"
    "Shit, there goes my money"
    menu:
        "Shit, there goes my money"
        "Oops, i want to flirt with him instead":
            jump catboyflirt

label catboyflirt:
    show catboy normal at top
    me "Robbed? By you? I'm not being robbed. You're way too adorable to rob anyone, young lady."
    show catboy angry at top
    unknowncatboy "Young lady? YOUNG LADY! YOU THINK I'M A YOUNG LADY!"
    me "Well, you don't exactly look 57 now, do you?"
    unknowncatboy "That's not the part I'm talking about you moron! Can't you see I'm clearly a man!"
    me "Now now, there is no need to get angry young lady."
    unknowncatboy "STOP CALLING ME A YOUNG LADY."
    me "Well, I don't quite have your name now, do I?"
    show catboy normal at top
    unknowncatboy "You're being robbed. Why would I tell you my name?"
    unknowncatboy "What are you gonna ask for next? My bank account details? Social security number? Marital status?"
    me "Well now that you mention it, I do wanna know why a cutie like you is roaming the streets robbing people without a partner in crime."
    show catboy blush at top
    unknowncatboy "Wha, what are you even talking about?"
    "Quick, he's distracted I can get out from under his claws"
    show catboy angry at top
    unknowncatboy "Where do you think you're going! Don't you dare meowve!"
    me "I'll let you rob me if you tell me your name, middle-aged lady!"
    unknowncatboy "Middle-aged? I'm 21! AND STOP CALLING ME A LADY. I AM NOT A LADY. I AM 120 POUNDS OF PURE MALE MASCULINE MEOWSCLE!"
    show catboy normal at top
    catboy "You know what? Fine. My name's Elliot. Can you stop calling me a young lady now?"
    me "See, I knew a cutie like you would have a fitting name."
    show catboy blush at top
    catboy "..."
    show catboy normal at top
    me "You seem quite hurt. How'd you end up here?"
    catboy "I don't wanna talk about it."
    me "Why? What's wrong?"
    catboy "I said I don't wanna talk about it."
    me "Well, are you gonna be fine if I just leave you here?"
    show catboy angry at top
    catboy "Don't you dare move a finger! You still haven't given me your money!"
    me "Damn, not even asking me out for a drink first. You seem like quite the golddigger Elliot"
    show catboy normal at top
    catboy "Are you expecting your robber to pay for your drinks? In what fantasy world do you live?"
    me "I could ask you the same. But how about this? I take you out for a date to get some food and you don't rob me of everything I have? Does that sound like a good deal to you?"
    catboy "Are you seriously asking your robber out on a date right meow?"
    me "Well, do you have anything better to do?"
    show catboy happy at top
    catboy "As long as you're paying for my food and drinks. I have nothing to lose I guess."
    me "Great! It's a date then!"
    show catboy normal at top
    catboy "Hmmmm. Fine."
    hide catboy
    show text "{size=+50}{color=#000000}One walk to the park later...{/color}" at truecenter
    with dissolve
    pause 3
    hide text
    with dissolve
    show bg generic

label catboyflirt2:
    "You know, 30 minutes ago when I was walking through the city, I didn't expect to be going on a date with an anthropomorphic animal, yet here we are."
    "Sitting in the park, having a picnic and eating to our hearts' content."
    "We got some fish from a local fish store here. It wasn't exactly cheap, but it was cheaper than just handing over my wallet, phone, and money."
    "Funny how a fantasy world takes real-world currency. How convenient is that!"
    "Elliot sure does seem to love the fish. It seems like he hasn't eaten in days. I'm kind of concerned for him."
    show catboy happy at top
    catboy "These fishies are DELICIOUS! I can't believe we have so many of these."
    show catboy normal at top
    menu:
        catboy "These fishies are DELICIOUS! I can't believe we have so many of these."
        "Share your fish":
            jump Share
        "Dont Share your fish":
            jump NoShare


label NoShare:
    hide catboy
    catboy "HEY, DON'T HOG THEM ALL FOR YOURSELF!"
    me "OW OW OKAY NO NEED TO SCRATCH"
    birdinspirit "Smooth, very smooth. Let's roll that one back"
    menu:
        birdinspirit "Smooth, very smooth. Let's roll that one back"
        "Oops, sorry you're right":
            jump catboyflirt2

label Share:
    show catboy happy at top
    me "Yeah, they seem really good. You take as many as you want."
    catboy "Now THAT'S what I'm talking about!"
    show catboy normal at top
    me "So why were you robbing people in that back alley?"
    catboy "That thought has not at all crossed your mind until a second ago?"
    me "In all fairness, I was wondering why such a cute kitty cat was roaming the streets but I never got to ask you until now."
    catboy "Well, it's complicated."
    me "I can handle it."
    show catboy angry at top
    catboy "You're quite persistent, aren't you?"
    me "Persistent is my middle name."
    catboy "I've noticed."
    "..."
    show catboy normal at top
    "......"
    ".................................................................................................................................."
    show catboy sad at top
    catboy "I'm homeless, okay. I got kicked out at 18, and ever since I've been trying to get something going, but it's hard."
    me "Oh, I'm sorry for making you say that."
    catboy "It's okay. It's part of who I am. I've been trying to work odd jobs as much as possible, but sometimes there just aren't any, and I have to get money in alternative ways."
    show catboy normal at top
    catboy "Seems like I picked a good target, though. Haven't had the police called on me, and I'm munching on these delicious fishies! I am sorry for trying to rob you, though."
    catboy "I hope we can still be friends and forget about this whole robbing thing."
    me "Yeah, of course. Would be a shame if I let such a cutie slide right past me."
    show catboy blush at top
    catboy "Stop calling me cute! Don't you see the fierce testosterone-rilled man in front of you?"
    show catboy normal at top
    me "Is the fierce testosterone-rilled man in the room with us right now?"
    catboy "Very funny..."
    me "Thank you, I try."
    catboy "You do know that you're supposed to be nice to your date, right? You don't seem to be too bright on the dating front."
    me "Oh, I know, I just think you're cute when you're annoyed."
    catboy "I'm beginning to think you're a lost cause."
    me "Oh, come on, I'm not that terrible."
    catboy "..."
    me "......"
    catboy "..."
    me "Okay, maybe I am that terrible."
    catboy "To be fair, you did get me loads of fishies, so I guess you're not all that terrible."
    me "You're making me feel like your personal Santa Claus."
    catboy "It's because you are, and I don't mind it one bit."
    me "Well then, how about you sit on Santa's lap?"
    show catboy angry at top
    catboy "Do you think I'm that cheap? You're going to have to take me out more if you want to order me around. Besides, I ate all the fishies. Since they are all gone, I have no reason to stay."
    show catboy normal at top
    me "Are you sure you don't want to stay a little longer?"
    catboy "I have business to take care of, so I think it's best if I leave meow. But if I find you again, I'll gladly let you take me out a second time."
    me 'Am I going to have to bribe you with fish again?'
    catboy "Depends on how badly you want to go on a second date."
    me "Is that a yes?"
    catboy "Well, if a certain sugar babe were to come along with some fish, I see no reason to deny a second date. But since you have none right now, your time's up."
    catboy 'I usually hang out around the city, so if you\'re looking for me, you know where to find me.'

label Share2:
    show catboy normal at top
    catboy "You do want to go out on another date, right?"
    menu:
        catboy "You do want to go out on another date, right?"
        "Yes":
            jump yescatboy
        "No":
            jump nocatboy

label nocatboy:
    hide catboy
    catboy "Ugh, so you're the type of person to just tease anyone huh? Gross.."
    birdinspirit "Way to screw that one up casanova. Here, lets try that again"
    menu:
        birdinspirit "Way to screw that one up casanova. Here, lets try that again"
        "Good idea...":
            jump Share2

label yescatboy:
    show catboy happy at top
    catboy "Yeah, I knew you would! See you then!"
    hide catboy
    "Okay, that went well I think. Atleast I didn't lose all my money."
    "I still don't know why I agreed to go on a date with him, but it was nicer than I expected."
    show bird mock at top
    bird "Fwie Fwie Fwie, how are you doing, young fellow."
    show bird normal at top
    me "What are you doing here, Corvo?"
    bird "I came here to congratulate you on succesfully having your first date."
    show bird mock at top
    bird "Oh, my little socially inept little fellow, growing up so fast."
    show bird normal at top
    me 'Hey!'
    bird "I'm sorry, I'm just very proud of you. Keep going like you're doing now."
    bird "I'll be waiting for you when you finish your second date."
    show bird mock at top
    bird "At this rate, you might have a shot at dating Vanessa!"
    show bird normal at top
    bird "Anyways, it's time for you to continue your search for love, my little fellow. Are you ready?"
    menu:
        bird "Anyways, it's time for you to continue your search for love, my little fellow. Are you ready?"
        "Yes":
            hide bird
            jump Catboydate2

label Catboydate2:
    show bg alleyway
    "It feels like my life has flipped upside down. Yesterday, I got sent to an alternative reality and now I'm suddenly on my way to score a second date with a cute catboy."
    "I'm not exactly minding it, but I still have to find a way to get home."
    "Also, why is fish so expensive? I never really bought fish before, but dating this catboy is killing my wallet! I get that fishing is difficult, but man do I wish I could just give him some cat food."
    "The city doesn't look any better than yesterday. It's dirty, deserted and feels like I'm being watched by both rats and gang members from the shadows."
    "Couldn't Elliot just be homeless in the better part of the city? It would make me feel safer trying to search for him at least. I really can't imagine he makes much money here."
    "At least not in a legal way."
    "Sure, there are a lot of liquor and tobacco stores, but I imagine they don't like hiring homeless people. Elliot looks quite beat up, which probably doesn't help either."
    "The further I walk into the city, the more screaming I hear. I feel bad for anyone who has to live here."
    "Damn, it really sounds like someone is being beaten up ahead. Kind of sounds like a cat is screaming in pain."
    "Cat, screaming in pain. Oh no, oh no no no please don't tell me it's Elliot. Please tell me he is okay."
    "I better hurry and check up on that cat in case it's Elliot. The closer I get the louder and more painful the cries for help sound."
    menu:
        "I better hurry and check up on that cat in case it's Elliot. The closer I get the louder and more painful the cries for help sound."
        "Im gonna run at full speed!":
            jump sprint
        "Actually, im gonna moonwalk over there":
            jump moonwalk

label moonwalk:
    "You moonwalked over there. You might not be fast, but atleast you're stylish! Style over (human?) lives, am I right?"
    birdinspirit "Speed it up casanova. Time is ticking! You could try to run this time instead"
    menu:
        birdinspirit "Speed it up casanova. Time is ticking! You could try to run this time instead"
        "Lame, whatever i guess i'll run then":
            jump sprint

label sprint:
    "You ran over there. You got there quickly!"
    show catboy normal at top
    "No matter how much screaming I heard, nothing could have prepared me for the state I found Elliot in. He was groaning in pain with new wounds on him."
    me 'Elliot, what happened? You look awful!'
    catboy "I'm fine, it's nothing serious. It will heal on its own."
    me "Are you serious? You\'re bleeding badly!"
    catboy "I\'m FINE. I just need to get up and find something to tie around my wounds."
    me "Are you insane? You\'ll make your wounds even bigger and deeper that way. Don\'t move. I\'m going to rip my shirt apart, and I\'ll use the cloth to cover the wound."
    show catboy blush at top
    catboy "You don\'t need to rip your shirt apart..."
    show catboy normal at top
    me "Yeah, but I want to. You\'re in no position to move. Now sit still and let me patch you up."
    catboy "Okay..."
    "..."
    me "There, all done. I would wait with moving until the wounds have fully closed. What happened to you though?"
    catboy "I don't really want to talk about it..."
    me "You can't say that after I find you all beaten up in some back alley! I want you to tell me what happened."
    show catboy sad at top
    catboy "Fine, I tried to rob someone because I was short on cash, but they pulled a knife on me."
    me "You got STABBED?!?"
    catboy "They were too slow for that, but the knife did slice my stomach. The wound isn't too deep, just quite long."
    show catboy normal at top
    me "I told you not to rob people..."
    show catboy angry at top
    catboy "Well, SOME people can't easily get a job, money, or a house, okay? What am I supposed to do? Starve to death? Freeze to death?"
    show catboy normal at top
    me "I get why you do it. There are other ways for you to make money that don't involve robbing people for their cash."
    show catboy angry at top
    catboy "ARE YOU IMPLYING I SHOULD WHORE MYSELF OUT?"
    show catboy normal at top
    me "Not at all! We can try to get you hired in some of these corner stores. Sure, they're awful, but it's safer than trying to rob people!"
    show catboy sad at top
    catboy "No one wants to hire a homeless person. No one wants to help a homeless person."
    me "I\'m helping you right now, aren\'t I?"
    catboy "It's not the same. I appreciate you helping me, but no one has ever done that before."
    show catboy normal at top
    me "Well, if I'm the first, I'll personally make sure I'm not the last."
    catboy "Why do you care so much about helping others?"
    me "No one deserves to live like this, Elliot. You deserve a roof over your head, food on the table, and to not be stabbed in a back alley."
    catboy "What are you? A vile communist?"
    me "If you living in a humane situation makes me a vile communist, then yes, I am."
    catboy "What are you gonna do? Drag me across town until someone hires me? Trust me, I've tried."
    me "You know what? Yeah, I am going to do that. I'll drag you across the world just so I can make sure I don't have to see you bleeding out again."
    show catboy happy at top
    catboy "You'd really do all that just to help me out?"
    show catboy normal at top
    me "Yup! I don't wanna live my life knowing I could have helped someone out of homelessness."
    show catboy blush at top
    catboy "That's very, caring of you."
    show catboy normal at top
    me "I almost forgot! I brought you some fish. I was hoping to ask you out on a second date with them, but I don't think you're able to go anywhere in your current state."
    catboy "I doubt it. But I tell you what, if you give me those fishies now, I'll go on a date with you once I'm better. Deal?"
    me "You just want the fish, don't you?"
    catboy "Well, the fishies are convincing, but I do also want to go out with you. You should come back to visit me in a week; I bet I'll be better!"
    me "Alright, I'll make sure to come back next week. You better not rob anyone until then alright!"
    catboy "Got it boss. No more robbing!"

label sprint2:
    show catboy normal at top
    menu:
        catboy "Got it boss. No more robbing!"
        "Im gonna give Elliot some money to get through the week":
            jump give
        "Im gonna keep my money all to myself":
            jump dontgive

label dontgive:
    hide catboy
    "I didn\'t give Elliot any money. I\'m sure he\'ll be alright. Atleast, that\'s what I tell myself"
    birdinspirit "What, you can't spare change to the homeless? How heartless. lets try that again"
    menu:
        birdinspirit "What, you can't spare change to the homeless? How heartless. lets try that again"
        "oops":
            jump sprint2


label give:
    show catboy happy at top
    catboy "Wait, you're giving me money? You shouldn't have, but I really appreciate them!"
    hide catboy
    show text "{size=+50}{color=#000000}Later...{/color}" at truecenter
    with dissolve
    pause 3
    hide text
    with dissolve
    show bg generic
    "Man, I seriously need to keep a better eye on Elliot."
    "Atleast he's okay now....I hope..."
    show bird mock at top
    bird "Fwie Fwie Fwie. Why so gloomy, my young fellow?"
    show bird normal at top
    me "*sighs* Hey Corvo"
    bird "My, you look like you've seen better days! Whatever has happened back there?"
    me "Well, you see--"
    show bird mock at top
    bird "You don't have to answer that, I already saw everything."
    show bird normal at top
    me "..."
    bird "Now now don't give me that look. I'm just trying to lighten up the mood."
    show bird mock at top
    bird "Anyhoot, your journey doesn't end here. I'll be hooting for you~."
    bird "Knock 'em dead darling. Chiao~!"
    hide bird
    me "I swear, i'll never understand this guy...."
    show bg alleyway
    "It's been a week since I saw Elliot. I'm kind of scared in which state I'll find him this time but all I can hope for is that he is safe."
    "And of course, I bought more fish. My wallet is begging for me to stop but I would feel a little bit bad if I didn't."
    "I've decided to take him out to the park again. It may be cheesy and a bit repetitive, but I don't want to stay in this hellhole of a city for longer than I have to."
    "No matter how many times I've been here, it feels more and more unsafe."
    "To be fair, the fact that the first time I got robbed and the second time I saw someone bleeding badly probably doesn't help make me feel safer."
    "Finding Elliot also isn't easy. It feels like he could be anywhere."
    "Now, looking for a normal person already isn't easy, but this really feels like finding a twink in a haystack."
    "I just hope I find him soon. I wouldn't be surprised if I got robbed before I find hi-"
    "You feel yourself get dragged into a back alley"
    show catboy normal at top
    catboy "Money, phone, and wallet!"
    me "I thought I told you to stop robbing people, Elliot."
    catboy "And I listened! I just thought I'd say hi in a unique fashion."
    me "You smelled the fish, didn't you?"
    show catboy happy at top
    catboy "Could smell it from a mile away, so I figured you were looking for me."
    show catboy normal at top
    me "Who says these are for you? Maybe I'm trying to romance some other cute catboy."
    show catboy angry at top
    catboy "YOU'D NEVER! THOSE ARE MY FISHIES."
    show catboy normal at top
    me "If you want the fish, I'm afraid you're going to have to go out on another date with me."
    catboy "Oh nooooooo the horrorrrrrrrrrrr!"
    me "Well, in that case, I'll just find the next best catboy."
    show catboy angry at top
    catboy "NO NO NO NO NO NO NOPE! We're going on a date RIGHT MEOW!"
    hide catboy

label give2:
    menu:
        catboy "NO NO NO NO NO NO NOPE! We're going on a date RIGHT MEOW!"
        "Go on a date":
            jump catboydate3
        "Dont go on a date":
            jump rejectiondate3


label rejectiondate3:
    catboy "Noooooo you MEANIE! Why don't you want to anymore? You still have a date voucher you know..."
    birdinspirit "My, you've made him upset. No need to fret, lets try that again"
    menu:
        birdinspirit "My, you've made him upset. No need to fret, lets try that again"
        "sounds like a plan":
                jump give2

label catboydate3:
    show catboy happy at top
    catboy "Yaay! I'm so excited! Lets go!"
    hide catboy
    show text "{size=+50}{color=#000000}Another walk to the park later...{/color}" at truecenter
    with dissolve
    pause 3
    hide text
    with dissolve
    show bg generic
    show catboy normal at top
    "The two of us took the time to walk back to the park to get out of this awful city. Luckily, no stabbings or robberies occurred on the way out, which was nice. "
    "This might be the first time we get to go out together without anything bad happening. I figured we were due for a good date. I don't regret buying fish for the occasion."
    "I know Elliot said he'd go on a date with me regardless, but it feels wrong to not bring anything."
    "The walk is quite long, but seeing Elliot so happy is nice."
    me "So how have you been doing? Has your wound been healing nicely?"
    catboy "I've been doing well! The wounds have healed up alright. They aren't fully closed yet, but we're getting there!"
    me "That's nice! I'm glad you're doing ok. Couldn't bear seeing such a cutie in distress, you know."
    show catboy blush at top
    catboy "Awh! Thanks for worrying about me. You're so attentive."
    catboy "You've been giving me loads of fish, helped me clear up my wounds, and gave me the motivation I needed to turn my life around."
    show catboy normal at top
    me "It's nothing, I saw a cute catboy in distress and figured I might as well help him."
    show catboy blush at top
    catboy "You're a good person, you know."
    show catboy normal at top
    me "Yeah, too good for my own good. My wallet's been screaming at me. Fish is so expensive here."
    catboy "Awh, but it's for a good cause!"
    me "You're a good cause now?"
    catboy "I'm my own charity."
    me "More like a charity case."
    catboy "..."
    me "Cutest charity case though!"
    show catboy happy at top
    catboy "By the way, I have big BIG news to tell you!"
    me "Oh, what's the big news?"
    catboy "Well, your words last week inspired me. If you were willing to help me, there must be someone out there who would want to do so too!"
    catboy "So, with that in mind, I walked all over town to find a place that would hire me. "
    catboy "After a long while, I found this corner store that agreed to hire me. The best thing is, they even let me sleep in the back of the store as long as I open up the next day! "
    catboy "My days of sleeping on the street are over!"
    show catboy normal at top
    me "That's amazing, Elliot! I knew you could do it! I told you that someone would be looking out for you. No one could say no to such a pretty face."
    catboy "Well, I owe it all to you. If you hadn't inspired me to go out and better my life, who knows how long it would have taken me to do so on my own!"
    catboy  "For all I know, I could've died out on those streets. So really, thank you for being there for me."
    me "No problem. I would gladly do it again!"
    catboy "I'm going to have to be honest with myself. I need to tell you something."
    me "What's up, Elliot?"
    show catboy blush at top
    catboy "Well, you see, ever since you said those words to me last week, I haven't been able to think of anything else... Or anyone else. "
    catboy "You cared so much for me. You first had the guts to hit on me while I was threatening you, then you took me out. I still don't know what made you do that."
    show catboy normal at top
    me "This was cheaper than being robbed of everything I have."
    show catboy blush at top
    catboy "I guess. But to get back to what I was saying... On the second date, when you cared for me, patched me up, and gave me motivation to better myself, it felt so sincere."
    catboy "And shirtless you was pretty hot too."
    catboy "Regardless, though, I started to fall for you. Then a week later, you came back to check up on me and take me out on another date. Man, this is getting kind of embarrassing, but I think I like you."
    catboy "I've never felt this way before. My heart races every time I see you, and I feel so safe around you. I guess I only have one last thing to ask of you."
    catboy "Do you like me as well? Do you want to stay by my side? Do you want to be my partner in non-crime related activities?"
    show catboy normal at top
    menu:
        catboy "Do you like me as well? Do you want to stay by my side? Do you want to be my partner in non-crime related activities?"
        "Accept his love":
            jump catboyaccept
        "Reject him":
            if Haslooped == True:
                python:
                    YouFail = True
                jump catboyreject
            elif Haslooped == False:
                python:
                    Haslooped = True
                jump catboyreject
                

label catboyaccept:
    show catboy happy at top
    catboy "I KNEW YOU'D AGREE. This makes me so happy! Think of all the things we can do together once I get my life together! Man, it's going to be so much fun!"
    hide catboy
    show bg endscreen
    window hide
    pause 
    return

label catboyreject:
    show catboy normal at top
    catboy "Oh, that's okay. I shouldn't have gotten my hopes up. I knew there was a chance you'd say no, but I hoped you'd say yes. Can we still be friends though?"
    hide catboy
    pause 1
    if YouFail == False:
        show bird normal at top
        bird "Hmm? Was he not your style? But you two seemed so cute together."
        bird "Oh well, these things happen sometimes. I can't force you to date Elliot."
        bird "Too bad though, he was the best trap in the city."
        bird "Well, since you denied to be Elliot's partner, do you wish to meet other bachelors? You haven't been to the pond after all."
        show bird mock at top
        bird "You're also free to give up if you decide you're too bad at dating! Fwie fwie fwie fwie!"
        show bird normal at top
        bird "I'm kidding, but the choise is yours. What will it be, young fellow?"
        menu:
            bird "I'm kidding, but the choise is yours. What will it be, young fellow?"
            "i give up :(":
                hide bird
                show bg endscreen
                window hide
                pause 
                return
            "let me try the pond!":
                hide bird
                jump pond
    elif YouFail == True:
        show bg generic
        show bird mock at top
        bird "Well well well casanova, seems like today isnt your lucky day"
        show bird normal at top
        me "No need to kick me while im down!"
        bird "You had two chances and you rejected them both!"
        me "I know, I know"
        me "Hey, at least i still have Vanessa to look forward to when i go back home"
        show bird mock at top
        bird "Fwie fwie fwie"
        me "Huh? Why are you laughing?"
        bird "Fwie fwie fwie"
        me "Stop that, explain yourself!"
        show bird normal at top
        bird "oh poor, poor casanova. did you really think you ever stood a chance with Vanessa?"
        me "WHAT IS THAT SUPPOSED TO MEAN?!?!"
        show bird mock at top
        bird "IT'S OBVIOUS CASANOVA, I CATFISHED YOU"
        me "FROM A DIFFERENT DIMENTION?????"
        bird "DONT QUESTION IT"
        me "WAAAAAAAAAAAAAAAH"
        hide bird
        show bg endscreen
        window hide
        pause     
        return

label pond:
    "The pond is way closer than that city. Definitely a no-brainer to go there first."
    "And to be honest, the park is kinda nice. Nothing like it would be normally, but nice."
    "The park seems ten times bigger than normal. In the real world, it's just a small vertical park on top of some roofs of a building."
    show bg pond
    "Here, it's huge! There are flowers and bushes everywhere. The park is a lot broader and there seems to be a lake with a fountain up ahead."
    "It seems like a perfect place to sit, calm down and think about what happened."
    show octolady normal at center
    "Oh, there is already someone at the fountain. They have very luscious purple hair and, tentacles?!"
    unknownoctolady "Hu hu hu hu! Hello there love, you seem quite puzzled, is something wrong?"
    me "You...have tentacles..."
    unknownoctolady "My my, straight to the point I see. Well, you aren't wrong. I'm half octopus after all."
    me "How. How does that even happen?"
    show octolady happy at center
    unknownoctolady "Well, you see, when a mommy octopus and a daddy octopus love each other very much..."
    me "And I thought this whole situation couldn't get any weirder."
    unknownoctolady "I'm just messing with you, love. Hu hu hu hu."
    show octolady normal at center
    unknownoctolady "I haven't seen you around here love, do you come from far away or something?"
    me "I guess you could say that..."
    unknownoctolady "Well, seems like I've lucked out on the hottie I found today. You're so, otherworldly and intriguing."
    unknownoctolady "I want you to go out on a date with me."
    me 'Wha-what do you mean?'
    unknownoctolady "I've never seen anyone like you before. Your uniqueness attracts me."
    unknownoctolady "There is something about you I can't put my finger on and it makes me want to know everything about you."
    unknownoctolady "So go out on a date with me. My treat!"

label pond2:    
    menu:
        unknownoctolady "So go out on a date with me. My treat!"
        "Accept":
            jump octoladydateaccept
        "Reject":
            hide octolady
            unknownoctolady "Hmpf, well, I simply won't give you a choice then"
            unknownoctolady "No hotties may leave without going on a small date atleast once!"
            menu:
                unknownoctolady "No hotties may leave without going on a small date atleast once!"
                "lets try that again...":
                    jump pond2

label octoladydateaccept:
    show octolady happy at center
    unknownoctolady "Yaay! Alright, lets get this date started!"
    show octolady normal at center
    me "So, what is your name? I feel like it's rude to not ask for the name of my date."
    show octolady happy at center
    octolady "Oh my, where are my manners! I'm way too quick and rushing into things again. My name is Aaliyah, nice to meet you."
    show octolady normal at center
    octolady "So, now that you asked me a question, I want to know more about you! Where are you from? I've never seen anyone like you, and trust me, I've seen a lot of people."
    me "I'm from Earth."
    octolady 'Earth? Never heard of that before. It sounds like a beautiful place. Just the name makes me want to visit sometime!'
    me "Yeah, very beautiful. Earth has lots of water."
    octolady "Really? That sounds amazing! I love that place already. Earth must be far if I have never seen anyone like you before. Do all people from Earth look like you?"
    me "I mean, sort of? I'm surprised you have never seen a human before. I've seen octolings plenty."
    show octolady happy at center
    octolady "REALLY? WHERE! WHAT DO THEY LOOK LIKE? WHAT DO THEY DO? HOW DO I GET TO EARTH?"
    show octolady sad at center
    octolady "Sorry, I got a little excited. You see, I lost my family at sea. I washed up on the shore when I was little, and someone took me with them."
    octolady "Eventually, I ended up here, and I've been looking for my parents ever since."
    show octolady normal at center
    me "Can't you just get out?"
    octolady "You see, I can walk and sit on non-water objects, but it tires me out greatly. There is no sea nearby, and no lakes in the area are connected to the sea, so I'm kind of stuck. "
    octolady "But if you have heard of octo people like me, you must be able to tell me about them! What are the octo people like on Earth?"
    me "Yeah, well, funny story actually. You guys mostly appear in Japanese adult comic books."
    show octolady happy at center
    octolady "That sounds so cool! I bet we're superheroes fighting crime! These tentacles are made to fight crime."
    show octolady normal at center
    me "...yeah... definitely... you guys are superheroes for sure. Your tentacles really show people who's boss..."
    octolady "Man does Earth sound exciting! Too bad I'm mostly stuck at this fountain."
    me "How far can you go without water?"
    octolady "I sadly can't leave much further than the park. It's really frustrating, but I guess there is nothing to be done about it. I just kind of sit here and wait for people to come along that I can talk to. "
    octolady "I just kind of sit here and wait for people to come along that I can talk to. "
    octolady "But oh my, I'm oversharing. Thanks for keeping me company though. I'm here if you're looking for me."
    me "No problem, Aaliyah. It's been nice talking to you. I'll definitely come back if I'm in the area and looking for some company. Take care!"
    octolady "Thank you! I'll be right here, waiting. Take care too, and maybe next time you visit, you can tell me more about Earth and those octo people. Goodbye for now!"

label octoladydateaccept2:    
    menu:
        octolady "Thank you! I'll be right here, waiting. Take care too, and maybe next time you visit, you can tell me more about Earth and those octo people. Goodbye for now!"
        "I'll blow her a kiss on my way out":
            jump blowkiss
        "i wont blow her a kiss on my way out":
            jump noblowkiss

label  noblowkiss:
    me "Goodbye, Aaliyah. Until next time!"
    show octolady happy at center
    birdinspirit "Psst, casanova. Why didn't you give her a kiss on the cheek?"
    show octolady normal at center
    menu:
        birdinspirit "Psst, casanova. Why didn't you give her a kiss on the cheek?"
        "Yeah good idea, i'll try again":
            jump octoladydateaccept2

label blowkiss:
    show octolady normal at center
    me "Hey Aaliyah, look at me!"
    me "Mwah!"
    show octolady happy at center
    octolady "Awh, thank you! You're adorable"
    hide octolady
    show text "{size=+50}{color=#000000}Later...{/color}" at truecenter
    with dissolve
    pause 3
    hide text
    with dissolve
    show bg generic
    "Okay, that went well I think. She seems pretty nice."
    "Didn't think she'd ask me out on a date this fast though."
    show bird mock at top
    bird "Fwie Fwie Fwie, how are you doing, young fellow."
    show bird normal at top
    me "What are you doing here, Corvo?"
    bird "I came here to congratulate you on succesfully having your first date."
    show bird mock at top
    bird "Oh, my little socially inept little fellow, growing up so fast."
    show bird normal at top
    me 'Hey!'
    bird "I'm sorry, I'm just very proud of you. Keep going like you're doing now."
    bird "I'll be waiting for you when you finish your second date."
    show bird mock at top
    bird "At this rate, you might have a shot at dating Vanessa!"
    show bird normal at top
    bird "Anyways, it's time for you to continue your search for love, my little fellow. Are you ready?"
    menu:
        bird "Anyways, it's time for you to continue your search for love, my little fellow. Are you ready?"
        "Yes":
            hide bird
            jump octoladydate2

label octoladydate2:
    show bg pond
    "Yesterday was certainly an interesting encounter. I feel kind of bad for Aaliyah, though. Being stuck in a small lake in the middle of a park probably gets lonely. Not to mention the lack of privacy."
    "I've decided I'm going to visit her again. She seemed desperate for social interaction, and if talking to her makes her happier, I'll talk to her. "
    "I'd hate to be in her situation; the lack of privacy would eat me alive."
    "I've been thinking about where to bring her. If she can't leave this park, then her options are limited. I might be able to somehow carry her to a nice spot in the park."
    "It could be good for her to enjoy something other than that small lake."
    show octolady normal at center
    octolady "Hey love! Such a surprise to see you here! A happy surprise, though."
    me "Yeah, I know. I kept thinking about how lonely you must be staying in that water all the time."
    octolady "And what's supposed to be wrong about staying in the place that keeps me alive?"
    show octolady happy at center
    me "Nothing, but I thought you might not get out often, so I wanted to ask you out on a date in the park."
    show octolady sad at center
    octolady "Oh sweetie, that's adorable of you. The thing is, by the time we found a good spot, I'd have to be returning already, or else I'll dry out."
    octolady "My tentacles have to be wet, and every time I walk, some of that wetness sticks to the ground. That's why I can't go long distances."
    show octolady normal at center
    me "What if I carry you?"
    octolady "What do you mean?"
    me "Would you be able to have a small date in the park with me if I carried you there so you don't lose too much water by walking there yourself?"
    octolady "I think that might be possible! Are you sure though? I don't want to break your back."
    show octolady happy at center
    octolady "Alright, I'll climb on top of you. Hang on!"

label octoladydate2_1:
    show octolady normal at center
    menu:
        octolady "Alright, I'll climb on top of you. Hang on!"
        "Im gonna make vehicle noises while carrying Aaliyah":
            jump vehicle
        "Im gonna act like a normal human adult should":
            jump normal

label normal:
    hide octolady
    me "Alright, let's go!"
    birdinspirit "Wow, you sure are the life of the party. You should try that again"
    menu:
        birdinspirit "Wow, you sure are the life of the party. You should try that again"
        "Yeah, you're right. My bad":
            jump octoladydate2_1
        "Wtf thats my choice what if i dont want to look like an idiot??":
            birdinspirit "JUST MAKE THE DAMN VEHICE NOISES"
            menu:
                birdinspirit "JUST MAKE THE DAMN VEHICE NOISES"
                "OKAY FINE JEEZ":
                    jump octoladydate2_1

label vehicle:
    show octolady normal at center
    me "Vroom! Vroooom! Eeeeeek! Beep-beep! Skreeee! Clunk! Swish-swish! Pop-pop! Beep-beep!"
    octolady "What are you doing?"
    me "I'm making car noises! I'm a human vehicle"
    show octolady happy at center
    octolady "You're adorable! Go my little wagon, go!"
    show octolady normal at center
    me "I can't go any faster!"
    octolady "You better go faster or I'll treat you like a horse and slap your butt to go faster!"
    me "Well this is conflicting- I mean yes ma'am"
    hide octolady
    show text "{size=+50}{color=#000000}One goofy ride later...{/color}" at truecenter
    with dissolve
    pause 3
    hide text
    with dissolve
    show bg generic
    "You know, I kind of regret offering to carry Aaliyah. These tentacles weigh like feathers, but giving a piggyback ride to an adult instead of a kid really does make a difference."
    "It was worth it though, she seems really happy to be in this part of the park."
    show octolady normal at center
    "I don't think she's been able to truly experience how nice this park actually is."
    show octolady happy at center
    octolady "This place is so beautiful! I never got to spend much time here before! You chose a good spot!"
    show octolady normal at center
    me "Thank you! I came across it when I first came here."
    octolady "Does Earth have any of these kinds of places?"
    me "Loads! Not all are as colorful and peaceful though."
    octolady "Well, from what I've heard, this place isn't too peaceful either. The park is fine, but the city in the far distance has a bad reputation."
    me "Why?"
    octolady "Lots of criminal activity from what I've heard. If you plan on going there, watch your back."
    me "Really? I'll make sure I watch my back."
    show octolady happy at center
    octolady "Good, I wouldn't want to see the hottie in front of me get hurt. I'd have to patch you right up."
    show octolady normal at center
    me "You could patch me up anytime."
    show octolady happy at center
    octolady "Oh, how adorable! Young people are so cocky!"
    show octolady normal at center
    me "Young? If you think I'm young, how old are you?"
    show octolady happy at center
    octolady "My my, have you never been taught to not ask a lady for her age! Just kidding, I'm 32 love."
    show octolady normal at center
    me "Really? You sure don't look the part. You look 10 years younger at least!"
    show octolady blush at center
    octolady "Oh, don't make me blush!"
    show octolady normal at center
    octolady "To be honest, 10 might be a bit of an overstatement, but I never thought she would be older than 26. She's hot though, I dig it."
    me "So what do you do in your free time?"
    "That's such a stupid question. She physically can't leave the pond. What is she gonna say? SWIM?"
    octolady "Well, I obviously can't go far by myself, so I usually hang out in the pond and strike up conversations with hotties crossing my way."
    me " You do seem like quite the extrovert."
    octolady "Awh, thank you! You learn to love it if it's the only way to get any way of social interaction."
    me "Is that why you were so eager to go out on a date with me?"
    show octolady happy at center
    octolady "Well, I'd be lying if I didn't admit it's the reason I first talked to you. Though I must say, you looked rather nice. Can't expect me not to pass up asking you out on a date when you look like that."
    show octolady normal at center
    "Man this girl is flirting with me hard, I'm not sure if I dislike it though!"
    me "My my, you sure do love calling me hot, don't you?"
    show octolady blush at center
    octolady "..."
    me "Well, that's totally fine. But a cutie like you needs to hear they're hot too every once in a while."
    octolady "Oh stop, you're making me blush. The damn nerve of young people these days."
    show octolady normal at center
    me "Oh come on Aaliyah, you're still young! Stop calling yourself old!"
    show octolady happy at center
    octolady "Quite the gentleman's response! Hu hu hu hu! You got your manners taught right back home for sure!"
    show octolady normal at center
    octolady "I'm starting to feel light-headed and warm inside. I think we might need to go back. I'm afraid I'll dry out otherwise."
    octolady "I had an amazing time though, thank you!"

label vehicle2:
    menu:
        octolady "I had an amazing time though, thank you!"
        "Im gonna propperly wish her farewell":
            jump proper
        "Im just gonna say bye":
            jump bye

label bye:
    me "Bye!"
    hide octolady
    birdinspirit "Psst, casanova. You can be a bit more kinder than that. Here, go ahead and try again"
    menu:
        birdinspirit "Psst, casanova. You can be a bit more kinder than that. Here, go ahead and try again"
        "Fair enough":
            jump vehicle2

label proper:
    show octolady normal at center
    me "Yeah it was amazing. Take care alright! See you later!"
    show octolady happy at center
    octolady "Yeah, see later love!"
    hide octolady
    show text "{size=+50}{color=#000000}Later...{/color}" at truecenter
    with dissolve
    pause 3
    hide text
    with dissolve
    "Man, I never thought Aaliyah would enjoy the date that much."
    "I hope I can make the next one even better."
    show bird mock at top
    bird "Fwie Fwie Fwie. Why so happy, my young fellow? Not to worry, I already know. You had a good date!"
    show bird normal at top
    me "*sighs* Hey Corvo"
    bird "Not happy to see me? I thought we were student and mentor. Fwie fwie fwie."
    me "Well, you see--"
    show bird mock at top
    bird "You don't have to answer that, I KNOW we have that bond my little fellow. You're just a little shy."
    show bird normal at top
    me "..."
    bird "Now now don't give me that look. I'm just trying to lighten up the mood."
    bird "Anyhoot, your journey doesn't end here. I'll be hooting for you~."
    show bird mock at top
    bird "Knock 'em dead darling. Chiao~!"
    hide bird
    me "I swear, i'll never understand this guy...."
    show text "{size=+50}{color=#000000}Later...{/color}" at truecenter
    with dissolve
    pause 3
    hide text
    with dissolve
    "You know, I might have regretted giving an adult a piggy ride, but I don't regret seeing Aaliyah that happy."
    "It felt like she could finally have a conversation without having to worry the other person wasn't up to it and would leave her all alone in that pond."
    "But there were none, so I had to pick flowers growing in the park. Not my classiest moment. Corvo definitely has a reason to laugh at me now, but as long as Aaliyah doesn't realize, I guess it's fine."
    "Again, not my proudest moment, but I got to give credit to my creativity."
    "That being vandalizing a public park."
    "Do they have fantasy police over here? Will I be thrown into fantasy jail over my fantasy vandalism?"
    "Probably not to be honest. I don't think that the people who made this fantasy world wanted to go through that kind of trouble. Seems like too much work."
    "Anyways, I've been thinking of ways to get Aaliyah in contact with her family."
    "I don't know if there are any waters nearby, but maybe we could rent a truck or something, place a little kiddy pool in there and fill it with water."
    "Maybe she could stay in there until we reach a river or an ocean. Even then, if this place is anything like Earth, the world should be mostly made out of water."
    "And if Aaliyah's family lives in the wild, there is a decent chance they've ended up as someone's dinner."
    "Even then, I have no idea if Aaliyah would even want to find her family. Maybe I should just ask her once I get to the lake."
    "The lake is just up ahead, just a few more steps and I should be there."
    show bg pond
    "Huh, that's weird, she isn't here."
    "Where did she go? Man, I hope the fisherman didn't get to her. I spent all this time getting flowers for he-"
    show octolady happy at center
    octolady 'BOO! Hu hu hu hu! Did I scare you love? I sure hope I did!'
    show octolady normal at center
    me 'Were you planning on giving me a heart attack? I brought flowers to take you out on a date you know!'
    octolady "Well, I might just have. You left me to sit there and wait for you for an entire week you know. I thought you'd never come back."
    show octolady happy at center
    octolady "But I do appreciate the flowers love. Such a little gentleman."
    show octolady normal at center
    me "Well, would you still want to go out on a third date with me?"
    octolady "You did leave me alone for an entire week. That wasn't cool. But you know, if you call me the most handsome girl in the world, I will."

label proper2:
    show octolady normal at center
    menu:
        octolady "You did leave me alone for an entire week. That wasn't cool. But you know, if you call me the most handsome girl in the world, I will."
        "Call her the most handsome girl in the world":
            jump handsome
        "Dont call her the most handosme girl in the world":
            jump nothandsome

label nothandsome:
    hide octolady
    me "Nope, not going to happen."
    octolady "You know what, I was willing to let it slide if you just said that, but now I won't. You should go reflect on how you've treated me the past week."
    birdinspirit "You really just said that huh? Here, you should try that one again"
    menu:
        birdinspirit "You really just said that huh? Here, you should try that one again"
        "Yeah, you're right":
            jump proper2
        "I just kinda wanted to see what would happen lmao":
            birdinspirit "*facepalm*"
            jump proper2

label handsome:
    show octolady normal at center
    me "You know what, sure. Aaliyah, you're the most handsome girl in the world."
    show octolady happy at center
    octolady "You know, I was kidding, but that's actually really sweet. Let's go on that date."
    show octolady normal at center
    me "So, I'm going to have to be honest here, I haven't thought of any place that we could go to this time."
    octolady 'We should just stay here, I have to recharge my water levels anyways. I was waiting in the bushes for a while.'
    me "Alright, that's fine with me. Is there any reason you wanted to scare me?"
    show octolady happy at center
    octolady "I felt like you might as well feel some of my pain. And it kinda worked hu hu hu hu."
    show octolady normal at center
    octolady "So, what have you been up to, love? Done anything exciting without me?"
    me "Most of my week has been spent looking for flowers for you, to be honest. They're hard to buy around here."
    octolady "So you got them from the park?"
    me "HOW DID YOU KNOW?!"
    show octolady happy at center
    octolady "Oh love, I've lived here for most of my life. I might be restricted to just the park, but that doesn't mean I don't leave my pond often, you know. I do appreciate the flowers though."
    show octolady normal at center
    me "Man, I feel embarrassed right now. Did you know this whole time?"
    octolady "Yup, but I thought it was cute, so I wasn't going to say anything."
    show octolady happy at center
    octolady "You look adorable when you're embarrassed though. Hu hu hu hu!"
    show octolady normal at center
    me "Hey now, don't make fun of me!"
    octolady "Don't worry, love, I'm just teasing you. I do mean it when I say you're cute though."
    me "You know you're supposed to be nice to your date, right?"
    show octolady happy at center
    octolady "Oh, but I am! I just like seeing my date a little flustered. I guess you're a bit shy when it comes to compliments. Hu hu hu hu!"
    show octolady normal at center
    me "As if you're one to talk, I saw that blushing face every time I complimented you on our previous dates."
    octolady "That never happened. You're lying!"
    me "So if I call you an adorable, cute-looking octogirl, you wouldn't be blushing?"
    show octolady blush at center
    octolady "...No..."
    show octolady normal at center
    me "See, knew you were lying!"
    me "So now, on a more serious note, I've been thinking of ways to get you back to the ocean!"
    me "Maybe we can rent a small van, put a little plastic swimming pool in there, and drive to the nearest ocean!"
    octolady 'Well-'
    me "Or maybe I can just lift you to some river nearby and get you to the ocean that way."
    octolady 'Actually-'
    me "Or can you move freely in the rain? I don't think you can since you stayed here all this time, but maybe that's an option too?"
    show octolady angry at center
    octolady "HEY! I'm trying to tell you something!"
    show octolady normal at center
    octolady "I'm not going to move anywhere."
    me "What but you said-"
    octolady "I know what I said before, but I've realized that I really don't have a clue where my family is, or if they would even still be alive."
    octolady "One thing I do know is that they would want me to be safe, and since this is about the most peaceful you can get, I've decided to stay here."
    show octolady happy at center
    octolady "Plus, a little cutie from Earth helps to make it more bearable too!"
    show octolady normal at center
    me "Really? Are you just going to live in the pond forever?"
    octolady "You know, it isn't that bad. I've made quite some friends over the years, and I have no one in the ocean."
    show octolady happy at center
    octolady "Plus, I don't think you have gills. It gets kind of hard to breathe underwater without them."
    show octolady normal at center
    me "What do you mean? Do you want me to come with you?"
    show octolady blush at center
    octolady "Well, you see, I've been thinking about it. You've been so nice to me, and you made me realize how much I have in this park. And in doing so, you made me a lot more confident in my own skin."
    octolady "I kinda started falling for your kindness towards me on the second date when you went out of your way to lift me to a spot in the park just to have a unique date with me."
    octolady "I guess I haven't asked yet, so I'll do it right now. I know this is going fast all of a sudden, but I feel like I need to ask."
    octolady "Do you want to be my partner? Do you want to spend the rest of your life with me?"
    menu:
        octolady "Do you want to be my partner? Do you want to spend the rest of your life with me?"
        "Accept her love":
            jump octoladyaccept
        "Reject her love":
            if Haslooped == True:
                python:
                    YouFail = True
                jump octoladyreject
            elif Haslooped == False:
                python:
                    Haslooped = True
                jump octoladyreject
            

label octoladyreject:
    show octolady normal at center
    octolady "Oh, well, I guess that is to be expected. I got so caught up in my own feelings I didn't even consider that you might not feel the same way about me."
    hide octolady
    pause 1
    if YouFail == False:
        show bg generic
        show bird normal at top
        bird "Hmm? Was she not your style? But you two seemed so cute together."
        bird "Oh well, these things happen sometimes. I can't force you to date Aaliyah."
        bird "Too bad though, she was the hottest milf around the park."
        bird "Well, since you denied to be Aaliyah's partner, do you wish to meet other bachelors? You haven't been to the city after all."
        show bird mock at top
        bird "You're also free to give up if you decide you're too bad at dating! Fwie fwie fwie fwie!"
        show bird normal at top
        bird "I'm kidding, but the choise is yours. What will it be, young fellow?"
        menu:
            bird "I'm kidding, but the choise is yours. What will it be, young fellow?"
            "i give up :(":
                hide bird
                show bg endscreen
                window hide
                pause     
                return
            "let me try the city!":
                hide bird
                jump city
    elif YouFail == True:
        show bg generic
        show bird mock at top
        bird "Well well well casanova, seems like today isnt your lucky day"
        show bird normal at top
        me "No need to kick me while im down!"
        bird "You had two chances and you rejected them both!"
        me "I know, I know"
        me "Hey, at least i still have Vanessa to look forward to when i go back home"
        show bird mock at top
        bird "Fwie fwie fwie"
        me "Huh? Why are you laughing?"
        bird "Fwie fwie fwie"
        me "Stop that, explain yourself!"
        show bird normal at top
        bird "oh poor, poor casanova. did you really think you ever stood a chance with Vanessa?"
        me "WHAT IS THAT SUPPOSED TO MEAN?!?!"
        show bird mock at top
        bird "IT'S OBVIOUS CASANOVA, I CATFISHED YOU"
        me "FROM A DIFFERENT DIMENTION?????"
        bird "DONT QUESTION IT"
        me "WAAAAAAAAAAAAAAAH"
        hide bird
        show bg endscreen
        window hide
        pause     
        return

label octoladyaccept:
    show octolady normal at center
    octolady "Yaay! I knew you would say yes. We're going to be the most adorable couple. I'm so happy! You showed me how good life can be, and I'm very grateful for that."
    octolady "Let's be together forever!"
    hide octolady
    show bg endscreen
    window hide
    pause 
    return