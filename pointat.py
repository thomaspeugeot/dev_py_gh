
import rhino3dm
from flask import Flask
import ghhops_server as hs

# register hops as middleware
pointatServer = Flask(__name__)
hops = hs.Hops(pointatServer)


@hops.component(
    "/pointatopposite",
    name="PointAtOpposite",
    description="Get Opposite Point Along the Curve",
    icon="pointat.png",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on curve", default=2.0),
    ],
    outputs=[hs.HopsPoint("P", "P", "Opposite point on curve at t")],
)
def pointatOpposite(curve: rhino3dm.Curve, t):
    print("pointatOpposite: T0: ", curve.Domain.T0, " T1: ", curve.Domain.T1)
    newT = curve.Domain.T1 - t
    return curve.PointAt(newT)


@hops.component(
    "/pointat",
    name="PointAt",
    description="Get Point Along the Curve",
    icon="pointat.png",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on curve", default=2.0),
    ],
    outputs=[hs.HopsPoint("P", "P", "Point on curve at t")],
)
def pointat(curve: rhino3dm.Curve, t):
    print(curve, t)
    print("toto")
    return curve.PointAt(t)


if __name__ == "__main__":
    pointatServer.run()
