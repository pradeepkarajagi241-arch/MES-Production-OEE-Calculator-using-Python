
class Production:
    def __init__(self, machine_id, production_count):
        self.machine_id = machine_id
        self.production_count = production_count

    def total_production(self):
        return self.production_count


class OEE:
    def __init__(self, cycle_time, runtime, total_time, good_count, total_count):
        self.cycle_time = cycle_time
        self.runtime = runtime
        self.total_time = total_time
        self.good_count = good_count
        self.total_count = total_count

    def availability(self):
        return self.runtime / self.total_time

    def performance(self):
        return (self.cycle_time * self.total_count) / self.runtime

    def quality(self):
        return self.good_count / self.total_count

    def oee(self):
        return self.availability() * self.performance() * self.quality()


prod = Production(1, 100)
print("Production:", prod.total_production())

oee = OEE(10, 100, 200, 90, 100)
print("Availability:", oee.availability())
print("Performance:", oee.performance())
print("Quality:", oee.quality())
print("OEE:", oee.oee())