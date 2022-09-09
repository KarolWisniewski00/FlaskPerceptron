from flask import Flask, render_template, request
from perceptron import Perceptron
from flask_wtf import FlaskForm

#GLOBAL SETTINGS - GLOBALNE USTAWIENIE
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'
perceptron = Perceptron()

#CSRF TOKEN
class FormToken(FlaskForm):
    pass

#INDEX - WIDOK GŁÓWNY
@app.route("/")
def indexController():
    #GO TO VIEW - IDŹ DO WIDOKU
    return render_template('index.html')

#START
@app.route("/start")
def startController():
    #PASS THE TOKEN - PODAJ TOKEN WERYFIKACYJNY
    form = FormToken()

    #GO TO VIEW - IDŹ DO WIDOKU
    return render_template('start.html', form=form)

#TRAINIG
@app.route("/training", methods=["POST","GET"])
def trainingController():
    #PASS THE TOKEN - PODAJ TOKEN WERYFIKACYJNY
    form = FormToken()
    if request.method == "POST":
        #VARIABLES - ZMIENNE
        dataTable=[]
        step=0.2

        #DYNAMIC GET DATA AND CUSTOM VALIDATION - DYNAMICZNE POBRANIE DANYCH I WŁASNA WALIDACJA
        try:
            counter=1
            for row in range(8):
                rows=[]
                for column in range(3):
                    rows.append(int(request.form['input{}'.format(counter)]))
                    counter+=1
                dataTable.append(rows)
        except:         
            #GO TO VIEW - IDŹ DO WIDOKU
            return render_template('start.html', form=form, error='Type in correct INPUTS! Sould be intiger, not string not NULL')

        #VALIDATION STEP - VALIDACJA KROKU
        try:
            step = int(request.form['STEP'])
        except:         
            pass

        #PERCEPTRON
        perceptron.appendVariables(step)
        perceptron.appendDataTable(dataTable)

        #GO TO VIEW - IDŹ DO WIDOKU
        return render_template('use.html', training=perceptron.training(), form=form)
    else:
        #GO TO VIEW - IDŹ DO WIDOKU
        return render_template('start.html', form=form, error='You have to input data first!')

#USE
@app.route("/use", methods=["POST","GET"])
def useController():
    #PASS THE TOKEN - PODAJ TOKEN WERYFIKACYJNY
    form = FormToken()
    if request.method == "POST":
        #VALIDATION
        try:
            int(request.form['input1'])
            int(request.form['input2'])
        except:         
            #GO TO VIEW - IDŹ DO WIDOKU
            return render_template('use.html', training=perceptron.getTrainingCounter(), form=form, error='Type in correct INPUT! Sould be intiger, not string not NULL')

        #GO TO VIEW - IDŹ DO WIDOKU
        return render_template('use.html', training=perceptron.getTrainingCounter(), form=form, result=perceptron.use(int(request.form['input1']),int(request.form['input2'])))
    else:
        #GO TO VIEW - IDŹ DO WIDOKU
        return render_template('start.html', form=form, error='You have to input data first!')


#MAIN APP
if __name__ == "__main__":
    app.run(debug=True)