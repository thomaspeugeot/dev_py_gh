import rhino3dm
from flask import Flask
import ghhops_server as hs

# register hops as middleware
app = Flask(__name__)
hops = hs.Hops(app)


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
    return curve.PointAt(t)


if __name__ == "__main__":
    app.run()
