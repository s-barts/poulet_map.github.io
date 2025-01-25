import scipy.spatial
import numpy as np
from scipy.spatial import ConvexHull
import folium
from folium.plugins import MeasureControl
from geopy.distance import great_circle
import webbrowser
from branca.element import Element  # Correct import for Element

# Add game rules HTML template
game_rules = """
<div style="position: fixed; 
            top: 10px; 
            left: 10px; 
            width: 250px; 
            height: 95%; 
            background: white;
            padding: 20px;
            z-index: 999;
            box-shadow: 0 0 5px rgba(0,0,0,0.2);
            overflow-y: auto;">
    <h3>Où est le Poulet Rules</h3>
    <ol>
        <li>Start at The Crosse Keys (red flag)</li>
        <li>Visit pubs within the red boundary</li>
        <li>Use measurement tool to check distances</li>
        <li>First team to find all chickens wins!</li>
        <li>Max 45 mins per round</li>
    </ol>
</div>
"""

# POSTCODE DATA FOR ALL PUBS
postcodes = {
    "The Lamb Tavern": "EC3V 1LR",
    "The Grapes (Leadenhall)": "EC3M 7AN",
    "Red Lion (Eldon Street)": "EC2M 7QF",
    "The Globe": "EC2M 6SA",
    "The Magpie": "EC4M 7EP",
    "Old Doctor Butler's Head": "EC2V 5BT",
    "The Trading House": "EC2V 7NQ",
    "The Golden Fleece": "EC3A 5BU",
    "The Pavilion End": "EC4M 9BR",
    "The Cock and Woolpack": "EC1A 9ER",
    "The Sugar Loaf": "EC2V 7NQ",
    "The Monument": "EC3R 6AJ",
    "The Hung, Drawn and Quartered": "EC3R 5AQ",
    "The Liberty Bounds": "EC3N 4AA",
    "The Wren Tavern": "EC4V 4BJ",
    # New additions
    "The Crosse Keys": "EC3V 0DR",         # Starting Point
    "Simmons Bank": "EC4N 8AR",
    "The Hydrant": "EC3R 6LJ",
    "The Banker": "EC4R 3TE",
    "Hamilton Hall": "EC2M 7PY"
}

# MANUALLY VERIFIED COORDINATES
pubs = {
    "The Lamb Tavern": (51.5129, -0.0832),
    "The Grapes (Leadenhall)": (51.5130, -0.0830),
    "Red Lion (Eldon Street)": (51.5173, -0.0851),
    "The Globe": (51.5186, -0.0886),
    "The Magpie": (51.5160, -0.1013),
    "Old Doctor Butler's Head": (51.5152, -0.0924),
    "The Trading House": (51.5167, -0.0939),
    "The Golden Fleece": (51.5126, -0.0802),
    "The Pavilion End": (51.5153, -0.0970),
    "The Cock and Woolpack": (51.5163, -0.0984),
    "The Sugar Loaf": (51.5161, -0.0931),
    "The Monument": (51.5101, -0.0857),
    "The Hung, Drawn and Quartered": (51.5095, -0.0801),
    "The Liberty Bounds": (51.5088, -0.0774),
    "The Wren Tavern": (51.5124, -0.0969),
    # New additions with verified coordinates
    "The Crosse Keys": (51.5132, -0.0837),     # Starting Point (9 Gracechurch St)
    "Simmons Bank": (51.5130, -0.0901),        # 20 Cornhill
    "The Hydrant": (51.5102, -0.0853),         # 27 Monument Street
    "The Banker": (51.5093, -0.0824),          # EC4R 3TE
    "Hamilton Hall": (51.5181, -0.0813)        # Liverpool Street Station
}

# CALCULATE CONVEX HULL BOUNDARY
coordinates = np.array(list(pubs.values()))
hull = ConvexHull(coordinates)
hull_points = coordinates[hull.vertices]

# CREATE MAP CENTERED ON STARTING POINT
m = folium.Map(location=pubs["The Crosse Keys"], zoom_start=16, tiles="OpenStreetMap")

# ADD MARKERS (same as before)
for pub, (lat, lon) in pubs.items():
    icon_color = "red" if pub == "The Crosse Keys" else "blue"
    icon_type = "flag" if pub == "The Crosse Keys" else "beer"
    
    folium.Marker(
        [lat, lon],
        tooltip=pub,
        popup=f"<b>{pub}</b><br>Postcode: {postcodes[pub]}",
        icon=folium.Icon(color=icon_color, icon=icon_type, prefix="fa")
    ).add_to(m)

# ADD TIGHT POLYGON BOUNDARY
folium.PolyLine(
    locations=np.append(hull_points, [hull_points[0]], axis=0),  # Close the polygon
    color="red",
    weight=2,
    fill=True,
    fill_color="red",
    fill_opacity=0.1
).add_to(m)

