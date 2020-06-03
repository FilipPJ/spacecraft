function [orientationquaternion]= get_orientation(sat_pos,target_pos,q_eci)
    reference_pos = sat_pos-target_pos;
    angZY = reference_pos(3)/reference_pos(2);
    angZX = reference_pos(3)/reference_pos(1);
    q1 = CL_rot_angles2quat(1, angZY * %pi/180); //X axis rotation angle
    q2 = CL_rot_angles2quat(2, -angZX * %pi/180); //Y axis rotation angle
    q = q1*q2; 
/*Quaternion q describes rotation of a satellite aligned with ECI axis to a orientation which the Z axis points at the target point*/
    q_out = c1/q_eci; 
    return q_out;
endfunction

/*
funkcja która przyjmuje pozycję satelity i pozycję stacji bazowej ->
zwracała potrzebny kwaternion orientacji satelity
podajemy ACDS kwaternion względem ECI
*/
