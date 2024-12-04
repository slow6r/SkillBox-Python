import random

class KarmaError(Exception):
    pass

class KillError(KarmaError):
    pass

class DrunkError(KarmaError):
    pass

class CarCrashError(KarmaError):
    pass

class GluttonyError(KarmaError):
    pass

class DepressionError(KarmaError):
    pass


def one_day():
    karma = random.randint(1, 7)
    if random.randint(1, 10) == 1:
        error = random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
        raise error("Произошло несчастье!")
    return karma


def main():
    total_karma = 0
    karma_goal = 500
    with open("karma.log", "w") as log_file:
        while total_karma < karma_goal:
            try:
                total_karma += one_day()
            except KarmaError as e:
                log_file.write(f"Ошибка: {e}\n")
            print(f"Текущая карма: {total_karma}")

if __name__ == "__main__":
    main()
