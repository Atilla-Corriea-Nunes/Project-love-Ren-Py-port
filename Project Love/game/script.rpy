# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define me = Character('Me', color='#000080')
define bird = Character('Corvo', color='#6ececd')
define catboy = Character('Elliot', color='#2d532f')
define octolady = Character('Aaliyah', color='#8b2650')
define unknownbird = Character('???', color='#6ececd')
define unknowncatboy = Character('???', color='#2d532f')
define unknownoctolady = Character('???', color='#8b2650')
define birdinspirit = Character('Corvo (in spirit)', color='#6ececd')



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



    
# The game starts here.

label start:
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
    bird "Do you really think Vanessa would have wanted to go out with such a sad little loser like you? You've got no dating experience!"
    show bird mock at top
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
        "Go to the City":
            hide bird
            "I can see some buildings up ahead. They don't seem to be the ones that are around here in the normal world though. Regardless, I might find a way back."
            "Hell, if that weird bird is right, I might even get to bang some chicks!"
            "Game Dev Team" "(Authors note: No chicks are going to banged)"
            jump city
        "Go to the Pond":
            jump pond

label gohome:
    "Ah forget it. I'd rather be with my waifus. Hatsune Miku i'm coming home baby~!"
    "Game Dev Team" "You go home to make out with your body pillow-- seriously what is wrong with you"
    menu:
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
        "Okay fine fine, take my money!":
            jump GOmoney
        "Flirt with him":
            jump catboyflirt
    return

label GOmoney:
    hide catboy
    "Yeah thats right, now beat it!"
    "Shit, there goes my money"
    menu:
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
    show text "{size=+50}{color=#2d532f}One walk to the park later...{/color}" at truecenter
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
        "Share your fish":
            jump Share
        "Dont Share your fish":
            jump Noshare
    return

label NoShare:
    hide catboy
    catboy "HEY, DON'T HOG THEM ALL FOR YOURSELF!"
    me "OW OW OKAY NO NEED TO SCRATCH"
    birdinspirit "Smooth, very smooth. Let's roll that one back"
    menu:
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
    show catboy anrgy at top
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
    catboy "You do want to go out on another date, right?"
    menu:
        "Yes":
            jump yescatboy
        "No":
            jump nocatboy

label nocatboy:
    hide catboy
    catboy "Ugh, so you're the type of person to just tease anyone huh? Gross.."
    birdinspirit "Way to screw that one up casanova. Here, lets try that again"
    menu:
        "Good idea...":
            jump Share2

label yescatboy:
    show catboy happy at top
    catboy "Yeah, I knew you would! See you then!"
    hide catboy
    "Okay, that went well I think. Atleast I didn't lose all my money."
    "I still don't know why I agreed to go on a date with him, but it was nicer than I expected."
    show bird mock at top
    bird 'Fwie Fwie Fwie, how are you doing, young fellow.'
    me "What are you doing here, Corvo?"
    show bird normal at top
    bird "I came here to congratulate you on succesfully having your first date."
    show bird mock at top
    bird "Oh, my little socially inept little fellow, growing up so fast."
    me 'Hey!'
    show bird normal at top
    bird "I'm sorry, I'm just very proud of you. Keep going like you're doing now."
    bird "I'll be waiting for you when you finish your second date."
    show bird mock at top
    bird "At this rate, you might have a shot at dating Vanessa!"
    show bird normal at top
    bird "Anyways, it's time for you to continue your search for love, my little fellow. Are you ready?"
    menu:
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
        "Im gonna run at full speed!":
            jump sprint
        "Actually, im gonna moonwalk over there":
            jump moonwalk

label moonwalk:
    "You moonwalked over there. You might not be fast, but atleast you're stylish! Style over (human?) lives, am I right?"
    birdinspirit "Speed it up casanova. Time is ticking! You could try to run this time instead"
    menu:
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
    menu:
        "Im gonna give Elliot some money to get through the week":
            jump give
        "Im gonna keep my money all to myself":
            jump dontgive

label dontgive:
    "I didn\'t give Elliot any money. I\'m sure he\'ll be alright. Atleast, that\'s what I tell myself"

label pond:
    return