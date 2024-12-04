from heroes import Tank, Healer, Attacker

def main():
    team = [Tank(), Healer(), Attacker()]
    for hero in team:
        print(hero.attack())

if __name__ == "__main__":
    main()
