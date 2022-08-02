import ghhops_server as hs
import rhino3dm

from . import hops


@hops.component(
    "/pointat",
    name="PointAt",
    description="Get Point Along the Curve",
    icon="hello_app/pointat.png",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on curve", default=2.0),
    ],
    outputs=[hs.HopsPoint("P", "P", "Point on curve at t")],
)
def pointat(curve: rhino3dm.Curve, t):
    print("pointat")
    return curve.PointAt(t)
