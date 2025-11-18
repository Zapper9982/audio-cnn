import sys 
import modal 

app = modal.App("audio-cnn")


@app.function()
def f(i):
    if i % 2 == 0:
        print("hello", i)
    else:
        print("world", i, file=sys.stderr)

    return i * i


@app.local_entrypoint()
def main():
    print(f.local(10))
    print(f.remote(10))


