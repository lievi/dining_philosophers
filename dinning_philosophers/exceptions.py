class BasePhilosophersException(Exception):
    ...


class PhilosopherWithSameIdException(BasePhilosophersException):
    def __init__(self) -> None:
        self.message = 'Id already used for another philosopher'
        super().__init__(self.message)
