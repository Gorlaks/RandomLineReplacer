from random import randrange

read_file_name = "sortedData.csv"
write_file_name = "data.csv"

def get_random_positions(lines):
  from_position = randrange(1, len(lines))
  to_position = randrange(1, len(lines))
  
  if (from_position == to_position):
    get_random_positions(lines)
  
  return from_position, to_position


with open(read_file_name, "r") as file:
  lines = file.readlines()
  iterations_count = len(lines)

  for n in range(iterations_count):
    from_position, to_position = get_random_positions(lines)
    to_position_text = lines[to_position]
    lines[to_position] = lines[from_position]
    lines[from_position] = to_position_text

  file.close()


with open(write_file_name, "w") as file:
  for line in lines:
    file.write(f"{line}")

  file.close()