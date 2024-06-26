default_initial_settings = {
    "name": "Cremaker M V2",
    "manufacturer": "JOYPLACE CO., LTD.",
    "start_gcode": "G28\nG29\nG1 Z5.0 F6000\nG1 X2 Y5 Z0.3 F3000\nG92 E0\nG1 Y100 E10 F1500\nG0 X2.3 F3000\nG1 Y20 E8.5 F1500\nG92 E0\nG1 F2400 E-2",
    "end_gcode": "M104 S0\nM140 S0\nG92 E1\nG1 E-1 F300\nG28 X0 Y200\nM84",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 100,
    "dia_feed": 1.75,
    "build_volume_x": 220,
    "build_volume_y": 220,
    "build_volume_z": 260,
}
