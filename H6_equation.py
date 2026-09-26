import numpy as np
import matplotlib.pyplot as plt


POWERS: dict[str, int] = {"linear": 1, "quadratic": 2, "cubic": 3}


def get_type() -> str:
  exponent: str = input("Type of equation: ").lower()
  if exponent in POWERS: return exponent
  else:
    print("Not a valid equation type." \
    "Try 'linear', 'quadratic', 'cubic', or check your spelling.")
    get_type()

def get_variable(var: str) -> float:
  try:
    coefficient: float = float(input(f"{var}: "))
    return coefficient
  except ValueError:
    print("Not a valid number.")
    get_variable(var)

def get_coefficients(n: int) -> list[int]:
  coefficients: list[float] = []

  for var in ["a", "b", "c", "d"][:n+1]: coefficients.append(get_variable(var))

  return coefficients

exponent: str = get_type()
power: int = POWERS[exponent]
coefficients: list[float] = get_coefficients(power)


x: float = np.arange(0, 50, 1)

match power:
  case 1:
    print(f"Your equation will look like this: y = {coefficients[0]}x + {coefficients[1]}")
    y: float = coefficients[0] * x + coefficients[1]
  case 2:
    print(f"Your equation will look like this: y = {coefficients[0]}x^2 + {coefficients[1]}x + {coefficients[2]}")
    y: float = coefficients[0] * x ** 2 + coefficients[1] * x + coefficients[2]
  case 3:
    print(f"Your equation will look like this: y = {coefficients[0]}x^3 + {coefficients[1]}x^2 + {coefficients[2]}x + {coefficients[3]}")
    y: float = coefficients[0] * x ** 3 + coefficients[1] * x ** 2 + coefficients[2] * x + coefficients[3]


plt.plot(x, y)
plt.show()