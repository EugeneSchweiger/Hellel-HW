import Human
class Godzilla:
    NUMBER_OF_TASKS=37
    NUMBER_OF_TESTS = 12
    TEST_WEIGHTS=[1, 1, 1, 2, 2, 2, 4, 4, 4, 8, 8, 15]
    def __init__(self,stomach_valume):
        self.stomach_volume=stomach_valume
        self.is_hungry=True
        self.feed_level=self.stomach_volume*0.1
    def eat(self,*human):
        print("_"*60)
        for person in human:
            if self.is_hungry:
                if self.stomach_volume>self.feed_level+person.weight:
                    self.stomach_volume-=person.weight
                    print("Godzilla eating.Corrent stomach volume is:%s"
                          %self.stomach_volume)
                elif self.stomach_volume==self.feed_level+person.weight:
                    self.stomach_volume -= person.weight
                    self.is_hungry=False
                    print("Godzilla eating.Corrent stomach volume is:%s"
                    % self.stomach_volume,"This is the last meal")
                else:
                    print("Can't eat this")
            else:
                print("Can't eat this")
        print("_"*60)

    def print_god_stats(self):
        print("*"*60)
        print("stomach_volume:",self.stomach_volume)
        print("is hungry?:",self.is_hungry)
        print("*"*60)

