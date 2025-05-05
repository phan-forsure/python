def httpReq(status):
  match status:
    case 200:
      return "You're good man!"
    case 400:
      return "Bad request"
    case 404:
      return "Not found"
    case 403:
      return "Forbidden"
    case _:
      return "Who knows man..."
    

x, y = (0, 4)

match x, y:
  case (0, 0):
    print("0, 0")
  case (x, 0):
    print(f"{x} 0")
  case (0, y):
    print(f"0 {y}")
  case (x, y):
    print(f"{x} {y}")
  case _:
    print(f"Not a point")