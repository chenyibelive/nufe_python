import turtle as t
t.setup(650,350,200,200)    #窗口大小及左上角位置
t.seth(30)                  #画笔起始方向
for i in range(6):
    t.fd(30)                #六角形边长30
    t.left(120)
    t.fd(30)
    t.left(120)
    t.fd(30)
    t.left(120)             #画完一个三角形
    
    t.fd(30)
    t.right(60)             #转换方向，开始准备新的三角形


