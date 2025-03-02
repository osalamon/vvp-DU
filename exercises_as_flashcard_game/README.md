# VVP's exercises flashcard game

## If my tight schedule allows, I might make a sort of flashcard game from (all) exercises in [the forked repository vvp](https://github.com/osalamon/vvp/tree/master)

## TODO (roughly)

* [ ] Improve a script which scrapes exericise's assignments from files in `Week_XY/XY_ukoly.ipynb`. The current implementation in `exercises_as_flashcard_game/scrape_exercises/first_steps.py` is very basic and quick and dirty proof of concept.
* [ ] Tidy scraped data, remove wrong texts and transform data into the proper form.
* [ ] Save data into a CSV file: the first line will consist of `poradi, assignment_text, tag`, where `poradi` is my own counting from 1 to the lastly scraped assignment, `assignment_text` is the text of the assignment, and `tag` is a tag which can be used to filter the assignments (ie. type of exercise like "Lambda funkce", "Generátory", etc).
* [ ] To each item in the CSV file, add a column with starting probability of being drawn in the "flashcard" game. It can by easily computed as `1 / number_of_assignments`.
* [ ] Create a script which will draw for example 10 random assignments from the CSV file and ask me to solve it. After I solve it, I will be asked to evaluate whether my solution was correct or not. 
* [ ] Come up with some profound algoritm which will adjust the probability of being drawn based on the correctness of the answer. The more correct answers, the less probable the assignment will be drawn.
* [ ] Each round of the "game" saves its results into a new CSV file. The file will consist of `poradi, assignment_text, tag, correct, incorrect, probability`. The `correct` and `incorrect` columns will be incremented based on the correctness of the answer. The `probability` column will be updated based on the correctness of the answer.
* [ ] Player can play the game as long as he wants.
* [ ] ??? (sci-fi) Deploy publicly on the web via GitHub Pages etc.