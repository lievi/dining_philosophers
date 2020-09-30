class BasePhilosophersException(Exception):
    ...


class PhilosopherWithSameIdException(BasePhilosophersException):
    def __init__(self) -> None:
        self.message = 'Id already used for another philosopher'
        super().__init__(self.message)


class PhilosopherWithMoreThanTwoForksException(BasePhilosophersException):
    def __init__(self) -> None:
        self.message = 'More than two neighbor forks'
        super().__init__(self.message)
