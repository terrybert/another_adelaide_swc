# tag id: A8025
# size
# sigthing per month

# is_large (lage means > 5 oz)
# is_small (small means < 3oz)
# capture

class Rodent:
    def __init__(self, tag_id, size):
        self.tag_id=tag_id
        self.size=size
        self.sightings_per_month={}

    def is_large(self): #self refers to the class Rodent
        return (self.size > 5)
        pass

    def is_small(self):
        return (self.size < 3)
        pass

    def plot(self):
        return self.tag_id[0]
        pass

    def capture(self, month):
        # we captured this rodent once this month
        if month not in self.sightings_per_month:
            self.sightings_per_month[month] = 0
        self.sightings_per_month[month] += 1
        pass
