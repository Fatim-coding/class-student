# create class
class Vehicle:

    # create init meathod
      def __init__(self, max_speed, mileage):
            
      # blind the arguments
           self.max_speed = max_speed
           self.mileage = mileage

# object creation
modelx = Vehicle(240, 18)

# access the variables inside init method
print("Model max speed:",modelx.max_speed)
print("Model mileage:", modelx.mileage)