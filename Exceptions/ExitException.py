class ExitException(Exception):
    def __init__(self):
        super().__init__("Exiting app")
