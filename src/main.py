from identifier import Identifier

class Main():
  identifier = Identifier()
  isValid = identifier.validateIdentifier('#')
  print(f'É válido? {isValid}')


if __name__ == "__main__":
  main = Main()