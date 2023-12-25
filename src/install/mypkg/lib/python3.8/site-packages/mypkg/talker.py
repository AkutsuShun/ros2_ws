import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker():
    def __init__(self, node):
         self.pub = node.create_publisher(Int16, "countup", 10)
         self.n = 0
         node.create_timer(0.5, self.cb) #selfをつける。
rclpy.init()
node = Node("talker")
talker = Talker()      #オブジェクトを作成（__init__が実行される。）

def cb(self):      #インデントをあげてselfを引数に
    msg = Int16()
    msg.data = self.n     #talker -> self
    self.pub.publish(msg) #talker -> self
    self.n += 1           #talker -> self

node.create_timer(0.5, cb)
rclpy.spin(node)

def main():
    rclpy.init()
    node = Node("talker")
    talker = Talker(node)
    rclpy.spin(node)

if __name__ == '__main__':
    main()

rclpy.init()
node = Node("talker")
talker = Talker(node) #この一行でパブリッシャが動き出す。
rclpy.spin(node)
