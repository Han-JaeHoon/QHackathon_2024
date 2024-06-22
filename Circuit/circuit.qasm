OPENQASM 2.0;
include "qelib1.inc";
qreg q[8];
creg c[8];
h q[0];
rz([0.8829856]) q[0];
h q[1];
rz([0.10203111]) q[1];
h q[2];
rz([1.3642341]) q[2];
h q[3];
rz([1.6254346]) q[3];
cx q[0],q[1];
rz([0.8829856]) q[1];
cx q[0],q[1];
cx q[1],q[2];
rz([0.10203111]) q[2];
cx q[1],q[2];
cx q[2],q[3];
rz([1.3642341]) q[3];
cx q[2],q[3];
h q[4];
rz([0.11995757]) q[4];
h q[5];
rz([0.7617787]) q[5];
h q[6];
rz([0.41467535]) q[6];
h q[7];
rz([0.5477866]) q[7];
cx q[4],q[5];
rz([0.11995757]) q[5];
cx q[4],q[5];
cx q[5],q[6];
rz([0.7617787]) q[6];
cx q[5],q[6];
cx q[6],q[7];
rz([0.41467535]) q[7];
cx q[6],q[7];
rx([0.14371413]) q[0];
ry([0.9436646]) q[0];
rz([0.01306617]) q[0];
rx([0.01574636]) q[1];
ry([0.3684163]) q[1];
rz([0.02103513]) q[1];
rx([0.77788323]) q[2];
ry([0.19325513]) q[2];
rz([0.20471233]) q[2];
rx([0.16486824]) q[3];
ry([0.6966121]) q[3];
rz([0.2067396]) q[3];
rx([0.70620644]) q[4];
ry([0.3279389]) q[4];
rz([0.00573939]) q[4];
rx([0.0467748]) q[5];
ry([0.8415177]) q[5];
rz([0.6689682]) q[5];
rx([0.15050918]) q[6];
ry([0.32400674]) q[6];
rz([0.97393656]) q[6];
rx([0.50145197]) q[7];
ry([0.5627268]) q[7];
rz([0.83460915]) q[7];
cx q[0],q[1];
cx q[1],q[2];
cx q[2],q[3];
cx q[3],q[4];
cx q[4],q[5];
cx q[5],q[6];
cx q[6],q[7];
rz(1.5707963267948966) q[4];
ry(3.141592653589793) q[4];
rz(10.995574287564276) q[4];
rz(1.5707963267948966) q[5];
ry(3.141592653589793) q[5];
rz(10.995574287564276) q[5];
rz(1.5707963267948966) q[6];
ry(3.141592653589793) q[6];
rz(10.995574287564276) q[6];
rz(1.5707963267948966) q[7];
ry(3.141592653589793) q[7];
rz(10.995574287564276) q[7];
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
measure q[3] -> c[3];
measure q[4] -> c[4];
measure q[5] -> c[5];
measure q[6] -> c[6];
measure q[7] -> c[7];
