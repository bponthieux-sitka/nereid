from flask import Flask
import json
import socket

def get_Host_name_IP(): 
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 

        return {
            "hostname": host_name,
            "ip_address": host_ip
        }

    except: 
        print("Unable to get Hostname and IP") 

app = Flask(__name__)

@app.route('/')
def hello_world():

    info = {
        "name": 'nereid',
        "version": '0.0.1', 
    }

    info.update(get_Host_name_IP())
    
    _json = json.dumps(
        info,
        sort_keys=True,
        indent=4,
    )

    rsp = "<pre>{}</pre>"
    
    return rsp.format(_json)

if __name__ == '__main__':
    app.run()