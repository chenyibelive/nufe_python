class CAT():
    zhonglei = '猫'
    name = 'Mimi'
    def miaomiaobark(self):
        print(self.name,'喵喵叫')
    def eat(self):
        print(self.name,'吃')
    def jump(self):
        print(self.name+'跳')

cat = CAT()
cat.name = 'ttt'
cat.jump()