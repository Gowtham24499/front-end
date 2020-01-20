import psutil
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html")

@app.route('/')
def process_index():
    processName_list = []
    processID_list = []
    cpuPercent_list = []
    memoryinfo_list = []
    for proc in psutil.process_iter():
        try:

            processName = proc.name()
            processID = proc.pid
            cpuPercent = proc.cpu_percent()
            memoryinfo = proc.memory_percent()
            processName_list.append(processName)
            processID_list.append(processID)
            cpuPercent_list.append(cpuPercent)
            memoryinfo_list.append(memoryinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

        return render_template("index.html",processName=processName_list,processID=processID_list,cpuPercent=cpuPercent_list,memoryinfo=memoryinfo_list)

if __name__ == '__main__':
   app.run(debug = True)