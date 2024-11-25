def process_tournament(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    threshold = int(lines[0].strip())
    players = []
    for line in lines[1:]:
        surname, name, score = line.split()
        score = int(score)
        if score > threshold:
            players.append((score, surname, name))
    
    players.sort(reverse=True, key=lambda x: x[0])
    with open(output_file, 'w') as file:
        file.write(f"{len(players)}\n")
        for idx, (score, surname, name) in enumerate(players, 1):
            file.write(f"{idx}) {name[0]}. {surname} {score}\n")

process_tournament('first_tour.txt', 'second_tour.txt')
