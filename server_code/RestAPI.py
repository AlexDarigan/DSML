import anvil.server


@anvil.server.http_endpoint("/stats")
def statistics():
  return "API endpoint is not implemented yet"

@anvil.server.http_endpoint("trends")
def trends():
  return "API endpoint is not implemented yet"

@anvil.server.http_endpoint("predict")
def predictions():
  return "API endpoint is not implemented yet"


