import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)