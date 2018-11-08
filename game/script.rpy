# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define cost = Character("Costy")
define vale = Character("Valeria")

define prota = Character("[name]")
define june = Character("June")
define mara = Character("Mara")
define sugar = Character("Sugar")
define alan = Character("Alan")
define art = Character("Arturo")
define sol = Character("Sol")
define prof = Character("Profesor")
define marcos = Character("Marcos")

# El juego comienza aquí.

label start:

    $ bodytype = 0 # 3 tipos
    $ hairlenght = 0 # 3 tipos
    $ done = False # Para terminar seleccion
    $ crush = 0 # Para crush (1 june, 2 mara, 3 sugar)

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene black

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    # Presenta las líneas del diálogo.

    $ name = renpy.input("{color=#ff1163}What's your name?{/color}")
    $ name = name.strip() or "Ari"

    show screen customization with dissolve
    with fade
    show screen vestuario1 with dissolve

    window hide
    $ renpy.pause(hard=True)

    label escena1:
        hide screen customization
        hide screen vestuario3
        hide screen vestuario1
        hide screen vestuario2
        hide screen body1
        hide screen body2
        hide screen body3
        hide screen skin1
        hide screen skin2
        hide screen skin3
        hide screen skin4
        hide screen skin5
        hide screen skin6
        hide screen skin7
        hide screen skin8
        hide screen skin9
        hide screen skin10
        hide screen skin11
        hide screen skin12
        hide screen hair1
        hide screen hair2
        hide screen hair3
        hide screen hair4
        hide screen hair5
        hide screen hair6
        hide screen hair7
        hide screen hair8
        hide screen hair9
        hide screen hair10
        hide screen hair11
        hide screen hair12
        hide screen hair13
        hide screen hair14
        hide screen hair15
        hide screen hair16

        scene black

        show costy:
            xalign 0.5
            yalign 0.0
            zoom 0.6

        cost "Hi there!"

        cost "My name is Costy, I’m the creator of Asphyxia."

        cost "Who are you? What’s your name?"

        cost "Oh, nice to meet you, [name]!"

        cost "I’m here to explain you how does this game work. Well first let's start with-"

        hide costy
        show vale:
            xalign 0.5
            yalign 1.0
            zoom 0.7

        vale "Hey!!! I want to be part of the spotlight too!"

        vale "Hi gurl!, I'm Valeria the programmer-of-Asphyxia-commander-in-chief-most-amazing-software-developer-ever!"

        vale "Haha well at least I like to believe I'm all that."

        vale "Now where were we? Oh yeah! Costy was trying to explain you how to play the game!"

        cost "Indeed, so could you please focus?"

        vale "Yes ma'am."

        cost "Ok. This is a game where your decisions matter. Think carefully about every choice you make, because those will change the course of the story."

        cost "There are multiple endings and multiple images that you can obtain."

        cost "Depending on your choices, you’ll have one ending or another, and you will gain one image or another."

        cost "Just like real life!"

        vale "And as an aditional feature you can choose how you wanna be!"

        cost "So, if you are ready, let’s define your appearance!"

        vale "You can choose between different types of body, skin and hair."

        vale "The controls are very easy, basically you just have to click on things or hover over them to reveal images and other surprises."

        vale "After that, the story will start. I can't wait to see how you'll manage everything!"

        cost "Well, I think that's all. Good luck and have fun!"

        scene black

        "¡RIIIIIIIIIING!"

        prota "What the herg?"

        "¡RIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIING!"

        prota "Oh, for Viktor’s heels."

        menu:
            "Let it ring":
                jump choice1

            "Answer":
                jump choice2

        label choice1:
            "It rings for a few moments more, and then it’s completely silent again."

            prota "Finally."

            scene habnoche with fade

            prota "Whom on Earth is calling me at… at…"

            prota "…2 a.m.?"

            prota "..."

            prota "WAIT A SECOND."

            "I go through my last calls, in a hurry."

            prota "Please, pick up, please, please, please…"

            jump choice1_done

        label choice2:
            scene habnoche with fade

            prota "Hello?"
            jump choice1_done

        label choice1_done:

            marcos "Hi?"

            prota "MARCOS, WHAT THE HERG ARE YOU DOING DUDE?"

            marcos "I’m sorr-"

            prota "DON’T YOU HAVE GUGGLE IN GERMANY? You could check what time is it here!"

            marcos "[name], chill out! I didn’t reach home until now."

            prota "..."

            marcos "Sorry if I upset you."

            menu:
                "Oh, no, it’s fine.":
                    jump choice3

                "Next time, check what time is it before calling.":
                    jump choice4

            label choice3:

                prota "Man, it’s ok. No problem."
                jump choice2_done

            label choice4:

                prota "You could have checked, dude."
                jump choice2_done

            label choice2_done:

                prota "Anyway, what were you calling for?"

                marcos "Ah, yes! Are you ready for your last high school week? And for that amazing thing you promised you’ll do?"

                prota "Gah."

                prota "No."

                marcos "Wow, your voice changed suddenly."

                prota "I won’t do it, ok?"

                marcos "You WON'T?!"

                marcos "You won't confess to your ultimate teenage crush before leaving High School?"

                marcos "Why not?!"

                menu:
                    "Because I’m scared.":
                        jump choice5

                    "Because I’d feel stupid.":
                        jump choice6

                    "Because it’s a cliché.":
                        jump choice7

                label choice5:
                    prota " Because I’m terrified of what could happen after that."
                    jump choice3_done

                label choice6:
                    prota "Because I would feel like an idiot if I confess to her."
                    jump choice3_done

                label choice7:
                    prota "Because is so cliché, man. The next thing I should do is give her flowers."
                    jump choice3_done

                label choice3_done:
                    marcos "Don’t be ridiculous. But… you promised me!"

                    prota "This has nothing to do with you, Marcos. I mean, exposing myself is my business."

                    prota "Besides, you’re having fun in Germany and you won’t suffer the consequences of this if everything goes to heck."

                    marcos "But I’m your best friend… and you made me a promise."

                    prota "This has nothing to do with that!"

                    marcos "Ok, alright. What I mean is… you can’t keep this inside forever."

                    marcos "Someday, you’ll have to put it out. You will never be 100 percent happy if you continue hiding this."

                    prota "Whoa, hang on there, Marcos."

                    prota "It’s late and I’m tired."

                    prota "Actually, I was sleeping but SOMEONE waked me up."

                    marcos "Ok, ok. I’ll let you sleep."

                    marcos "Don’t miss this chance, [name]."

                    prota "Bye."

                    marcos "Good night."

    label escena2:

        "Even though Marcos led me sleep, I couldn’t. I rolled and rolled around in bed, thinking about what he said."

        prota "Maybe I should do this."

        prota "I have such a big crush on her."

        prota "But what if she doesn’t like girls? What if she thinks I’m a pervert?"

        prota "What if another people find out and start harassing me again?"

        "Suddenly, my phone sends me a notification. My crush has uploaded a new photo in Tuiter. And her friends as well."

        show screen notifications with dissolve
        show cellphone with dissolve:
            xalign 0.93
            yalign 0.25

        label vacio:
            "Let's see..."
            $ renpy.pause(hard=True)

        label choosegirl1:
            show screen junepic with dissolve
            prota "She looks so into that book."
            jump vacio

        label choosegirl2:
            show screen marapic with dissolve
            prota "Oh, she looks more and more athletic every time I see her."
            jump vacio

        label choosegirl3:
            show screen sugarpic with dissolve
            prota "How does she manage to do all this stuff at the same time?."
            jump vacio

        label choosegirldone:

            hide cellphone with dissolve
            hide junepic with dissolve
            hide marapic with dissolve
            hide sugarpic with dissolve
            hide notifications with dissolve

            prota "Damn, she’s pretty."
            #$ renpy.pause(hard=False)

        prota "Marcos is right. I can’t keep hiding this into myself. I have to let it out."

        "I take a really deep breath, and then I shout with everything I've got:"

        menu:
            "June is my crush!":
                $ crush = 1
                jump choosegirldone2

            "Mara is my crush!":
                $ crush = 2
                jump choosegirldone2

            "Sugar is my crush!":
                $ crush = 3
                jump choosegirldone2

        label choosegirldone2:

            "It feels good to say it out loud."

            "But after waking up the whole neighborhood with my yelling, my little brother shouts at me from the other room, completely annoyed."

            alan "SHUT UP! There’s people trying to sleep here, you know."

            prota "Then stop playing Fort Night if you wanna sleep so terribly!."

            "He’s right, though. I should probably sleep."

    label escena3:

        scene basket with fade

        "Ok, it’s already Friday and yet I didn’t do anywhing about my crush."

        "Marcos has been sending me whasaps every night to remember me to do that. How annoying can he be!"

        "Though, I’m still doubting"

        "A small figure comes to me, really excited and happy."

        hide alanfeliz
        hide alancute
        hide alanenojado
        hide alanneutral
        hide alanasustado
        show alanfeliz:
            xalign 0.5
            yalign 1.0
            zoom 0.8

        alan "Did you saw me? Did you saw my last shot?"

        menu:
            "Yes, I did!":
                jump choice8

            "Sorry, I was distracted!":
                jump choice9

        label choice8:

            prota "Yes, it was amazing!"

            hide alanfeliz
            hide alancute
            hide alanenojado
            hide alanneutral
            hide alanasustado
            show alancute:
                xalign 0.5
                yalign 1.0
                zoom 0.8

            alan "Really? And what do you think about the guy who I passed after? He’s cool, right?"

            prota "…"

            jump choice4_done

        label choice9:

            prota "I’m sorry, sweetie, I was really unfocussed."

            jump choice4_done

        label choice4_done:

            prota "I’m sorry, I didn’t paid attention."

            hide alanfeliz
            hide alancute
            hide alanenojado
            hide alanneutral
            hide alanasustado
            show alanenojado:
                xalign 0.5
                yalign 1.0
                zoom 0.8

            alan "Ah."

            alan "I though you were here to watch me playing."

            prota "Well, there’s something bothering me"

            hide alanfeliz
            hide alancute
            hide alanenojado
            hide alanneutral
            hide alanasustado
            show alanneutral:
                xalign 0.5
                yalign 1.0
                zoom 0.8

            "Really quick, I tell him about the promise I made to Marcos, and about this crush I have on this girl."

            "He does not look angry anymore, though."

            alan "So, you have always liked a girl in your class but you never talked to her?"

            prota "We talked, once."

            hide alanfeliz
            hide alancute
            hide alanenojado
            hide alanneutral
            hide alanasustado
            show alanfeliz:
                xalign 0.5
                yalign 1.0
                zoom 0.8

            alan "AWWW. That’s super cute, [name]!"

            prota "Alan, focus, please."

            hide alanfeliz
            hide alancute
            hide alanenojado
            hide alanneutral
            hide alanasustado
            show alanasustado:
                xalign 0.5
                yalign 1.0
                zoom 0.8

            alan "SORRY"

            hide alanfeliz
            hide alancute
            hide alanenojado
            hide alanneutral
            hide alanasustado
            show alanneutral:
                xalign 0.5
                yalign 1.0
                zoom 0.8

            alan "The thing is, I don’t really know what you should do."

            hide alanfeliz
            hide alancute
            hide alanenojado
            hide alanneutral
            hide alanasustado
            show alancute:
                xalign 0.5
                yalign 1.0
                zoom 0.8

            alan "Dad always says this: when you have a problem, you should ask a person who has more experience that you in that area."

            prota "Like a teacher or something?"

            alan "Yes? I guess."

            "One of Alan’s friends calls him, quite in a hurry."

            hide alanfeliz
            hide alancute
            hide alanenojado
            hide alanneutral
            hide alanasustado
            show alanfeliz:
                xalign 0.5
                yalign 1.0
                zoom 0.8

            alan "I have to go! But if you need any more advice, you can always come."

            prota "Ok, lil bro. And, Alan?"

            hide alanfeliz
            hide alancute
            hide alanenojado
            hide alanneutral
            hide alanasustado
            show alancute:
                xalign 0.5
                yalign 1.0
                zoom 0.8

            alan "Yes?"

            prota "Don’t tell mum or dad. And come home before 8.pm!"

            hide alanfeliz
            hide alancute
            hide alanenojado
            hide alanneutral
            hide alanasustado
            show alanenojado:
                xalign 0.5
                yalign 1.0
                zoom 0.8

            alan "*gasps* Ok, fiiiiiiine."

            hide alanenojado with dissolve

            "There he goes."

            "He’s only 11, but he’s more wise than most of the adults I know."

            "And he’s right. I should ask someone with experience. Or maybe someone whom knows a lot about this topic."

        menu:
            "Look for an experimented person.":
                jump choice10

            "Look for an informed person.":
                jump choice11


        label choice10:
            prota "Ok, here I go!"
            jump escena4

        label choice11:
            prota " Ok, here I go!"
            jump escena4

    label escena4:

        scene biblio with fade

        prota "This is fun. I have never been in this library more than 20 minutes since I started high school."

        prota "And now that I’m about to leave, I decide to spend my last teenage moments among this books."

        prota "But he can only be here."

        "I start looking around the bookshelves, wondering where the hell he is."

        menu:
            "Look around the fantasy section.":
                jump choice12

            "Look into the filosophy section.":
                jump choice13

        label choice12:
            prota "Man, he’s not here."
            jump choice5_done

        label choice13:
            prota "Oh, no, he’s not here."
            jump choice5_done

        label choice5_done:

            "As soon as I turn around, I bump into a person way taller than me."

            prota "Oh, I’m sorry."

            "Wait a second."

            prota "Álvarez Sensei!"

            show profeenojado:
                xalign 0.5
                yalign 1.0
                zoom 0.53

            prof "There’s no need to call me “sensei” out of the class, [name]."

        menu:

            "Sumimasen.":
                jump choice14

            "Gomen ne.":
                jump choice15

        label choice14:
            prota "Sumimasen!"
            jump choice6_done

        label choice15:
            prota "Gomen ne!"
            jump choice6_done

        label choice6_done:

            hide profeenojado
            show profeneutral:
                xalign 0.5
                yalign 1.0
                zoom 0.53

            prof "Well, seems like you have been paying attention in my classes."

            prota "Actually, I’m here because I want to ask you something."

            "Very quick, I start telling him that I like someone from my same gender and everything that has been around my head this week."

            hide profeneutral
            show profeenojado:
                xalign 0.5
                yalign 1.0
                zoom 0.53

            "Every word I say, this face becomes more and more somber."

            "He’s the only gay teacher we have, and even though that, not everyone is conscious of this side of him. I’d prefer to talk to a woman, but I’m aware the institution is not hiring any lesbian teachers."

            "I don’t know why that’s different from hiring gay men."

            "When I’m finished, Álvarez Sensei puts a hand in my shoulder."

            prof "I don’t think you should confess to her."

            prota "Wait, what? Why not?"

            hide profeenojado
            show profetriste:
                xalign 0.5
                yalign 1.0
                zoom 0.53

            prof "If you do that, I could be a problem for you in the future."

            prof "If people knows that you are not… let’s say, straight, that could blind them and it would be difficult for you to get a job."

            hide profetriste
            show profeenojado:
                xalign 0.5
                yalign 1.0
                zoom 0.53

            prof "And I not only mean jobs. Scholarships, trips, prizes… all that stuff can be out of your life if you proclaim yourself as gay."

            "I’m so surprised that I don’t know what to say."

            prota "Is that how being gay works? What’s the point, then?"

            hide profeenojado
            show profetriste:
                xalign 0.5
                yalign 1.0
                zoom 0.53

            prof "Wait until you get a stable job, a stable family, a stable life. And go out of the closet then."

            hide profetriste
            show profeneutral:
                xalign 0.5
                yalign 1.0
                zoom 0.53

            prof "[name], that would be enough to get you out of risk."

            "I’m completely astonished. That’s not how I expected our conversation to go through."

            "I thank my teacher, and I leave him, sunk in my thoughts."

            hide profeneutral with dissolve

    label escena5:

        scene gym with fade

        "I don’t know why, but my feet lead me to the gym of the school."

        "The closing ceremony has ended and everyone is picking up their stuff."

        "I sit in one of the empty chairs."

        prota "Poor Álvarez Sensei."

        prota "Life must have been hard for him."

        prota "He’s from another generation, though. Things should be different know. You shouldn’t be kick away from a job just because you like people from your same gander, right?"

        prota "…"

        prota "Marcos would do a sarcastic comment about that."

        "While I’m thinking, a ball flies directly to my face!"

        menu:
            "Turn head to the left.":
                jump choice16

            "Turn head to the right":
                jump choice17

        label choice16:
            prota "I move to the left!"
            jump choice8_done

        label choice17:
            prota "I move to the right!"
            jump choice8_done

        label choice8_done:

            "Just before I can do anything, someone catches the ball and saves my ass."

            art "Ey, you two. Be careful, for God’s sake!"

            show stalkerpreocupado:
                xalign 0.5
                yalign 1.0
                zoom 0.47

            "I look at him, while he scolds two first year student. He takes his vice-captain position very seriously."

            art "You weren’t injured, right? If so, I’ll go and kick their asses."

            "I laugh."

            prota "Artie, you shouldn’t kick someone’s ass because of this!"

            hide stalkerpreocupado
            show stalkerneutral:
                xalign 0.5
                yalign 1.0
                zoom 0.47

            art "Well, I would if they hurt you."

            "He sits next to me. Artie has been friends with Marcos since we started high school. I have a normal relationship with him, nothing that bonding as Marcos and I."

            hide stalkerneutral
            show stalkerpreocupado:
                xalign 0.5
                yalign 1.0
                zoom 0.47

            art "So, how’s big dick’s head doing in Germany?"

        menu:
            "He’s having fun.":
                jump choice18

            "He’s making great stuff.":
                jump choice19

        label choice18:

            prota "He’s having the time of his life. And look at us, here, abandoned, and homeless!"
            jump choice9_done

        label choice19:

            prota " He’s doing great and amazing things. And look at us, here, abandoned, and homeless!"
            jump choice9_done

        label choice9_done:

            hide stalkerpreocupado
            show stalkerneutral:
                xalign 0.5
                yalign 1.0
                zoom 0.47

            "Arturo throws a laugh. A few girls turn their heads to look at him."

            art "Ok, ok, good one, [name]. I think you’re missing him, right?"

            prota "I do."

            art "Well, you can talk to me, if you want. I might not be as amazing as that asshole, but I can listen a bit."

            hide stalkerneutral
            show stalkerpreocupado:
                xalign 0.5
                yalign 1.0
                zoom 0.47

            "I nod and start talking. He’s really into all the idea of the crush and stuff. He even gives me advice about how to get a boy."

            prota "But my crush is not a boy, Artie."

            "His expression changes."

            hide stalkerpreocupado
            show stalkerenojado:
                xalign 0.5
                yalign 1.0
                zoom 0.47

            art "What do you mean by “not a boy”?"

            "Oh. His voice sounds sharp."

            prota "What you hear. A person who’s gender is not male."

            "He gasps. The atmosphere feels heavy."

            hide stalkerenojado
            show stalkerpreocupado:
                xalign 0.5
                yalign 1.0
                zoom 0.47

            art "So… like… like…"

        menu:
            "Be sarcastic.":
                jump choice20

            "Be direct.":
                jump choice21

        label choice20:

            prota "Like a dinosaur, Artie. Come on, man, use your brain! Is a girl!"
            jump choice10_done

        label choice21:

            prota "Like a girl, Artie. I’m talking about a girl."
            jump choice10_done

        label choice10_done:

            "Arturo seems completely concerned."

            art "Are you sure… about that?"

            prota "What do you mean?"

            hide stalkerpreocupado
            show stalkerneutral:
                xalign 0.5
                yalign 1.0
                zoom 0.47

            art "That if you’re sure this is not a phase. What If you are confused?"

            prota "Ehm, no? I’m sure of what I am."

            hide stalkerneutral
            show stalkerenojado:
                xalign 0.5
                yalign 1.0
                zoom 0.47

            art  "I can’t believe you are like one of those!"

            prota "One of what?"

            "I’m getting really angry. I don’t know when, but we have both stand up."

            art "One of those… FAGGOTS."

            "I’m shocked. I make a step back, as shocked as I’ve never been."

            "Is that what Álvarez Sensei meant when he said that I’d be safe if I don’t tell anyone I like girls?"

            art "Maybe you should try with other men. Maybe you haven’t kissed a man who can makes you feel like a woman."

            "Oh, for Shoyo’s crow."

            prota "Listen to me, you ridiculous ignorant asshole. I FEEL like a woman. I AM a woman. And I LIKE women. I feel attracted to them. It has nothing to do with my gender identity."

            hide stalkerenojado
            show stalkerneutral:
                xalign 0.5
                yalign 1.0
                zoom 0.47

            art "Now you sound like one of those communist people."

            "Once he says so, a big girl stands in front of him."

            sol "What does communism to do with that, idiot?"

            hide stalkerneutral

            show solenojada:
                xalign 0.5
                yalign 1.0
                zoom 0.4

            "Sol is here!"

            "Sol is the one person who’s bigger and stronger than Arturo. She can kick his ass while she’s eating a sandwich."

            "She’s awesome."

            hide solenojada
            show solenojada:
                xalign 0.7
                yalign 1.0
                zoom 0.4

            show stalkerenojado:
                xalign 0.3
                yalign 1.0
                zoom 0.47

            sol "Go back to the Paleolithic Ages where you belong, cave man!"

            art "You will regret this, one day. You’re not gay, you’re just confused."

            prota "Oh, fuck off, dude."

            hide stalkerenojado with dissolve

            "He’s leaving. Sol looks at me with anger in her eyes."

            hide solenojada
            show solenojada:
                xalign 0.5
                yalign 1.0
                zoom 0.4

            sol "He’s such a dick."

            prota "He is."

            "She gives me a worried look."

            hide solenojada
            show soltriste:
                xalign 0.5
                yalign 1.0
                zoom 0.4

            sol "Well, I’m sorry but I heard everything."

            prota "Amazing."

            sol "I think I haven’t talk to you in all those years of school, right?"

            "She’s right. We have not talked. We have barely shared some subjects. But she’s so shiny, and happy, and full of life that it’s hard to not know her."

            "Well, since she heard all the conversation, I can ask her what she thinks about this all confess-my-love-thing."

            prota "We have not, but is never late, right? I’m [name]."

            hide soltriste
            show solneutral:
                xalign 0.5
                yalign 1.0
                zoom 0.4

            sol "I’m Sol!"

            prota "Hey, Sol. As you heard the whole thing, maybe you could help me with some advice."

            "She smiles quite more, as if it were possible."

            hide solneutral
            show solfeliz:
                xalign 0.5
                yalign 1.0
                zoom 0.4

            sol "Yes, yes! Tell me!"

            "I tell her everything that happened that day. How confused I am. But I’m not confused about whom I like, I’m confused about telling her or not."

            "I feel so relief. She just listens and nods."

            "She’s so full of shine."

            hide solfeliz
            show solneutral:
                xalign 0.5
                yalign 1.0
                zoom 0.4

            sol "Look, [name]. I think you should do this anyway. You should tell her. We’re young."

            prota "So, wait, does it matter if we’re young?"

            hide solneutral
            show solasustada:
                xalign 0.5
                yalign 1.0
                zoom 0.4

            sol "Of course it does! Do you think you’ll be allow to make mistakes or teenage stuff when you get 30?, 40?"

            hide solasustada
            show solneutral:
                xalign 0.5
                yalign 1.0
                zoom 0.4

            sol "We have to take advantage of our time now that we can, right?"

            prota "Oh god you’re absolutely right."

            hide solneutral
            show solfeliz:
                xalign 0.5
                yalign 1.0
                zoom 0.4

            "We high five, and Sol laughs. She’s cool."

            "I don’t know how, but we end up exchanging our phone numbers and our Tuiter accounts."

            "She’s so genuine."

            prota "So, I have to go. I’m sorry we had to meet at the end of this cycle."

            sol "You’re right. We can keep in touch anyway!"

        menu:
            "Are you sure about that?":
                jump choice22

            "You’re absolutely right.":
                jump choice23

        label choice22:

            prota "Well I’m not even going to study in this city, so…"

            hide solfeliz
            show solneutral:
                xalign 0.5
                yalign 1.0
                zoom 0.4

            sol "Don’t worry! We’ll figure out how to meet!"

            jump choice11_done

        label choice23:

            prota "Yes! And we can watch 90s movies!"

            sol "Ohhh, awesome, please!"

            jump choice11_done

        label choice11_done:

            hide solfeliz with dissolve
            hide solneutral with dissolve

            "Sol is gone. Is nothing else to do here."

    label escenaJUNE:

        scene basket with fade

        "Well, I’ve gone this far and I still I haven’t made a choice."

        "It’s just that… everything is so complicated. I have to think about a lot of stuff."

        "Like, I can lose my job, my family, friends, if I just tell her I like her?"

        "But then I can be truly myself."

        "I have to think carefully about what’s more important for me. My identity or my beloved ones."

        prota "OH GOD NO."

        prota "WHY THIS HAS TO HAPPEN NOW"

        "June is there. She’s putting some books in her bag."

        "Oh god she’s so pretty-"

        "Wait."

        "…"

        "She’s coming in this direction."

        prota "Oh no oh no oh no ohhhhh noooooooooo"

        "WHAT SHOULD I DO FOR VIKTOR’S HEELS."

        "This is my last choice. My last chance."

        "I have to choose!"

        menu:
            "Confess my love.":
                jump choice24

            "Don’t confess my love.":
                jump choice25

        label choice24:

            prota "Well, I’ll go for it."

            "I walk to June and put a hand in her shoulder. She turns back, astonished."

            prota "Hi. There’s something I have to tell you."

            june "Yes?"

            prota "Actually, there’s something I have to confess."

            jump escenafinaljune

    label escenafinaljune:

        marcos "Uh?"

        marcos "Why is [name] sending me a letter?"

        marcos "Is like we lived in XVIII century."

        marcos "What a waste of paper."

        marcos "Anyway, time to read this."

        prota "Hey Marcos!"

        prota "I hope you’re having a great time in Munich."

        prota "I’m sending this letter because I had a revelation about what you said. About that promise and stuff."

        prota "So, after hearing many other opinions, I decided to confess to this girl."

        prota "And we have went in a few dates!"

        prota "I’ve thought about it, and I don’t need to hide myself anymore."

        prota "No with you, Alan, Sol, and other supporting me."

        prota "Sure there’s people who thinks I‘m a failure. That I need to be fixed or something. And I tell them: there’s nothing to fix. This is me."

        prota "And I’m loved."

        prota "I just wanted you to know that, there’s a lot of people like me, like us, around the globe."

        prota "And we have been hiding for a lot of time. We don’t have to do that anymore."

        prota "Love, [name]."

        jump credits


    label choice25:

        prota "Ok, ok, let her pass."

        "June walks next to me. I watch her passing."

        "She jumps into a car."

        "I don’t know why, buy I don’t feel anxious anymore. But..."

        "At the same time, there’s something inside of me that’s hurting."

        "What is this feeling?"

        jump choicewrongfinal

    label choicewrongfinal:

        marcos "[name]?"

        marcos "I know you might see this in the morning, that’s late over there, and I’m sorry, but please, pay attention."

        marcos "You don’t have to hide yourself."

        marcos "Even if it’s online, I’m here for you, and I support you and who you really are."

        marcos "Sweetie, there’s people like you, like me, around the entire world."

        marcos "If your environment is not safe, maybe it’s ok if you take care of yourself and decide to hide a little bit until you can get safer surroundings."

        marcos "But it’s not your case, [name]. Alan, your family and I, we all support you. We love you."

        marcos "Sure, there’s people who thinks that we should be in a mental hospital, but they are living in the past. We’re the future."

        marcos "Anyway."

        marcos "I’m here for you, and if I’m not available at the moment, there’s plenty of people who would help you."

        marcos "Love, your best friend."

        jump credits


    label credits:
        return
