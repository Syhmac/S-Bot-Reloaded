import random

class JOB:
    def __init__(self, job_id, min_earnings, max_earnings, min_tips = 0, max_tips = 0):
        self.job_id = job_id
        self.min_earnings = min_earnings
        self.max_earnings = max_earnings
        self.min_tips = min_tips
        self.max_tips = max_tips

    def calculateEarnings(self):
        # Calculate earnings based on the range
        return random.randint(self.min_earnings, self.max_earnings)

    def calculateTips(self):
        # Calculate tips based on the range
        return random.randint(self.min_tips, self.max_tips)

# Job definitions
JOB_LIST = {
    1: JOB('fastfood', 10, 50),
    2: JOB('retail', 15, 60),
    3: JOB('coffee', 10, 50, 1, 20),
    4: JOB('delivery', 20, 70, 1, 25),
    5: JOB('programming', 200, 500),
    6: JOB('ticket_inspector', 15, 40),
    7: JOB('lawn_mowing', 5, 30, 1, 10),
    8: JOB('dog_walking', 5, 25, 1, 10),
    9: JOB('babysitting', 10, 40, 3, 15),
    10: JOB('house_cleaning', 10, 50, 5, 20),
    11: JOB('car_washing', 5, 30, 1, 10),
    12: JOB('pc_repair', 20, 100),
    13: JOB('tutoring', 15, 60, 1, 20),
    14: JOB('office', 20, 80),
    15: JOB('bartender', 15, 50, 1, 25),
    16: JOB('waiter', 10, 40, 1, 15),
    17: JOB('security_guard', 20, 70),
    18: JOB('event_staff', 10, 50),
    19: JOB('garbage_collector', 10, 40),
    20: JOB('translator', 20, 80),
    21: JOB('taxi', 15, 60, 1, 20),
    22: JOB('convenience_store', 10, 40),
    23: JOB('art', 50, 200),
    24: JOB('blog_writing', 20, 100),
    25: JOB('call_center', 10, 40),
    26: JOB('gardening', 5, 30, 1, 10),
    27: JOB('3d_printing', 10, 60),
    28: JOB('photography', 20, 100),
    29: JOB('chef', 30, 90),
    30: JOB('youtube', 1, 200),
    31: JOB('streaming', 1, 250),
    32: JOB('police', 20, 80),
    33: JOB('firefighter', 20, 80),
    34: JOB('paramedic', 20, 80),
    35: JOB('teacher', 15, 70),
    36: JOB('bus_driver', 10, 50),
    37: JOB('train_conductor', 15, 60),
    38: JOB('train_driver', 20, 80),
    39: JOB('pilot', 50, 200),
    40: JOB('astronaut', 300, 700),
    41: JOB('tram_driver', 20, 60),
    42: JOB('drop_shipping', 10, 50),
    43: JOB('veterinarian', 30, 100),
    44: JOB('animal_shelter_volunteer', 0, 0),
    45: JOB('truck_driver', 40, 120),
    46: JOB('electrician', 30, 100),
    47: JOB('plumber', 30, 100),
    48: JOB('carpenter', 25, 90),
    49: JOB('door_sales', 10, 50),
    50: JOB('street_performance', 5, 30),
    51: JOB('farming', 10, 60),
    52: JOB('hand_craft', 15, 70),
    53: JOB('car_rental', 20, 80),
    54: JOB('moving_service', 30, 100),
    55: JOB('software_testing', 20, 80),
    56: JOB('survey_taking', 5, 25),
    57: JOB('zoo_keeper', 15, 60),
    58: JOB('museum_guide', 20, 80),
    59: JOB('fandub', 10, 50),
    60: JOB('voice_acting', 20, 100),
    61: JOB('hot_dog_stand', 5, 30),
    62: JOB('ice_cream_truck', 10, 50),
    63: JOB('hotel_receptionist', 15, 60),
    64: JOB('pool_lifeguard', 10, 40),
    65: JOB('personal_maid', 60, 140),
}