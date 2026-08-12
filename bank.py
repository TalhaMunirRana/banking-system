class Bank():
    """A Simple attempt to model a Bank"""

    def __init__(self, name):
        """Initialize the attirbutes for bank."""
        self.name = name
        self.customers = []
        self.accounts = []