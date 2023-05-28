from tools import execute, store, retrieve
from agent import generate

def main():
    task = "generate a random array with 20 digits and sort using quicksort. print the sorted array"
    # TODO check vectordb for code
    # generate code
    code = generate(task)
    # execute code
    execution = execute(code)
    # TODO store code in vectordb
    code = {
        "task": task,
        "generation": code
    }
    return

if __name__ == "__main__":
    main()

