from vehicle import Vehicle
from time import sleep as s
def pp(foo):
    print("*"*40)
    print(foo)
    print("*" * 40)
class Plane(Vehicle):
    def __init__(self,fc,ms,tc):
        super().__init__(fc,ms,tc)
        self._turbine_is_started=False
    def start_turbine(self):
        if self._turbine_is_started:
            pp("Turbine started already!")
            s(3)
        else:
            self._turbine_is_started=True
            pp("Turbine started.")
            s(3)
    def stop_turbine(self):
        if self._turbine_is_started:
            self._turbine_is_started=False
            pp("Turbine stoped")
            s(3)
        else:
            pp("Turbine is stoped already!")
            s(3)
    def fly(self,dist):
        if self._turbine_is_started:
            super().move(dist)
            s(3)
        else:
            pp("Can not move.Start turbine first")
            s(3)
    def print_info(self):
        super().print_info()
        print('Turbine started?:', self._turbine_is_started)
        s(3)