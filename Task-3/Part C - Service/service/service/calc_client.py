import rclpy
from rclpy.node import Node
from service_interface.srv import Calc

class CalcClient(Node):
    def __init__(self):
        super().__init__('Calc_client')

        self.client = self.create_client(Calc, 'calc_service')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for calculator service...")
        self.req = Calc.Request()

    def send_request(self, a, b, op):
        self.req.a = a
        self.req.b = b
        self.req.op = op
        self.get_logger().info(f"Sending request: {a} {op} {b}")
        future = self.client.call_async(self.req)
        rclpy.spin_until_future_complete(self,future)
        return future.result()
    
def main(args=None):
    rclpy.init(args=args)
    client = CalcClient()
    response = client.send_request(10, 5, '+')
    client.get_logger().info(f"Result: {response.result}")
    rclpy.shutdown()

if __name__ == "__main__":
    main()        
