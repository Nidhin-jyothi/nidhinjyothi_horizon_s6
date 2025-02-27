import rclpy
from rclpy.node import Node
from service_interface.srv import Calc

class CalcServer(Node):
    def __init__(self):
        super().__init__("Calc_server")

        self.srv = self.create_service(Calc, 'calc_service', self.calc_callback)
        self.get_logger().info('Calculator service server is ready.')

    def calc_callback(self, request, response):
        self.get_logger().info(f"Received request: a={request.a}, b={request.b}, op='{request.op}'")    

        if request.op == '+':
            response.result = request.a + request.b
        elif request.op == '-':
            response.result = request.a - request.b
        elif request.op == '*':
            response.result = request.a * request.b
        elif request.op == '/':
            if request.b == 0:
                self.get_logger().error("Division by zero")
            else:
                response.result = request.a // request.b      

        else:
            self.get_logger().error("Unknown operator")
            response.result = 0

        self.get_logger().info(f"Sending response: {response.result}")    
        return response

def main(args=None):
    rclpy.init(args=args)
    server = CalcServer()                  
    rclpy.spin(server)
    rclpy.shutdown()

if __name__ == "__main__":
    main()    