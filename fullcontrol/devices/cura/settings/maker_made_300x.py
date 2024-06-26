default_initial_settings = {
    "name": "Maker Made 300x",
    "manufacturer": "Maker Made",
    "start_gcode": "G28 ;Home\n G29 ;Auto Level\n G92 E0 ;Reset Extruder\n G1 Z5.0 F3000 ;Move Z Axis up\n G1 X25 Y295.0 Z0.28 F3000.0 ;Move to extrude\n G1 X250 Y295.0 Z0.28 F1500.0 E15 ;Draw the first line\n G1 X25 Y290.0 Z0.28 F3000.0 ;Move to side a little\n G1 X250 Y290.0 Z0.28 F1500.0 E30 ;Draw the second line\n G92 E0 ;Reset Extruder\n G1 Z5.0 F3000 ;Move Z Axis up",
    "end_gcode": "M104 S0\n M140 S0\n ;Retract the filament\n G92 E1\n G1 E-1 F300\n G28 X0 Y0\n G1 Y300 F3000 ;Move bed forward\n M84",
    "bed_temp": 50,
    "nozzle_temp": 220,
    "material_flow_percent": 100,
    "print_speed": 50,
    "travel_speed": 150,
    "dia_feed": 1.75,
    "build_volume_x": 300,
    "build_volume_y": 300,
    "build_volume_z": 400,
}
