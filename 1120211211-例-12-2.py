class PERSON:
    
    def eat(self, name,place):
    	print("{}在{}吃饭".format(name, place))
    def sleep(self,name, place):
    	print("{}在{}睡觉".format(name, place))
    
    def dosport(self,name, place, sport_name):
    	print("{}在{}{}".format(name, place, sport_name))
    
    def makeup(self,name, place):
    	print("{}在{}化妆".format(name, place))
    def playgame(self,name, place, game_name):
    	print("{}在{}玩{}".format(name, place, game_name))
    def watchvideo(self,name, video):
    	print("{}在看{}".format(name, video))

class STUDENT(PERSON):
    def gotoclass(self, name,place, class_name):
        print("{}在{}上课".format(name, place, class_name))
    def study(self,name, place):
        print("{}在{}自习".format(name, place))

class WORKER(PERSON):
    def gotowork(self, name,place):
        print("{}在{}上班".format(name, place))
    def gotoconference(self,name, place):
        print("{}在{}开会".format(name, place))
if __name__=="__main__":
    worker_name1 = "小明"
    worker_class1=WORKER()
    print("======{}的一天======".format(worker_name1))
    worker_class1.gotowork(worker_name1,"华为")
    worker_class1.gotoconference(worker_name1,"华为B区201")