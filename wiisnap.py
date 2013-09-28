import snapext
import cwiid
print "Please connect a Wiimote by pressing the 1 and 2 buttons now."
wm = cwiid.Wiimote()
def uids(q, l):
    r = []
    for i, j in enumerate(l):
        if j == q:
            r.append(str(i + 1))
    return r
def binlist(s):
    return ('0'*(20-len(bin(s))) + bin(s))[::-1]
    
wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC | cwiid.RPT_MOTIONPLUS | cwiid.RPT_NUNCHUK | cwiid.RPT_CLASSIC

@snapext.SnapHandler.route('/led/set')
def ledset(setting):
    wm.led = setting

@snapext.SnapHandler.route('/rumble')
def rumble(setting):
    wm.rumble = setting

@snapext.SnapHandler.route('/led/get')
def ledget():
    return wm.state['led']

@snapext.SnapHandler.route('/wiimote/getacc')
def wmacc(q):
    return wm.state['acc'][['x','y','z'].index(q)]

@snapext.SnapHandler.route('/wiimote/battery')
def wmbattery():
    return wm.state['battery']

@snapext.SnapHandler.route('/wiimote/buttons')
def wmbuttons():
    return ' '.join(uids('1', binlist(wm.state['buttons'])))

@snapext.SnapHandler.route('/nunchuk/getacc')
def nacc(q):
    return wm.state['nunchuk']['acc'][['x','y','z'].index(q)]

@snapext.SnapHandler.route('/nunchuk/buttons')
def nbuttons():
    return ' '.join(uids('1', binlist(wm.state['nunchuk']['buttons'])))

@snapext.SnapHandler.route('/nunchuk/stickpos')
def nacc(q):
    return wm.state['nunchuk']['stick'][['x','y'].index(q)]

@snapext.SnapHandler.route('/classic/buttons')
def cbuttons():
    return ' '.join(uids('1', binlist(wm.state['classic']['buttons'])))

@snapext.SnapHandler.route('/classic/stick')
def cstick(d,q):
    return wm.state['classic']['%s_stick'%d][q]

if __name__ == "__main__":
    snapext.main(snapext.SnapHandler, 1280)
