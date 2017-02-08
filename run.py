import gpxpy
import gpxpy.gpx
import pandas as pd


def main():
    # loop through all the files here once
    gpx_file = open('morning_run.gpx', 'r')

    gpx = gpxpy.parse(gpx_file)

    json_point = []
    points = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                lat = point.latitude
                lng = point.longitude
                t  = {'lat': lat, 'lng': lng}
                points.append(t)


    # activity_data = pd.DataFrame(points, columns=['latitude', 'longitude'])

    # activity_coordinates = ",\n".join(
            # ["{{lat: {lat}, lng: {lon}}}".format(lat=x[0], lon=x[1]) for x in activity_data.iterrows()])

    print(points)

if __name__ == '__main__':
    main()
