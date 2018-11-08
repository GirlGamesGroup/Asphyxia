# Screens para elegir personaje

screen body1():
    frame:
        xpos 1280 ypos 70
        background "CUERPO_DEFAULT_01.png"

screen body2():
    frame:
        xpos 1280 ypos 70
        background "CUERPO_DEFAULT_02.png"

screen body3():
    frame:
        xpos 1280 ypos 70
        background "CUERPO_DEFAULT_03.png"

####

screen hair1():
    frame:
        xpos 1280 ypos 70
        background "PELO_DEFAULT_CORTO_MARRON.png"

screen hair2():
    frame:
        xpos 1280 ypos 70
        background "PELO_DEFAULT_MEDIO_MARRON.png"

screen hair3():
    frame:
        xpos 1280 ypos 70
        background "PELO_DEFAULT_LARGO_MARRON.png"

screen hair4():
    frame:
        xpos 1280 ypos 70
        background "PELO_DEFAULT_LARGO_MARRON_C03.png"

################################################

screen customization():
    image "PERSONALIZACION_FONDO.png"
    image "PERSONALIZACION_CUADRO_PERSONAJE.png"
    image "PERSONALIZACION_TEXTO.png"

screen vestuario1():
    #BODY
    imagebutton:
        xpos 300 ypos 500
        idle "PERSONALIZACION_OPCION_01.png"
        hover "PERSONALIZACION_OPCION_01_SELECCIONADO.png"
        hovered [Show("body1"), Hide("body2"), Hide("body3")]
        action [SetVariable("bodytype", 1), Notify(_("Body type selected."))]

    imagebutton:
        xpos 500 ypos 500
        idle "PERSONALIZACION_OPCION_02.png"
        hover "PERSONALIZACION_OPCION_02_SELECCIONADO.png"
        hovered [Show("body2"), Hide("body1"), Hide("body3")]
        action [SetVariable("bodytype", 2), Notify(_("Body type selected."))]

    imagebutton:
        xpos 700 ypos 500
        idle "PERSONALIZACION_OPCION_03.png"
        hover "PERSONALIZACION_OPCION_03_SELECCIONADO.png"
        hovered [Show("body3"), Hide("body2"), Hide("body1")]
        action [SetVariable("bodytype", 3), Notify(_("Body type selected."))]

    #DONE
    if bodytype != 0:
        imagebutton:
            xpos 600 ypos 900
            idle "PERSONALIZACION_FLECHA_DER.png"
            hover "PERSONALIZACION_FLECHA_DER.png"
            action [Hide("vestuario1"), Show("vestuario2")]


screen vestuario2():
    #HAIR
    imagebutton:
        xpos 200 ypos 500
        idle "PERSONALIZACION_OPCION_PELO_CORTO.png"
        hover "PERSONALIZACION_OPCION_PELO_CORTO_SELECCIONADO.png"
        hovered [Show("hair1"), Hide("hair2"), Hide("hair3"), Hide("hair4")]
        action SetVariable("hairlenght", 1)

    imagebutton:
        xpos 500 ypos 500
        idle "PERSONALIZACION_OPCION_PELO_MEDIO.png"
        hover "PERSONALIZACION_OPCION_PELO_MEDIO_SELECCIONADO.png"
        hovered [Show("hair2"), Hide("hair1"), Hide("hair3"), Hide("hair4")]
        action SetVariable("hairlenght", 2)

    if bodytype == 1:
        imagebutton:
            xpos 800 ypos 500
            idle "PERSONALIZACION_OPCION_PELO_LARGO.png"
            hover "PERSONALIZACION_OPCION_PELO_LARGO_SELECCIONADO.png"
            hovered [Show("hair4"), Hide("hair2"), Hide("hair3"), Hide("hair1")]
            action SetVariable("hairlenght", 3)

    else:
        imagebutton:
            xpos 800 ypos 500
            idle "PERSONALIZACION_OPCION_PELO_LARGO.png"
            hover "PERSONALIZACION_OPCION_PELO_LARGO_SELECCIONADO.png"
            hovered [Show("hair3"), Hide("hair2"), Hide("hair1"), Hide("hair4")]
            action SetVariable("hairlenght", 3)

    #DONE
    if bodytype!=0 and hairlenght!=0:
        imagebutton:
            xpos 1400 ypos 900
            idle "PERSONALIZACION_CUADRO_LETS GO.png"
            hover "PERSONALIZACION_CUADRO_LETS GO.png"
            action [SetVariable("done", True), Notify(_("You are ready.")), Jump("escena1"), Hide("customization"), Hide("vestuario1"), Hide("vestuario2"), Hide("vestuario3")]

# Screens para elegir interes amoroso

screen junepic():
    frame:
        ypos 100 xpos 400
        background "notijude.png"

screen marapic():
    frame:
        ypos 100 xpos 400
        background "notimara.png"

screen sugarpic():
    frame:
        ypos 100 xpos 400
        background "notisugar.png"

