
import ghhops_server as hs
from flask import Flask

from . import point_at_opposite, pointat, pointatServer

if __name__ == "__main__":
    pointatServer.run(debug=True)
