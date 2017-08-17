from vehicle import Vehicle
from time import sleep as s
def pp(foo):
    print("*"*40)
    print(foo)
    print("*" * 40)
class Train(Vehicle):
    def __init__(self,fc,ms,tc):
        super().__init__(fc,ms,tc)
        self._engine_is_started=False
    def start_engine(self):
        if self._engine_is_started:
            pp("Engine started already!")
            s(3)
        else:
            self._engine_is_started=True
            pp("Engine started.")
            s(3)
    def stop_engine(self):
        if self._engine_is_started:
            self._engine_is_started = False
            pp("Engine stoped")
            s(3)
        else:
            pp("Engine is stoped already!")
            s(3)
    def drive(self,dist):
        if self._engine_is_started:
            super().move(dist)
            s(3)
        else: pp("Can not move.Start engine first")
        s(3)
    def print_info(self):
        super().print_info()
        print('Engine started?:', self._engine_is_started)
        s(3)