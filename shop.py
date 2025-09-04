# building a multi elevator control system
# four classes: elevator, passanger

class Building:
    def __init__(self, num_elevators, num_floors, elevators):
        self.num_elevators = num_elevators
        self.num_floors = num_floors
        self.elevators = elevators
        
    def get_elevator(self, passenger):
        # closest elevator going in the same direction as the passenger
        for elevator in self.elevators:
            if elevator.direction == passenger.direction:
                return elevator
        return self.elevators[0]
    
    def elevator_transit(self, passenger):
        relevant_elevator = self.get_elevator(passenger)
        print(relevant_elevator.current_floor)
        relevant_elevator.move(passenger.destination_floor)
        passenger.current_floor = relevant_elevator.current_floor
        passenger.direction = "up" if relevant_elevator.direction == "up" else "down"
            
class Elevator:
    def __init__(self, id, current_floor, max_floor, direction):
        self.id = id
        self.current_floor = current_floor
        self.max_floor = max_floor
        self.direction = direction
        self.passengers = []
        
    def move(self, destination_floor):
        self.current_floor = destination_floor
        self.direction = "up" if self.direction == "down" else "down"

class Passenger:
    def __init__(self, id, current_floor, destination_floor, direction):
        self.id = id
        self.current_floor = current_floor
        self.destination_floor = destination_floor
        self.direction = direction

elevators = [Elevator(1, 0, 10, "up"), Elevator(2, 0, 10, "up"), Elevator(3, 0, 10, "up")]
building = Building(3, 10, elevators)

tom = Passenger(1, 0, 10, "up")
building.elevator_transit(tom)
print(tom.current_floor)
print(tom.direction)
print(tom.destination_floor)
# chosen elevator goes to the destination floor
# update states of that elevator during that transit
