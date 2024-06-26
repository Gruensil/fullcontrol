default_initial_settings = {
    "name": "Atom 2",
    "manufacturer": "Layer One",
    "start_gcode": "G21\nG90 \nM107\nG28\nG1 Y-110 Z15\nG0 Z{0.2}\nG92 E0\nG1 F200 Y-100 E6\nG92 E0",
    "end_gcode": "G28\nG91\nG1 E-6 F300\nM104 S0\nG1 E-1000 F5000\nM84\nG90",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 32,
    "travel_speed": 120,
    "dia_feed": 2.85,
    "build_volume_x": 210,
    "build_volume_y": 210,
    "build_volume_z": 320,
}
