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
    def __init__(self, text, cps=25, **properties):

        super(BootingMessage, self).__init__()

        # Store original arguments for recreating the Text child later
        self.textList = text
        self.cps = cps
        self.original_properties = properties

        self.reset()

    def display(self, st, at):
        """Create a new Text object with the current CPS."""
        newst = 1. / self.cps

        ret = Text(self.originalText[0:self.displayedLength], **self.original_properties)
        if self.displayedLength < len(self.originalText):
            if (self.start_st is None) or (st - self.current_st > newst):
                self.displayedLength+=1
                self.current_st = st
            if (self.start_st is None):
                self.start_st = st
            st = newst
        else:
            st = None

        return ret, st

    def reset(self):
        """Update the displayable to show the text at the new CPS."""
        self.displayedLength = 0
        self.textIndex = 0
        self.originalText = self.textList[0]
        self.start_st = None

        # The "start time" of the animation
        self.start_st = None
        # The current st of the animation
        self.current_st = 0

    def switch(self):
        if self.textIndex < len(self.textList):
            self.textIndex += 1
            self.originalText += self.textList[self.textIndex]
            self.start_st = None

bootingMessage1 = "Atremius systems\nRevision 800 model H.A.C.K.E.R.\nversion 2.4\n"
bootingMessage2 = "\nRegistering new master..."
bootingMessage3 = "\nNew quest accepted.\nTime flies like an arrow..."
bootingMessage4 = "\nExecuting runtime bugfixes..."
bootingMessage5 = "\nTraversing word trie..."
bootingMessage6 = " Done."
bootingMessage7 = "\n\nAccepting 'Rosalind' as instance identifier."
bootingMessage8 = "\nGenerating nerve tissues..."
bootingMessage9 = "\nLearning to move muscles..."
bootingMessageA = "\n\nInitial setup complete."
bootingMessageList = [
    bootingMessage1, bootingMessage2, bootingMessage3,
    bootingMessage4, bootingMessage5, bootingMessage6,
    bootingMessage7, bootingMessage8, bootingMessage9,
    bootingMessageA
    ]

bootingMessageText = BootingMessage(bootingMessageList, cps=15, font="terminat.ttf", size=30)
