from flask import Flask, render_template, jsonify, request
import os
import requests
from math import radians, sin, cos, sqrt, atan2

app = Flask(__name__)

DEFAULT_CONFIG = {
    'vehicles': ['MH14HQ2061', 'MH12KQ4018', 'MH12HB2065', 'MH12HB2064'],
    'home_lat': 18.4556175,
    'home_lon': 73.9174223,
    'school_lat': 18.473634,
    'school_lon': 73.923871,
    'alert_distance': 0.8,
    'very_near_distance': 400,
    'check_interval': 30,
    'map_zoom': 13
}

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return round(R * c, 2)

def fetch_vehicle_location(vehicle_no):
    try:
        url = f"https://tbtrack.in/gps/public/v1/vehicle/location/data?vehicleNo={vehicle_no}&timeRanges="
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'OK' and data.get('code') == 200:
                location_data = data.get('data', {})
                location = location_data.get('location', [])
                
                if len(location) >= 2:
                    return {
                        'vehicle_no': vehicle_no,
                        'lon': location[0],
                        'lat': location[1],
                        'speed': location_data.get('speed', 0),
                        'added': location_data.get('added', ''),
                        'address': location_data.get('address', ''),
                        'status': location_data.get('status', ''),
                        'success': True
                    }
    except Exception as e:
        print(f"Error fetching {vehicle_no}: {str(e)}")
    
    return {'vehicle_no': vehicle_no, 'success': False, 'error': 'Unable to fetch'}

@app.route('/')
def index():
    return render_template('index.html', config=DEFAULT_CONFIG)

@app.route('/api/vehicles', methods=['POST'])
def get_vehicles():
    data = request.get_json()
    vehicle_list = data.get('vehicles', DEFAULT_CONFIG['vehicles'])
    home_lat = float(data.get('home_lat', DEFAULT_CONFIG['home_lat']))
    home_lon = float(data.get('home_lon', DEFAULT_CONFIG['home_lon']))
    
    results = []
    for vehicle_no in vehicle_list:
        vehicle_data = fetch_vehicle_location(vehicle_no)
        if vehicle_data['success']:
            distance = calculate_distance(home_lat, home_lon, vehicle_data['lat'], vehicle_data['lon'])
            vehicle_data['distance_from_home'] = distance
        results.append(vehicle_data)
    
    return jsonify({'success': True, 'vehicles': results, 'home': {'lat': home_lat, 'lon': home_lon}})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
