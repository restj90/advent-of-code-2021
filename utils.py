import pathlib
from aocd import get_data, submit

ROOT=pathlib.Path(__file__).parent.resolve()
INPUTS_DIR = ROOT/'inputs'
AOC_SESSION=(ROOT/'.token').read_text().strip()

def save_data_file(day, year):
    file = INPUTS_DIR/f"day{str(day).rjust(2, '0')}.txt"
    if not file.exists():
        data = get_data(AOC_SESSION, day, year)
        file.write_text(data.strip())
    return file
        
def read_lines(file):
    with open(file, "r") as f:
        return f.read().strip().splitlines()
        
def read_csv(file):
    with open(file, "r") as f:
        return f.read().strip().split(',')

def read_integers(file):
    input_lines = read_lines(file)
    return [int(i) for i in input_lines]

def submit_answer(answer, part, day, year):
    return submit(answer, part, day, year, AOC_SESSION)