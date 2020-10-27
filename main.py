from random import randrange

def get_random_positions(lines):
  from_position = randrange(1, len(lines))
  to_position = randrange(1, len(lines))
  
  if (from_position == to_position):
    get_random_positions(lines)
  
  return from_position, to_position


with open("data.csv", "r") as file:
  lines = file.readlines()
  iterations_count = len(lines)

  for n in range(iterations_count):
    from_position, to_position = get_random_positions(lines)
    to_position_text = lines[to_position]
    lines[to_position] = lines[from_position]
    lines[from_position] = to_position_text

  file.close()


with open("data.csv", "w") as file:
  for line in lines:
    file.write(f"{line}")

  file.close()