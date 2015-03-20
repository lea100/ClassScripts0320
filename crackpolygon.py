import Rhino
import rhinoscriptsyntax as rs

#recursive
#put point in center, build new polygons

def crackpolygon(polylines, count):
    #count = # of times to crack, # generations
    #pls = polylines
    newPolylines = []
    if count > maxGen:
        return
    for polyline in polylines:
        if rs.CloseCurve(polyline) == False:
            print "not a closed curve"
        else:
            centroid = rs.CurveAreaCentroid(polyline)
            centpt = rs.AddPoint(centroid[0])
            curves = rs.ExplodeCurves(polyline)
            for crv in curves:
                pt1 = rs.CurveStartPoint(crv)
                pt2 = rs.CurveEndPoint(crv)
                pts = []
                pts.append(pt1)
                pts.append(pt2)
                pts.append(centpt)
                pts.append(pt1)
                newpl = rs.AddPolyline(pts)
                newPolylines.append(newpl)
                rs.DeleteObject(crv)
            rs.DeleteObjects(centpt)
    return crackpolygon(newPolylines, count+1)
    
    
def main():
    maxGen = rs.GetInteger("How many iterations would you like to do?", 3)
    polyline = rs.GetCurveObject("Pick a closed curve to crack")
    polylineGuid = polyline[0]
    polygons = []
    polygons.append(polylineGuid)
    crackpolygon(polygons, 0)
