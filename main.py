from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    colors = []
    if request.method == 'POST':
        hue_start = int(request.form['hueStart'])
        steps = int(request.form['steps'])
        colors = intervalPicker(hue_start, steps)
    return render_template('index.html', colors=colors)

def intervalPicker(hueStart, steps):
  color = hueStart
  interval = (255 / steps)
  colors = []

  for num in range(steps):
    color = color % 256
    colors.append(f"hsl({int(color)},100%,50%)")
    color = color + interval

  return colors

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
