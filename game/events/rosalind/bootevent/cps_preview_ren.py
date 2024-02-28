"""renpy
init -1 python:
"""

class PreviewSlowText(renpy.Displayable):
    """
    A class to display a preview of the current CPS settings.

    Attributes:
    -----------
    text : string
        The text to display for this displayable preview.
    properties : dict
        Optional keyword arguments that will be applied to the text
        to style it.
    """
    def __init__(self, text, **properties):

        super(PreviewSlowText, self).__init__()

        # Store original arguments for recreating the Text child later
        self.originalText = text
        self.original_properties = properties

        # Text displayable that represents PreviewSlowText.
        self.current_child = self.new_text()

        # The "start time" of the animation
        self.start_st = None
        # The current st of the animation
        self.current_st = 0

    def new_text(self):
        """Create a new Text object with the current CPS."""

        return Text(self.originalText, slow_cps=preferences.text_cps, **self.original_properties)

    def update_cps(self):
        """Update the displayable to show the text at the new CPS."""
        self.current_child = self.new_text()
        self.start_st = self.current_st

    def render(self, width, height, st, at):
        """Render the text to the screen."""

        # Record when this animation is starting
        if self.start_st is None:
            self.start_st = st
        # Keep track of the current st
        self.current_st = st

        # Trigger this function again when possible,
        # to test and/or update all of this stuff again.
        renpy.redraw(self, 0)

        # Create a render (canvas).
        render = renpy.Render(width, height)

        # Calculate the "virtual" start time
        new_st = st - self.start_st

        # Place the Text child onto it, with the adjusted st
        render.place(self.current_child, st=new_st, at=at)

        # Return the render.
        return render

class BootingMessage():
    """
    A class to display a preview of the current CPS settings.

    Attributes:
    -----------
    text : string
        The text to display for this displayable preview.
    properties : dict
        Optional keyword arguments that will be applied to the text
        to style it.
    """
    def __init__(self, cps=25, **properties):

        super(BootingMessage, self).__init__()

        # Store original arguments for recreating the Text child later
        self.text = ""
        self.cps = cps
        self.cursor = True
        self.original_properties = properties

        self.reset()

    def display(self, st, at):
        """Create a new Text object with the current CPS."""
        newst = 1. / self.cps

        ret = self.originalText[0:self.displayedLength]
        if self.displayedLength < len(self.originalText):
            if (self.start_st is None) or (st - self.current_st > newst):
                self.displayedLength+=1
                self.current_st = st
            if (self.start_st is None):
                self.start_st = st
            st = newst
            ret += "{image=events/rosalind/bootevent/cursor.png}"
            self.cursor = True
        else:
            if st - self.current_st > .5:
                if self.cursor:
                    ret += "{image=events/rosalind/bootevent/cursor.png}"
                self.cursor = not self.cursor
                self.current_st = st

            st = .5

        return Text(ret, **self.original_properties), st

    def reset(self, text=""):
        """Update the displayable to show the text at the new CPS."""
        self.displayedLength = 0
        self.textIndex = 0
        self.originalText = text
        self.start_st = None

        # The "start time" of the animation
        self.start_st = None
        # The current st of the animation
        self.current_st = 0

    def appendText(self, text):
        self.originalText += text
        lineFeedCount = self.originalText.count('\n')
        while lineFeedCount > 8:
            firstLF = self.originalText.index('\n')
            self.originalText = self.originalText[(firstLF + 1):]
            self.displayedLength -= firstLF + 1
            lineFeedCount = self.originalText.count('\n')
        self.start_st = None

bootingMessageText = BootingMessage(cps=15, font="terminat.ttf", size=30)
