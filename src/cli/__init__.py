import cyclopts

app = cyclopts.App()


@app.default
def main():
    print("Hello World!")
