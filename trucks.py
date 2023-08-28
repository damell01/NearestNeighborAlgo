class Truck:
    def __init__(self):
        self.current_location = 'HUB'
        self.route = []

    def load(self, package):
        self.route.append(package)
        # Implement package loading logic here

    def deliver(self):
        # Implement package delivery logic here