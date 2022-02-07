norabidea = False
u = 0
DFRobotMaqueenPlus.i2c_init()
DFRobotMaqueenPlus.PID(PID.OFF)

def on_forever():
    global u, norabidea
    u = DFRobotMaqueenPlus.ultra_sonic(PIN.P1, PIN.P2)
    if u < 20 and u != 0:
        norabidea = Math.random_boolean()
        if norabidea == True:
            DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, 100)
            DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, 0)
            basic.pause(1000)
        else:
            DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, 0)
            DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, 100)
            basic.pause(1000)
    else:
        DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CW, 100)
basic.forever(on_forever)
