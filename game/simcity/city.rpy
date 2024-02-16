define buildings = [
    [None, "ricetree", "castle", None, "maintree", None, "workshop", "hive", None, None],
    [None, "ricetree", "meattree", "ricetree", "hive", "appletree", "appletree", None, None, None, None],
    [None, None, None, "appletree", "appletree", "workshop", None, None],
    ["appletree", "appletree", "appletree", "appletree", "appletree", "appletree", "appletree", "appletree", "appletree", "appletree"],
    ["appletree", "appletree", "appletree", "appletree", "appletree", "appletree", "appletree", "appletree", "appletree"],
    [None, None, "ricetree", "meattree", "ricetree", "grapetree", "grapetree", "teatree"]
]

define consultant = ["말리 SD", "로잘린드 SD", "세라 SD", "카라 SD", "만다 SD", "루시 SD"]

default cityZoom=.64
default edgeScroll=False

screen city:
    default s = None

    viewport id "vp":
        if edgeScroll:
            edgescroll (200, 400, scrollSpeed)
            
        draggable True
        mousewheel True
        xinitial .5 yinitial .0

        frame:
            xysize (int(3000*cityZoom), int(1800*cityZoom))
            background None
            for (y, row) in enumerate(buildings):
                for (x, b) in enumerate(row):
                    if b is not None:
                        add b:
                            pos calcXYPos(x, y, cityZoom) anchor (.5, .5)
                            zoom cityZoom*.5

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
                    else:
                        action NullAction()
                    hovered SetLocalVariable("s", c)
                    unhovered SetLocalVariable("s", None)

    key "mousedown_5" action SetVariable("cityZoom", min(1., cityZoom+.05))
    key "mousedown_4" action SetVariable("cityZoom", max(1920./3000, cityZoom-.05))

        
