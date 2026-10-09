""" Build a Travel Weather Planner
For this lab, you will use conditional statements to determine whether commuting is possible based on the weather, the distance to travel, and the availability of a vehicle.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab. """

distance_mi = 0
is_raining = False
has_bike = False
has_car = False
has_ride_share_app = False

if not distance_mi:
    print(False)
elif distance_mi <= 1 and not is_raining:
    print(True)
elif 1 < distance_mi <= 6 and has_bike and not is_raining:
    print(True)
elif distance_mi > 6 and has_ride_share_app:
    print(True)
elif distance_mi > 6 and has_car:
    print(True)

else:
    print(False)
