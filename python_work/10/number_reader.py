from pathlib import Path
import json

path = Path('numbers.json')
content = path.read_text()
numbers = json.loads(content)

print(numbers)
