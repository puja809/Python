import os
import zipfile
from flask import Flask, request, redirect, url_for, flash, render_template,send_file
from werkzeug.utils import secure_filename
#from flask_ngrok import run_with_ngrok
UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__))
ALLOWED_EXTENSIONS = set(['zip'])

app = Flask(__name__)
#run_with_ngrok(app)

filename = ""
filename_model = "model.pkl"

b = "processing"
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/download_files')
def download_all():
    # Zip file Initialization and you can change the compression type
    zipfolder = zipfile.ZipFile('models.zip','w', compression = zipfile.ZIP_STORED)
    # zip all the files which are inside in the folder
    for root,dirs, files in os.walk('models/'):
        for file in files:
            zipfolder.write('models/'+file)
    zipfolder.close()

    return send_file('models.zip',
            mimetype = 'zip',
            attachment_filename= 'models.zip',
            as_attachment = True)

    # Delete the zip file if not needed
    os.remove("models.zip")

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            global filename
            filename = secure_filename(file.filename)
            print(filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            zip_ref = zipfile.ZipFile(os.path.join(UPLOAD_FOLDER, filename), 'r')
            zip_ref.extractall(UPLOAD_FOLDER)
            zip_ref.close()
            return redirect(url_for('index',filename=filename))
    return render_template('upload.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form.getlist('hello'))
        z = request.form.getlist('hello')
        if z[0] == '1':
            return redirect(url_for('svc'))
        if z[0] == '2':
            return redirect(url_for('knn'))
        if z[0] == '3':
            return redirect(url_for('logistic'))
        if z[0] == '4':
            return redirect(url_for('adaboost'))
        if z[0] == '5':
            return redirect(url_for('naive'))
    try:
        #global filename
        import os
        num_classes = len(os.listdir(os.path.splitext(filename)[0]))
        print("Number of classes : ",num_classes)
    except:
        num_classes = "error"
    return render_template('upload1.html',filename=filename,num_class=num_classes)

@app.route('/returnmodel/')
def returnmodel():
	try:
		return send_file("model.pkl")
	except Exception as e:
		return str(e)

@app.route('/svc_classifier', methods=['GET', 'POST'])
def svc():
    global filename
    if request.method == 'POST':
        print(request.form.getlist('kernal')[0])
        kernel = request.form.getlist('kernal')[0]
        print(request.form.getlist('gamma')[0])
        gamma = request.form.getlist('gamma')[0]
        print(request.form.getlist('decision_function_shape')[0])
        decision_function_shape = request.form.getlist('decision_function_shape')[0]
        print(request.form.getlist('max_iter')[0])
        try:
            max_iter = int(request.form.getlist('max_iter')[0])
        except:
            max_iter = -1
        print(request.form.getlist('random_state')[0])
        try:
            random_state = int(request.form.getlist('random_state')[0])
        except:
            random_state = None
        print(request.form.getlist('shape1')[0])
        shape11 = int(request.form.getlist('shape1')[0])
        print(request.form.getlist('shape2')[0])
        shape22 = int(request.form.getlist('shape2')[0])
        import trainer
        a,bz = trainer.svc_model(kernel1=kernel,gamma1=gamma,max_iter1=max_iter, decision_function_shape1=decision_function_shape,random_state1=random_state,shape1 = shape11,shape2=shape22,file=os.path.splitext(filename)[0])
        global filename2
        filename2 = a
        global b
        b = bz
        return redirect(url_for('svc'))
    return render_template('upload_svc.html',something=str(b))

@app.route('/logistic_classifier', methods=['GET', 'POST'])
def logistic():
    if request.method == 'POST':
        print(request.form.getlist('criterion'))
        print(request.form.getlist('splitter'))
        print(request.form.getlist('max_depth'))
        print(request.form.getlist('random_state'))
        print(request.form.getlist('min_samples_split'))
        print(request.form.getlist('max_features'))
        print(request.form.getlist('shape1')[0])
        shape11 = int(request.form.getlist('shape1')[0])
        print(request.form.getlist('shape2')[0])
        shape22 = int(request.form.getlist('shape2')[0])
        try:
            max_depth = int(request.form.getlist('max_depth')[0])
        except:
            max_depth = None
        try:
            min_samples_split = int(request.form.getlist('min_samples_split')[0])
        except:
            min_samples_split = 2
        try:
            min_samples_leaf = int(request.form.getlist('min_samples_leaf')[0])
        except:
            min_samples_leaf = 2
        try:
            random_state = int(request.form.getlist('random_state')[0])
        except:
            random_state = None
        if request.form.getlist('max_features')[0] == "None":
            max_features = None
        else:
            max_features = request.form.getlist('max_features')[0]
        criterion = request.form.getlist('criterion')[0]
        splitter = request.form.getlist('splitter')[0]
        global filename
        import trainer
        a,bz = trainer.logistic(criterion1=criterion, splitter1=splitter, max_depth1=max_depth, min_samples_split1=min_samples_split,min_samples_leaf1 =min_samples_leaf ,max_features1=max_features,random_state1=random_state,shape1 = shape11,shape2= shape22,file=os.path.splitext(filename)[0])
        filename2 = a
        global b
        b = bz
        return redirect(url_for('logistic'))
    return render_template('upload_logistic.html',something=str(b))

@app.route('/adaboost_classifier', methods=['GET', 'POST'])
def adaboost():
    global filename
    if request.method == 'POST':
        print(request.form.getlist('learning_rate'))
        print(request.form.getlist('random_state'))
        print(request.form.getlist('n_estimators'))
        try:
            learning_rate = float(request.form.getlist('learning_rate')[0])
        except:
            learning_rate = 0.1
        try:
            random_state = int(request.form.getlist('random_state')[0])
        except:
            random_state = None
        try:
            n_estimators = int(request.form.getlist('n_estimators')[0])
        except:
            n_estimators = 100
        print(request.form.getlist('shape1')[0])
        shape11 = int(request.form.getlist('shape1')[0])
        print(request.form.getlist('shape2')[0])
        shape22 = int(request.form.getlist('shape2')[0])
        import trainer
        global filename
        a,bz = trainer.adaboost(n_estimators1=n_estimators,random_state1=random_state,learning_rate1=learning_rate,shape1 = shape11,shape2= shape22,file=os.path.splitext(filename)[0])
        global filename2
        filename2 = a
        global b
        b = bz
        return redirect(url_for('adaboost'))
    return render_template('upload_adaboost.html',something=str(b))

@app.route('/knn_classifier', methods=['GET', 'POST'])
def knn():
    global filename
    if request.method == 'POST':
        print(request.form.getlist('weights'))
        print(request.form.getlist('algorithm'))
        print(request.form.getlist('leaf_size'))
        print(request.form.getlist('n_neighbors'))
        weights = request.form.getlist('weights')[0]
        algorithm = request.form.getlist('algorithm')[0]
        try:
            leaf_size = int(request.form.getlist('leaf_size')[0])
        except:
            leaf_size = 30
        try:
            n_neighbors = int(request.form.getlist('n_neighbors')[0])
        except:
            n_neighbors = 5
        print(request.form.getlist('shape1')[0])
        shape11 = int(request.form.getlist('shape1')[0])
        print(request.form.getlist('shape2')[0])
        shape22 = int(request.form.getlist('shape2')[0])
        import trainer
        a,bz = trainer.knn(weights1 =weights,leaf_size1=leaf_size,n_neighbors1 = n_neighbors,algorithm1 = algorithm,shape1 = shape11,shape2= shape22,file=os.path.splitext(filename)[0])
        global filename2
        filename2 = a
        global b
        b = bz
        return redirect(url_for('knn'))
    return render_template('upload_knn.html',something=str(b))

@app.route('/naive_classifier', methods=['GET', 'POST'])
def naive():
    if request.method == 'POST':
        print(request.form.getlist('shape1')[0])
        shape11 = int(request.form.getlist('shape1')[0])
        print(request.form.getlist('shape2')[0])
        shape22 = int(request.form.getlist('shape2')[0])
        import trainer
        a,bz = trainer.naivebayes(shape1 = shape11,shape2= shape22,file=os.path.splitext(filename)[0])
        global filename2
        filename2 = a
        global b
        b = bz
        return redirect(url_for('naive'))
    return render_template('upload_naive.html',something=str(b))

if __name__ == "__main__":
    app.run()
    #app.run(debug=True)