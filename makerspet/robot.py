import rclpy
from rclpy.node import Node
from rcl_interfaces.srv import GetParameters, SetParameters
from rcl_interfaces.msg import Parameter, ParameterType

# https://www.theconstruct.ai/how-to-set-get-parameters-from-another-node-ros2-humble-python-tutorial/

class ParamClient(Node):

  def __init__(self, param_server_name):
    super().__init__('parameter_client_' + param_server_name)

    self.setter = self.create_client(SetParameters, '/' + param_server_name + '/set_parameters')
    self.getter = self.create_client(GetParameters, '/' + param_server_name + '/get_parameters')

    while not self.setter.wait_for_service(timeout_sec=1.0):
      self.get_logger().info('Waiting ' + param_server_name + ' set_parameters service ...')

    while not self.getter.wait_for_service(timeout_sec=1.0):
      self.get_logger().info('Waiting ' + param_server_name + ' get_parameters service ...')

    self.set_req = SetParameters.Request()
    self.get_req = GetParameters.Request()


  def get(self, param_name_list):
    if not isinstance(param_name_list, list):
      param_name_list = [param_name_list]

    self.get_req.names = param_name_list

    self.future_get = self.getter.call_async(self.get_req)
    rclpy.spin_until_future_complete(self, self.future_get)

    return self.future_get.result()


  def set(self, param_tuple_list, param_value=None):
    if param_value is not None:
      param_tuple_list = [(param_tuple_list, param_value)]

    if not isinstance(param_tuple_list, tuple):
      param_tuple_list = [param_tuple_list]

    for param_tuple in param_tuple_list:
      param_name = param_tuple[0]
      param_value = param_tuple[1]

      if isinstance(param_value, float):
        val = ParameterValue(double_value=param_value, type=ParameterType.PARAMETER_DOUBLE)
      elif isinstance(param_value, int):
        val = ParameterValue(integer_value=param_value, type=ParameterType.PARAMETER_INTEGER)
      elif isinstance(param_value, str):
        val = ParameterValue(string_value=param_value, type=ParameterType.PARAMETER_STRING)
      elif isinstance(param_value, bool):
        val = ParameterValue(bool_value=param_value, type=ParameterType.PARAMETER_BOOL)

      self.req.parameters.append(Parameter(name=param_name, value=val))

    self.future_set = self.setter.call_async(self.set_req)
    rclpy.spin_until_future_complete(self, self.future_set)

#    response = self.future.result()
#    if response[0].successful:
#      return True
    return self.future_set.result()
