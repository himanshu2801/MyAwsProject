import os
from flask import Flask, render_template, request, redirect, send_file
from boto3_file import *

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(app.instance_path, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
BUCKET = "flaskdisk"
@app.route('/')
def entry_point():
    return render_template('navigation.html')

@app.route('/createec2instance')
def getDetail():
    return render_template('createEc2.html')


@app.route('/create',methods=['POST'])
def create():
    data = {}
    data["imageId"] = request.form['imageId']
    data["minCount"] = request.form['minCount']
    data["maxCount"] = request.form['maxCount']
    data["instanceType"] = request.form["instanceType"]
    data["keyName"] = request.form["keyName"]
    print(data)
    create_instance(data)
    return 'Successfully created'

@app.route("/ec2Setting")
def publicIp():
    return render_template("choose.html")
    
@app.route("/getinstance",methods=['POST'])
def renderEc2PublicIp():
    if request.method=='POST':
        instance_id = request.form['instanceidip']
        result = get_public_ip(instance_id)
        return "Public Ip Address: " + result

@app.route("/terminateinstance",methods=['POST'])
def terminateEc2():
    if request.method=='POST':
        instance_id = request.form['instanceidterminate']
        terminate_instance(instance_id)
        return "Terminated Successfully"

@app.route("/stopinstance",methods=['POST'])
def stopEc2():
    if request.method=='POST':
        instance_id = request.form['instanceidstop']
        stop_instance(instance_id)
        return "Stopped Successfully"
    

@app.route("/storage")
def storage():
    contents = list_files("flaskdisk")
    #return render_template('s3Page.html')
    return render_template('s3Page.html', contents=contents)

@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER,f.filename))
        upload_file(UPLOAD_FOLDER + "/" + f.filename, BUCKET)
        return redirect("/storage")

@app.route("/download/<filename>", methods=['GET'])
def download(filename):
    print(filename)
    if request.method == 'GET':
        output = download_file(filename, BUCKET)

        return send_file(output, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)