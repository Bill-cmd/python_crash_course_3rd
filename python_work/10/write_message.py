from pathlib import Path

contents = "I love programming."
contents += "\nI love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('program.txt')
# write a new file
path.write_text(contents)
