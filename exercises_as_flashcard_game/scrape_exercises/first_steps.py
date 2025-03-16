import requests
import json
import numpy as np
 
url_with_json_to_parse = "https://raw.githubusercontent.com/osalamon/vvp/refs/heads/master/Week_02/02_ukoly.ipynb"

response = requests.get(url_with_json_to_parse)

jsondata = json.loads(response.text)

exercises_raw = [i["source"] for i in jsondata["cells"] if i["cell_type"] == "markdown"]

with open("exercises_as_flashcard_game/ukoly.csv", "w", newline="\n") as saved_file:
    saved_file.write("poradi, text\n")
    for i in range(1, len(exercises_raw)):
        saved_file.write(f"{i}., {exercises_raw[i]}\n")

# "ukoly.csv" output (getting closer to the desired format...):
# poradi, text
# 1., ['1. Deklarujte proměnnou s názvem ``jmeno`` a přiřaďte jí řetězec s vaším jménem.\n']
# 2., ['\n', '2. Vytiskněte typ proměnné ``jmeno``.\n']
# 3., ['\n', '3. Deklarujte proměnnou ``vek`` a přiřaďte jí vaše číslo věku. Jaký typ bude mít tato proměnná?\n']
# 4., ['\n', '4. Převeďte ``vek`` na typ float a uložte do nové proměnné ``vek_float``.\n']
# 5., ['\n', '5. Vytiskněte hodnoty ``vek`` a ``vek_float``.\n']
# 6., ['\n', '6. Deklarujte proměnnou ``seznam`` a přiřaďte jí list s třemi čísly.\n']
# 7., ['\n', '7. Vytiskněte druhý prvek z listu ``seznam``.\n']
# 8., ['\n', '8. Přidejte na konec listu ``seznam`` další číslo.\n']
# 9., ['\n', '9. Vytiskněte délku listu ``seznam``.\n']
# ...