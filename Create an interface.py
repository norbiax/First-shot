from abc import abstractmethod, ABC
class BMW(ABC):

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

class ThreeSeries(BMW):

    def __init__(self, cruiseControlEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled

    def display(self):
        print(self.cruiseControlEnabled)

    def drive(self):
        print("ThreeSeries is being driven")

    def start(self):
        super().start()
        print("Start button")

    def stop(self):
        super().stop()
        print("Stop button")

class FiveSeries(BMW):

    def __init__(self, parkingAssistEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled

    def drive(self):
        print("FiveeSeries is being driven")

    def start(self):                                                    
        super().start()
        print("Remote start")

    def stop(self):
        super().stop()
        print("Remote stop")

threeseries = ThreeSeries(True, "BMW", "328i", "2018")
print(threeseries.cruiseControlEnabled)
print(threeseries.make)
print(threeseries.model)
print(threeseries.year)

threeseries.start()
threeseries.stop()
threeseries.display()

fiveSeries = FiveSeries(True, "BMW", "328i", "2018")
