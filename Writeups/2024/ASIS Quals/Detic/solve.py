import socket
import math
import re

import numpy as np
from time import sleep
from scipy.optimize import minimize


# Constants
R = 6371  # Earth's radius in km

# Parse the response to extract P1, P2, and P3
def parse_locations(response):
    # Regex to extract the points from the server message
    pattern = re.compile(r"P\d = \('.*?', \(([-\d.]+), ([-\d.]+)\)\)")
    matches = pattern.findall(response)
    
    if len(matches) != 3:
        raise ValueError("Failed to parse the locations from the server response.")
    
    points = [(float(lat), float(lon)) for lat, lon in matches]
    return points

# Connect to the server and send the result
def send_to_server():
    # Server details
    SERVER_IP = '65.109.192.143'
    SERVER_PORT = 13770

    # Create a socket connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, SERVER_PORT))
        
        # Receive the initial message from the server
        response = s.recv(4096).decode()
        print(response)
        
        # Send "Y" to proceed
        s.sendall(b'Y\n')
    
        while True:
            sleep(1)

            # Receive the challenge message with the locations
            response = s.recv(4096).decode()
            print(response)
            
            # Parse the locations (P1, P2, P3) from the server message
            points = parse_locations(response)


            def to_cartesian(lat, lon):
                lat_rad = np.radians(lat)
                lon_rad = np.radians(lon)
                x = R * np.cos(lat_rad) * np.cos(lon_rad)
                y = R * np.cos(lat_rad) * np.sin(lon_rad)
                z = R * np.sin(lat_rad)
                return np.array([x, y, z])

            def distance(p0, p1):
                x0, y0, z0 = to_cartesian(p0[0], p0[1])
                x1, y1, z1 = to_cartesian(p1[0], p1[1])
                dot_product = x0 * x1 + y0 * y1 + z0 * z1
                return R * np.arccos(dot_product / (R**2))

            def objective(p0, p1, p2, p3):
                d1 = distance(p0, p1)
                d2 = distance(p0, p2)
                d3 = distance(p0, p3)
                return abs(d1 - d2) + abs(d1 - d3) + abs(d2 - d3)  # Minimize the sum of absolute differences

            def find_equidistant_point(p1, p2, p3):
                # Starting point: average of the three points
                avg_lat = (p1[0] + p2[0] + p3[0]) / 3
                avg_lon = (p1[1] + p2[1] + p3[1]) / 3
                initial_guess = (avg_lat, avg_lon)

                # Minimize the objective function
                result = minimize(objective, initial_guess, args=(p1, p2, p3), method='L-BFGS-B', bounds=[(-90, 90), (-180, 180)])

                return result.x

            p0 = find_equidistant_point(*points)
            d1 = distance(p0, points[0])
            d2 = distance(p0, points[1])
            d3 = distance(p0, points[2])
            print(f"Equidistant point: Latitude {p0[0]:.6f}, Longitude {p0[1]:.6f}")
            print(f"Distance from P0 to P1: {d1:.6f} km")
            print(f"Distance from P0 to P2: {d2:.6f} km")
            print(f"Distance from P0 to P3: {d3:.6f} km")


            # Round results to 5 decimal places for 1 meter precision
            lat_deg_rounded = round(p0[0], 6)
            lon_deg_rounded = round(p0[1], 6)

            # Prepare the final answer in the required format
            answer = f"{lat_deg_rounded}, {lon_deg_rounded}\n"
            print(f"Sending answer: {answer}")
            
            # Send the answer (longitude, latitude)
            s.sendall(answer.encode())

# Run the function to send the data to the server
if __name__ == "__main__":
    send_to_server()
