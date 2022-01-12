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

    def __init__(self, cruise_control_enabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.cruise_control_enabled = cruise_control_enabled

    def display(self):
        print(self.cruise_control_enabled)

    def drive(self):
        print("Three Series is being driven")

    def start(self):
        super().start()
        print("Start button")

    def stop(self):
        super().stop()
        print("Stop button")


class FiveSeries(BMW):

    def __init__(self, parking_assist_enabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.parking_assist_enabled = parking_assist_enabled

    def drive(self):
        print("Five Series is being driven")

    def start(self):
        super().start()
        print("Remote start")

    def stop(self):
        super().stop()
        print("Remote stop")


def main():
    three_series = ThreeSeries(True, "BMW", "328i", "2018")
    print(three_series.cruise_control_enabled)
    print(three_series.make)
    print(three_series.model)
    print(three_series.year)

    three_series.start()
    three_series.stop()
    three_series.display()

    five_series = FiveSeries(True, "BMW", "520d", "2021")
    print(five_series.parking_assist_enabled)
    print(five_series.make)
    print(five_series.model)
    print(five_series.year)

    five_series.start()
    five_series.stop()
    five_series.drive()


if __name__ == "__main__":
    main()
