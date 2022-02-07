let norabidea = false
let u = 0
DFRobotMaqueenPlus.I2CInit()
DFRobotMaqueenPlus.PID(PID.OFF)
basic.forever(function () {
    u = DFRobotMaqueenPlus.ultraSonic(PIN.P1, PIN.P2)
    if (u < 20 && u != 0) {
        norabidea = Math.randomBoolean()
        if (norabidea == true) {
            DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, 100)
            DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CW, 0)
            basic.pause(1000)
        } else {
            DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, 0)
            DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CW, 100)
            basic.pause(1000)
        }
    } else {
        DFRobotMaqueenPlus.mototRun(Motors.ALL, Dir.CW, 100)
    }
})