# ADD MEASUREMENT TOOL
m.add_child(MeasureControl(position="bottomleft"))

# SAVE AND OPEN
m.save("tight_boundary_map.html")
webbrowser.open("tight_boundary_map.html")
import scipy.spatial
import numpy as np
from scipy.spatial import ConvexHull
import folium
from folium.plugins import MeasureControl
from geopy.distance import great_circle
import webbrowser

# POSTCODE DATA FOR ALL PUBS
postcodes = {
    "The Lamb Tavern": "EC3V 1LR",
    "The Grapes (Leadenhall)": "EC3M 7AN",
    "Red Lion (Eldon Street)": "EC2M 7QF",
    "The Globe": "EC2M 6SA",
    "The Magpie": "EC4M 7EP",
    "Old Doctor Butler's Head": "EC2V 5BT",
    "The Trading House": "EC2V 7NQ",
    "The Golden Fleece": "EC3A 5BU",
    "The Pavilion End": "EC4M 9BR",
    "The Cock and Woolpack": "EC1A 9ER",
    "The Sugar Loaf": "EC2V 7NQ",
    "The Monument": "EC3R 6AJ",
    "The Hung, Drawn and Quartered": "EC3R 5AQ",
    "The Liberty Bounds": "EC3N 4AA",
    "The Wren Tavern": "EC4V 4BJ",
    # New additions
    "The Crosse Keys": "EC3V 0DR",         # Starting Point
    "Simmons Bank": "EC4N 8AR",
    "The Hydrant": "EC3R 6LJ",
    "The Banker": "EC4R 3TE",
    "Hamilton Hall": "EC2M 7PY"
}

# MANUALLY VERIFIED COORDINATES
pubs = {
    "The Lamb Tavern": (51.5129, -0.0832),
    "The Grapes (Leadenhall)": (51.5130, -0.0830),
    "Red Lion (Eldon Street)": (51.5173, -0.0851),
    "The Globe": (51.5186, -0.0886),
    "The Magpie": (51.5160, -0.1013),
    "Old Doctor Butler's Head": (51.5152, -0.0924),
    "The Trading House": (51.5167, -0.0939),
    "The Golden Fleece": (51.5126, -0.0802),
    "The Pavilion End": (51.5153, -0.0970),
    "The Cock and Woolpack": (51.5163, -0.0984),
    "The Sugar Loaf": (51.5161, -0.0931),
    "The Monument": (51.5101, -0.0857),
    "The Hung, Drawn and Quartered": (51.5095, -0.0801),
    "The Liberty Bounds": (51.5088, -0.0774),
    "The Wren Tavern": (51.5124, -0.0969),
    # New additions with verified coordinates
    "The Crosse Keys": (51.5132, -0.0837),     # Starting Point (9 Gracechurch St)
    "Simmons Bank": (51.5130, -0.0901),        # 20 Cornhill
    "The Hydrant": (51.5102, -0.0853),         # 27 Monument Street
    "The Banker": (51.5093, -0.0916),          # EC4R 3TE
    "Hamilton Hall": (51.5181, -0.0813)        # Liverpool Street Station
}

# CALCULATE CONVEX HULL BOUNDARY
coordinates = np.array(list(pubs.values()))
hull = ConvexHull(coordinates)
hull_points = coordinates[hull.vertices]

# CREATE MAP CENTERED ON STARTING POINT
m = folium.Map(location=pubs["The Crosse Keys"], zoom_start=16, tiles="OpenStreetMap")

# ADD MARKERS (same as before)
for pub, (lat, lon) in pubs.items():
    icon_color = "red" if pub == "The Crosse Keys" else "blue"
    icon_type = "flag" if pub == "The Crosse Keys" else "beer"
    
    folium.Marker(
        [lat, lon],
        tooltip=pub,
        popup=f"<b>{pub}</b><br>Postcode: {postcodes[pub]}",
        icon=folium.Icon(color=icon_color, icon=icon_type, prefix="fa")
    ).add_to(m)

# ADD TIGHT POLYGON BOUNDARY
folium.PolyLine(
    locations=np.append(hull_points, [hull_points[0]], axis=0),  # Close the polygon
    color="red",
    weight=2,
    fill=True,
    fill_color="red",
    fill_opacity=0.1
).add_to(m)

# ADD MEASUREMENT TOOL
m.add_child(MeasureControl(position="bottomleft"))

# Add this at the end to ensure mobile compatibility
m.get_root().header.add_child(Element("""
<meta name="viewport" content="width=device-width, initial-scale=1.0">
"""))

# SAVE AND OPEN

m.save("index.html") 