from flask import Flask
import ghhops_server as hs

# register hops as middleware
pointatServer = Flask(__name__)
hops = hs.Hops(pointatServer)
