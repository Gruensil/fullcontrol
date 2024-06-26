default_initial_settings = {
    "name": "Liquid",
    "manufacturer": "Liquid 3D",
    "start_gcode": "G21 ; set units to millimeters\nG90 ; use absolute positioning\nM83 ; relative extrusion mode\nM104 S{data['nozzle_temp']} ; set extruder temp\nM140 S{data['bed_temp']} ; set bed temp\nM190 S{data['bed_temp']} ; wait for bed temp\nM109 S{data['nozzle_temp']} ; wait for extruder temp\nG32 ; mesh bed leveling\nG92 E0.0 ; reset extruder distance position\nG1 X0 Y-2 Z0.3 F4000.0 ; go outside print area\nG1 X60.0 E9.0 F1000.0 ; intro line\nG1 X110.0 E15.5 F1000.0 ; intro line\nG92 E0.0 ; reset extruder distance position",
    "end_gcode": "M104 S0 ; turn off extruder\nM140 S0 ; turn off heatbed\nM106 S0 ; turn off fan\nG91 ; relative positioning\nG1 Z1 F360 ; lift Z by 1mm\nG90 ; absolute positioning\nG1 X10 Y200 F3200; home X axis and push Y forward\nG1 Z200 F1200; home Z axis\nM84 ; disable motors",
    "bed_temp": 60,
    "nozzle_temp": 200,
    "material_flow_percent": 100,
    "print_speed": 35,
    "travel_speed": 150,
    "dia_feed": 1.75,
    "build_volume_x": 200,
    "build_volume_y": 200,
    "build_volume_z": 200,
}
