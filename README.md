# Vehicle Tracker Web App

Real-time GPS vehicle tracking with distance monitoring and alerts.

## Features
- Real-time GPS tracking via API
- Interactive map with Leaflet.js
- Distance calculation from home location
- Desktop notifications + sound alerts
- Multiple vehicle support with color coding
- Customizable settings (alert distance, check interval, zoom)

## Configuration
Edit settings in the web interface:
- **Home Location**: Your reference coordinates
- **Vehicles**: Vehicle registration numbers (one per line)
- **Alert Distance**: Notification trigger distance (km)
- **Check Interval**: Update frequency (seconds)
- **Map Zoom**: Initial zoom level

## Local Testing
```bash
pip install -r requirements.txt
python app.py
```
Visit http://localhost:8080

## Deploy to Back4App
1. Push code to GitHub
2. Create Container as a Service app on Back4App
3. Connect GitHub repository
4. Deploy (Dockerfile detected automatically)

## API
Vehicle data from: https://tbtrack.in/gps/public/v1/vehicle/location/data
