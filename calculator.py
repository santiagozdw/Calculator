import logging
logging.basicConfig(level=logging.DEBUG)

def add (a,b):
    return a + b
def sub (a,b):
    return a - b
def multi (a,b):
    return a * b
def div (a,b):
    return a / b

        

if __name__ == "__main__":
	def calculator():
		user_input = int(input("\n\n Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
		operations = ["add","sub","multi","div"]
		operations_name = operations[user_input - 1]
		a = float(input("Podaj składnik 1: "))
		b = float(input("Podaj składnik 2: "))
		

		if operations_name == "add":
			logging.info(f"Dodaję {a} i {b}")
			print(f"Wynik to: {add(a,b)}")
		if operations_name == "sub":
			logging.info(f"Odejmuję {a} i {b}")
			print(f"Wynik to: {sub(a,b)}")
		if operations_name == "multi":
			logging.info(f"Mnożę {a} i {b}")
			print(f"Wynik to: {multi(a,b)}")
		if operations_name == "div":
			logging.info(f"Dzielę {a} i {b}")
			print(f"Wynik to: {div(a,b)}")
	repeat = True

	while repeat:
		try:
			calculator()
			repeat = False
		except ValueError:
			logging.error("Musisz podać liczbę")
		except IndexError:
			logging.error("Musisz podać prawidłową liczbę!")
		except ZeroDivisionError:
			logging.error("Nie dziel nigdy przez zero")
