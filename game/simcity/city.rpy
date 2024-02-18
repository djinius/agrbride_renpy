default buildings = []
#    [None, None, None, None, None, None, None, None, None, None, None, "lodge", "castle", False, "maintree", False, "workshop", "barn", "winery", None],
#    [None, None, None, None, None, None, None, None, None, None, "ricetree", "meattree", "ricetree", "ricetree", "appletree", "appletree", None, None, None, None],
#    [None, None, None, None, None, None, None, None, None, None, None, None, "appletree", "appletree", "grapetree", None, None],
#    [None, None, None, None, None, None, None, None, None, "appletree", "appletree", "appletree", "appletree", "appletree", "appletree", "appletree", "appletree", "appletree", "appletree"],
#    [None, None, None, None, None, None, None, None, None, "appletree", "appletree", "appletree", "appletree", "appletree", "appletree", "appletree", "appletree", "appletree"],
#    [None, None, None, None, None, None, None, None, None, None, None, "peachtree", "meattree", "ricetree", "grapetree", "grapetree", "teatree"],
#    [None, None, None, None, None, None, None, None, None, "busstop", "pension", "cocktailbar"]
#]

define consultant = ["말리 SD", "로잘린드 SD", "세라 SD", "카라 SD", "만다 SD", "루시 SD"]
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
        repeat

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
                            idle Solid("#F00")
                            xysize (int(256*cityZoom), int(256*cityZoom))
                            pos calcXYPos(x, y, cityZoom) anchor (.5, .75)
                            if toPlace is None:
                                hover Solid("#FF0")
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
            for (n, c) in enumerate(consultant):
                imagebutton:
                    idle Transform(c, zoom=.1)
                    if n == 0:
                        action Call("maliTeaEvent")
                    elif n == 3:
                        action Call("charaCakeEvent")
                    else:
                        action NullAction()
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

    if toPlace is None:
        text "None" align (0., 0.)
    else:
        text toPlace align (0., 0.)


    key "mousedown_5" action SetVariable("cityZoom", min(1., cityZoom+.05))
    key "mousedown_4" action SetVariable("cityZoom", max(cityMinZoom(cityCells), cityZoom-.05))
    key "game_menu" action SetLocalVariable("toPlace", None)

        
