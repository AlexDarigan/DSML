import anvil.server


@anvil.server.http_endpoint("/greet")
def greeting():
  return "Hello World"
