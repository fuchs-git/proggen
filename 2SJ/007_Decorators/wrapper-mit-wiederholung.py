from functools import wraps


def meine_function(funktion: callable):
    @wraps(funktion)
    def wrapper(*args, **kwargs):
        print('Wrapper Text')
        funktion(*args, **kwargs)
        funktion(*args, **kwargs)
        print('Wrapper Ende')

    return wrapper


@meine_function
def sag(etwas):
    print(etwas)


sag('mal was')


def wiederhole_n_mal(anzahl):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(anzahl):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@wiederhole_n_mal(1)
def sag_hallo():
    print("Hallo")

sag_hallo()




from datetime import datetime

def wiederhole_n_mal(anzahl):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(anzahl):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator



def nachtruhe_einhalten(start, ende):  # das hier ist unser Decorator
    def decorator(func):
        def wrapper():
            if start <= datetime.now().hour < ende:
                func()  # hier wird die Funktion aufgerufen
            else:
                pass # nichts machen, wenn die Uhrzeit nicht passt
        return wrapper
    return decorator

@nachtruhe_einhalten(20,7)
def sag_hallo():        # diese Funktion schreit rum
    print("Hallo!")


sag_hallo()  # ... und aufrufen, sie schreit jetzt nicht immer