from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/plugin")
def plugin():
    from da_plugin import awesome_module
    return awesome_module.awesome_function()


if __name__ == '__main__':
    app.run()
