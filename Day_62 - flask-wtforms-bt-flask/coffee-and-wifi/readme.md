## problem statement:

Create a multi-page website to manage cafes
* show all cafes with their meta-data
* /add new cafe with persistent storage

Todo:

1. Create home page (as per lecture)

## new_learnen 
### use novalidate in bootstrap-flask_5
{{ render_form(form, novalidate=True) }}

### validation works best after including request.method == post condition:

```python
@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if request.method == 'POST':
        # Exercise:
            # Make the form write a new row into cafe-data.csv
            # with   if form.validate_on_submit()
        if form.validate_on_submit():
            print("True")
            print(form.data.items())
            with open(filename, mode='a', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator = "\n")
                csv_writer.writerow([form.cafe.data, form.location.data, form.open.data, form.close.data, form.coffee.data,
                                    form.wifi.data, form.power.data])
                return redirect(url_for('cafes'))
    
    return render_template('add.html', form=form)

```
