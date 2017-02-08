import gpxpy
import gpxpy.gpx
import pandas as pd
import json
import os

def main():
    points = [] 

    for filename in os.listdir('./activities/'):
        if filename[-7:-4] == 'Run':

            gpx_file = open('./activities/' + filename, 'r')
            gpx = gpxpy.parse(gpx_file)

            current_route = []
           
            for track in gpx.tracks:
                for segment in track.segments:
                    for point in segment.points:
                        latt = point.latitude
                        lngg = point.longitude
                        t  = {'lat': latt, 'lng': lngg}
                        current_route.append(t)

            points.append(current_route)


    with open('data_new.txt', 'w') as outfile:
        json.dump(points, outfile)

if __name__ == '__main__':
    main()
