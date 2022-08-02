
import ghhops_server as hs
import rhino3dm

from . import hops


@hops.component(
    "/pointatopposite",
    name="PointAtOpposite",
    description="Get Opposite Point Along the Curve",
    icon="hello_app/pointat.png",
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
