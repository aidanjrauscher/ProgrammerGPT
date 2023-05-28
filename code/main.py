from tools import execute, get_collection, store, retrieve
from agent import generate, describe

def main():
    task = "generate a random array with 20 digits and sort using bubblesort. print the sorted array"
    chroma_collection = get_collection()
    retrieved_code = retrieve(chroma_collection, task)
    if(retrieved_code is not None):
        execute(retrieved_code)
        return

    # generate and describe code
    code = generate(task)
    description = describe(code)

    # execute code
    execute(code)

    #store code in vectordb
    store(chroma_collection, code, description)
    return

if __name__ == "__main__":
    main()

