default_initial_settings = {
    "name": "Winbo Super Helper 105",
    "manufacturer": "Winbo Smart Tech Co., Ltd.",
    "start_gcode": "G21\nG90\nM82\nM107\nG28 X0 Y0\nG28 Z0\nG1 F6000 Z0.3\nG92 E0\nG1 F1000 X30 E8\nG92 E0\nM117 Printing.",
    "end_gcode": "M104 S0\nM140 S0\nG92 E2\nG1 E0 F200\nG28 X0 Y0\nM84 X Y E",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 52,
    "travel_speed": 80,
    "dia_feed": 2.85,
    "build_volume_x": 108,
    "build_volume_y": 108,
    "build_volume_z": 158,
}
