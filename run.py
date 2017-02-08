import gpxpy
import gpxpy.gpx
import pandas as pd
import json


def main():
    # loop through all the files here once
    gpx_file = open('morning_run.gpx', 'r')

    gpx = gpxpy.parse(gpx_file)

    json_point = []
    points = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                latt = point.latitude
                lngg = point.longitude
                # t  = {'lat': latt, 'lng': lngg}
                t = (latt, lngg)
                points.append(t)

    activity_data = pd.DataFrame(points, columns=['lat', 'lng'])

    # activity_coordinates = ",\n".join(
            # ["{{lat: {lat}, lng: {lon}}}".format(lat=x[0], lon=x[1]) for x in points])
    
    print(activity_data)
    
    activity_data.to_json('point_data.json')

if __name__ == '__main__':
    main()
