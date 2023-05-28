# EXECUTE CODE BLOCKS

def execute(code):
    try:
        exec(code, globals())
        return
    except Exception as e:
        print(e)
        return
