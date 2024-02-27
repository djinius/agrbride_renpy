default buildings = []
#    [None, None, None, None, None, None, None, None, None, None, None, "lodge", "castle", False, "maintree", False, "workshop", "barn", "winery", None],
#    [None, None, None, None, None, None, None, None, None, None, "ricetree", "meattree", "ricetree", "ricetree", "appletree", "appletree", None, None, None, None],
#    [None, None, None, None, None, None, None, None, None, None, None, None, "appletree", "appletree", "grapetree", None, None],
#    [None, None, None, None, None, None, None, None, None, "appletree", "appletree", "appletree", "appletree", "appletree", "appletree", "appletree", "appletree", "appletree", "appletree"],
#    [None, None, None, None, None, None, None, None, None, "appletree", "appletree", "appletree", "appletree", "appletree", "appletree", "appletree", "appletree", "appletree"],
#    [None, None, None, None, None, None, None, None, None, None, None, "peachtree", "meattree", "ricetree", "grapetree", "grapetree", "teatree"],
#    [None, None, None, None, None, None, None, None, None, "busstop", "pension", "cocktailbar"]
#]

define consultant = [("말리 SD", "maliTeaEvent"), ("로잘린드 SD", "rosalindChoice"), ("세라 SD", None), ("카라 SD", "charaCakeEvent"), ("만다 SD", "mandaGymEvent"), ("루시 SD", None), ("보미 SD", None)]
define buildingButtons = [["appletree", "grapetree", "peachtree"], ["hive"]]

default cityZoom=cityMinZoom()
default edgeScroll=False
default cityCells = (31, 15)

transform placeButton:
    on idle:
        alpha 1.
    on hover:
        linear .5 alpha .0
        linear .5 alpha 1.
        repeat

transform bulidingButton:
    on idle:
        linear .25 zoom 1.
    on hover:
        linear .25 zoom 1.1

screen city:
    default s = None
    default toPlace = None

    viewport id "vp":
        if edgeScroll:
            edgescroll (200, 400, scrollSpeed)
            
        draggable True
        mousewheel True
        xinitial .5 yinitial .0

        frame:
            xysize citySize(cityCells, cityZoom)
            background None
            for (y, row) in enumerate(buildings):
                for (x, b) in enumerate(row):
                    if x >= getColLimit(cityCells[0], y):
                        pass
                    elif b is None:
                        imagebutton:
                            idle Solid("#400")
                            xysize (int(256*cityZoom), int(256*cityZoom))
                            pos calcXYPos(x, y, cityZoom) anchor (.5, .75)
                            if toPlace is None:
                                hover Solid("#330")
                                action NullAction()
                            else:
                                hover Transform(toPlace, zoom=cityZoom*.5)
                                action Function(addBuilding, x=x, y=y, bd=toPlace)
                            at placeButton
                    elif b is not False:
                        imagebutton:
                            idle Transform(b, zoom=cityZoom*.5)
                            hover Transform(b, zoom=cityZoom*.5)
                            pos calcXYPos(x, y, cityZoom) anchor (.5, .75)
                            if toPlace is None:
                                at bulidingButton
                                action NullAction()
                            else:
                                action NullAction()

    vbox:
        align (1., 1.)

        if s is not None:
            add s xalign 1. zoom .5

        hbox:
            xalign 1.
            for (n, (c, e)) in enumerate(consultant):
                imagebutton:
                    idle Transform(c, zoom=.1)
                    if e is None:
                        action NullAction()
                    else:
                        action Call(e)

                    hovered SetLocalVariable("s", c)
                    unhovered SetLocalVariable("s", None)

    hbox:
        align (.0, 1.)

        for bcol in buildingButtons:
            vbox:
                yalign 1.
                for b in bcol:
                    textbutton b:
                        action SetLocalVariable("toPlace", b)

        textbutton "읍내":
            action Call("visitTown")
            yalign 1.

        textbutton "메뉴":
            action ShowMenu()
            yalign 1.

    if toPlace is None:
        hbox:
            align (0., 0.)
            add "effectNewTreeGrowing"
            add "effectNewBudGrowing"
    else:
        text toPlace align (0., 0.)


    key "mousedown_5" action SetVariable("cityZoom", min(1., cityZoom+.05))
    key "mousedown_4" action SetVariable("cityZoom", max(cityMinZoom(cityCells), cityZoom-.05))
    key "game_menu" action SetLocalVariable("toPlace", None)

        
