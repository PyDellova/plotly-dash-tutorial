# Interactive Sine with Dash & Render

This tutorial shows how to transform a sine curve into an **interactive web app** with [Dash](https://dash.plotly.com/) and deploy it easily on [Render](https://render.com).

---

## Local Setup

1. Clone the repo:

```
git clone n https://github.com/PyDellova/plotly-dash-tutorial.git
cd plotly-dash-tutorial
```

2. Create a virtual environment and install dependencies:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Tutorial

3. **Intro**
Run 01_matplotlib.py

```
python 01_matplotlib.py
```

4. **Plotly**
Write a script that mirrors the features of 01_matplotlib.py, but only using Plotly. You will need :
- [numpy.linspace](https://numpy.org/devdocs//reference/generated/numpy.linspace.html)
- [numpy.sin](https://numpy.org/devdocs//reference/generated/numpy.sin.html)
- [plotly.express.line](https://plotly.com/python-api-reference/generated/plotly.express.line)

5. **Dash**
Write a script to produce an interactive graph, where both the frequency and phase of the sine can be controlled by two separate sliders. In addition to the previous functions, you will need :
- [Dash](https://dash.plotly.com/) to create the web app and layout.
- `dcc.Slider` to allow interactive control of frequency and phase.
- `dcc.Graph` to display the sine curve dynamically.
- A callback function (`@app.callback`) to update the graph whenever slider values change.

6. **Render**
Deploy your interactive Dash app online using Render:

Make sure your repo contains:
   - `app.py` (your Dash script)
   - `requirements.txt` (list of dependencies: numpy, plotly, etc)
   - `Procfile` (contains: `web: gunicorn app:server`)

Push your repo to GitHub.

Go to [Render](https://render.com) → **New → Web Service** → connect your repo.

Configure the service:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:server`

Click **Deploy**. Once the build completes, Render provides a **public URL** to access your interactive sine app from anywhere.