screen notifications:
    imagebutton:
        xpos 1700 ypos 210

        idle "CELLPHONE_OPCION_01.png"
        hover "CELLPHONE_OPCION_01_SELECCIONADO.png"
        hovered [Jump("choosegirl1")]
        unhovered [Hide("junepic")]
        action NullAction()

    imagebutton:
        xpos 1700 ypos 300

        idle "CELLPHONE_OPCION_02.png"
        hover "CELLPHONE_OPCION_02_SELECCIONADO.png"
        hovered [Jump("choosegirl2")]
        unhovered [Hide("marapic")]
        action NullAction()

    imagebutton:
        xpos 1700 ypos 390

        idle "CELLPHONE_OPCION_03.png"
        hover "CELLPHONE_OPCION_03_SELECCIONADO.png"
        hovered [Jump("choosegirl3")]
        unhovered [Hide("sugarpic")]
        action NullAction()

    imagebutton:
        xpos 1750 ypos 500
        idle "flecha.png"
        action [Hide("notifications"), Hide("cellphone.png"), Hide("junepic"), Hide("marapic"), Hide("sugarpic"), Jump("choosegirldone")]


screen finaljune():
    frame:
        if bodytype == 1:
            if hairlenght == 1:
                xalign 0.5
                image "junepelocorto.jpg"
                background "junecgrande.jpg"

            elif hairlenght == 2:
                xalign 0.5
                image "junepelomedio.jpg"
                background "junecgrande.jpg"

            elif hairlenght == 3:
                xalign 0.5
                image "junepelolargo.jpg"
                background "junecgrande.jpg"

        elif bodytype == 2:
            if hairlenght == 1:
                xalign 0.5
                image "junepelocorto.jpg"
                background "junecmedio.jpg"

            elif hairlenght == 2:
                xalign 0.5
                image "junepelomedio.jpg"
                background "junecmedio.jpg"

            elif hairlenght == 3:
                xalign 0.5
                image "junepelolargo.jpg"
                background "junecmedio.jpg"

        elif bodytype == 3:
            if hairlenght == 1:
                xalign 0.5
                image "junepelocorto.jpg"
                background "junecflaco.jpg"

            elif hairlenght == 2:
                xalign 0.5
                image "junepelomedio.jpg"
                background "junecflaco.jpg"

            elif hairlenght == 3:
                xalign 0.5
                image "junepelolargo.jpg"
                background "junecflaco.jpg"


screen finalmara():
    frame:
        if bodytype == 1:
            if hairlenght == 1:
                xalign 0.5
                image "marapelocorto.jpg"
                background "maracgrande.jpg"

            elif hairlenght == 2:
                xalign 0.5
                image "marapelomedio.jpg"
                background "maracgrande.jpg"

            elif hairlenght == 3:
                xalign 0.5
                image "marapelolargo.jpg"
                background "maracgrande.jpg"

        elif bodytype == 2:
            if hairlenght == 1:
                xalign 0.5
                image "marapelocorto.jpg"
                background "maracmedio.jpg"

            elif hairlenght == 2:
                xalign 0.5
                image "marapelomedio.jpg"
                background "maracmedio.jpg"

            elif hairlenght == 3:
                xalign 0.5
                image "marapelolargo.jpg"
                background "maracmedio.jpg"

        elif bodytype == 3:
            if hairlenght == 1:
                xalign 0.5
                image "marapelocorto.jpg"
                background "maracflaco.jpg"

            elif hairlenght == 2:
                xalign 0.5
                image "marapelomedio.jpg"
                background "maracflaco.jpg"

            elif hairlenght == 3:
                xalign 0.5
                image "marapelolargo.jpg"
                background "maracflacojpg"



screen finalsugar():
    frame:
        if bodytype == 1:
            if hairlenght == 1:
                xalign 0.5
                image "sugarpelocorto.jpg"
                background "sugarcgrande.jpg"

            elif hairlenght == 2:
                xalign 0.5
                image "sugarpelomedio.jpg"
                background "sugarcgrande.jpg"

            elif hairlenght == 3:
                xalign 0.5
                image "sugarpelolargo.jpg"
                background "sugarcgrande.jpg"

        elif bodytype == 2:
            if hairlenght == 1:
                xalign 0.5
                image "sugarpelocorto.jpg"
                background "sugarcmedio.jpg"

            elif hairlenght == 2:
                xalign 0.5
                image "sugarpelomedio.jpg"
                background "sugarcmedio.jpg"

            elif hairlenght == 3:
                xalign 0.5
                image "sugarpelolargo.jpg"
                background "sugarcmedio.jpg"

        elif bodytype == 3:
            if hairlenght == 1:
                xalign 0.5
                image "sugarpelocorto.jpg"
                background "sugarcflaco.jpg"

            elif hairlenght == 2:
                xalign 0.5
                image "sugarpelomedio.jpg"
                background "sugarcflaco.jpg"

            elif hairlenght == 3:
                xalign 0.5
                background "CUERPO_DEFAULT_01.png"
