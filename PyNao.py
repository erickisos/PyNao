#!/usr/bin/python
# -*- encoding:utf-8 -*-
__author__ = 'erick'


has_pil = True

try:
    from PIL import Image
except Exception as e:
    print(e)
    has_pil = False

import math
import sys
import time
import almath
from PyQt4 import QtCore, QtGui
from naoqi import ALProxy
import threading
import vision_definitions as vd

from mainWindowComplex import Ui_MainWindow


class Ventana(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.win = Ui_MainWindow()
        self.win.setupUi(self)
        self.win.textIP.setText("127.0.0.1")
        self.win.textPORT.setText("9559")
        self.win.excitedButton.setText("Macarena")
        self.win.rockButton.setText("RockYou")
        self.win.autonoModeButton.setText("STOP ALL!")
        self.connect(self.win.volumeSlider, QtCore.SIGNAL('valueChanged(int)'), self.volumeControl)
        self.connect(self.win.readSensorButton, QtCore.SIGNAL('clicked()'), self.leerSensores)
        self.connect(self.win.AnySayButton, QtCore.SIGNAL('clicked()'), self.animatedSay)
        self.connect(self.win.calmDownButton, QtCore.SIGNAL('clicked()'), self.Cool)
        self.connect(self.win.excitedButton, QtCore.SIGNAL('clicked()'),
                     self.bailaMacarena)
        self.connect(self.win.explicandoButton, QtCore.SIGNAL('clicked()'), self.Explain)
        self.connect(self.win.rockButton, QtCore.SIGNAL('clicked()'),
                     self.RockYou)
        self.connect(self.win.kongButton, QtCore.SIGNAL('clicked()'), self.kingKong)
        self.connect(self.win.musclesButton, QtCore.SIGNAL('clicked()'), self.muscle)
        self.connect(self.win.r2d2Button, QtCore.SIGNAL('clicked()'), self.arturito)
        self.connect(self.win.nopeButton, QtCore.SIGNAL('clicked()'), self.Nope)
        self.connect(self.win.yeahButton, QtCore.SIGNAL('clicked()'), self.runBehaviorDialog)
        self.connect(self.win.vacuumButton, QtCore.SIGNAL('clicked()'), self.aspiradora)
        self.connect(self.win.flyingButton, QtCore.SIGNAL('clicked()'), self.avioncito)
        self.connect(self.win.hotspotButton, QtCore.SIGNAL('clicked()'), self.crearHotspot)
        self.connect(self.win.turnFlButton, QtCore.SIGNAL('clicked()'), self.GiroFrenteIzquierda)
        self.connect(self.win.turnFrButton, QtCore.SIGNAL('clicked()'), self.GiroFrenteDerecha)
        self.connect(self.win.turnBlButton, QtCore.SIGNAL('clicked()'), self.GiroBackIzquierda)
        self.connect(self.win.turnBrButton, QtCore.SIGNAL('clicked()'), self.GiroBackDerecha)
        self.connect(self.win.batteryButton, QtCore.SIGNAL('clicked()'), self.batteryStatus)
        self.connect(self.win.autonoModeButton, QtCore.SIGNAL('clicked()'),
                     self.stopAll)
        self.connect(self.win.frontButton, QtCore.SIGNAL('clicked()'), self.avanza)
        self.connect(self.win.backButton, QtCore.SIGNAL('clicked()'), self.retrocede)
        self.connect(self.win.rightButton, QtCore.SIGNAL('clicked()'), self.derecha)
        self.connect(self.win.leftButton, QtCore.SIGNAL('clicked()'), self.izquierda)
        self.connect(self.win.sitButton, QtCore.SIGNAL('clicked()'), self.sentarse)
        self.connect(self.win.sayButton, QtCore.SIGNAL('clicked()'), self.hablando)
        self.connect(self.win.WakeButton, QtCore.SIGNAL('clicked()'), self.wakeUp)
        self.connect(self.win.ConnectButton, QtCore.SIGNAL('clicked()'), self.Connect)
        self.connect(self.win.RestButton, QtCore.SIGNAL('clicked()'), self.rest)
        self.connect(self.win.pictureButton, QtCore.SIGNAL('clicked()'), self.videoCam)
        self.connect(self.win.saludoButton, QtCore.SIGNAL('clicked()'), self.Saludar)
        #self.connect(self.win.sayText, QtCore.SIGNAL('returnPressed()'), self.hablando)
        #self.connect(self.win.textPORT, QtCore.SIGNAL('returnPressed()'), self.Connect)

    def stopAll(self):
        IP = str(self.win.textIP.text())
        PORT = int(self.win.textPORT.text())
        try:
            bh = ALProxy("ALBehaviorManager", IP, PORT)
            mv = ALProxy("ALMotion", IP, PORT)
            pst = ALProxy("ALRobotPosture", IP, PORT)
            bh.stopAllBehaviors()
            mv.stopMove()
            pst.goToPosture("Stand", 0.3)
            mv.rest()
        except Exception, e:
            print(e)

    def RockYou(self):
        IP = str(self.win.textIP.text())
        PORT = int(self.win.textPORT.text())
        try:
            bh = ALProxy("ALBehaviorManager", IP, PORT)
            if bh.isBehaviorInstalled('User/wewillrockyouv6-22529a/RockYou'):
                bh.runBehavior('User/wewillrockyouv6-22529a/RockYou')
        except Exception, e:
            print(e)

    def runBehaviorDialog(self):
        IP = str(self.win.textIP.text())
        PORT = int(self.win.textPORT.text())
        try:
            bhProxy = ALProxy("ALBehaviorManager", IP, PORT)
            bhProxy.startBehavior("User/holamundo-2a0070/behavior_1")
        except Exception, e:
            print(e)

    def Rock(self):
        print("Rock")
        pass

    def Yeah(self):
        print("Yeah!")
        pass

    def Explain(self):
        print("Explicando")
        pass

    def Cool(self):
        print("Calm Down")
        pass

    def excited(self):
        print("Excited")
        pass

    def GiroFrenteIzquierda(self):
        IP = str(self.win.textIP.text())
        PORT = int(self.win.textPORT.text())
        try:
            motionProxy = ALProxy("ALMotion", IP, PORT)
            postureProxy = ALProxy("ALRobotPosture", IP, PORT)
            motionProxy.wakeUp()
            postureProxy.goToPosture("StandInit", 0.5)
            motionProxy.moveTo(0,0, math.pi/2.0)
        except Exception, e:
            print("Error")
            print e

    def GiroFrenteDerecha(self):
        IP = str(self.win.textIP.text())
        PORT = int(self.win.textPORT.text())
        try:
            motionProxy = ALProxy("ALMotion", IP, PORT)
            postureProxy = ALProxy("ALRobotPosture", IP, PORT)
            motionProxy.wakeUp()
            postureProxy.goToPosture("StandInit", 0.5)
            motionProxy.moveTo(0,0, -(math.pi/2.0))
        except Exception, e:
            print("Error")
            print(e)

    def GiroBackIzquierda(self):
        print("Giro de reversaIzquierda")
        pass

    def GiroBackDerecha(self):
        print("Giro de reversaDerecha")
        pass

    def crearHotspot(self):
        print("Soy un AP")
        try:
            IP = str(self.win.textIP.text())
            PORT = int(self.win.textPORT.text())
            alconProxy = ALProxy("ALConnectionManager", IP, PORT)
            alconProxy.enableTethering("wifi", "mynao", "naonaonao")
            print "wifi", "mynao", "naonaonao"
        except Exception as e:
            print(e)
        ttsProxy = ALProxy("ALTextToSpeech", IP, PORT)
        ttsProxy.say("Soy un jotspod!")

    def volumeControl(self):
        print("Volume changed")
        pass

    def animatedSay(self):
        IP = str(self.win.textIP.text())
        PORT = int(self.win.textPORT.text())
        animatedProxy = ALProxy("ALAnimatedSpeech", IP, PORT)
        ttsProxy = ALProxy("ALTextToSpeech", IP, PORT)
        ttsProxy.setLanguage("Spanish")
        text = "^mode(contextual)" #+ str(self.win.comboBox.currentText())
        print type(self.win.AniSayText.text())
        dialog = str(self.win.AniSayText.text())
        animatedProxy.say(text + dialog)

    def batteryStatus(self):
        print("Checking Battery")
        IP = str(self.win.textIP.text())
        PORT = int(self.win.textPORT.text())
        batteryProxy = ALProxy("ALBattery", IP, PORT)
        carga = batteryProxy.getBatteryCharge()
        self.win.batteryText.setText("%d por ciento" %(carga))

    def aspiradora(self):
        print("Vacuum")
        try:
            IP = str(self.win.textIP.text())
            PORT = int(self.win.textPORT.text())
            saludaProxy = ALProxy("ALAnimatedSpeech", IP, PORT)
            saludaProxy.say("^start(animations/Stand/Waiting/Vacuum_1) ^wait(animations/Stand/Waiting/Vacuum_1)")

        except:
            print("No quiero")

    def avioncito(self):
        print("I believe...")
        try:
            IP = str(self.win.textIP.text())
            PORT = int(self.win.textPORT.text())
            motionProxy = ALProxy("ALMotion", IP, PORT)
            motionProxy.setFallManagerEnabled(False)
            saludaProxy = ALProxy("ALAnimatedSpeech", IP, PORT)
            saludaProxy.say("^start(animations/Stand/Waiting/SpaceShuttle_1) ^wait(animations/Stand/Waiting/SpaceShuttle_1)")
        except Exception, e:
            print(e)

    def muscle(self):
        print("Muscles")
        try:
            IP = str(self.win.textIP.text())
            PORT = int(self.win.textPORT.text())
            saludaProxy = ALProxy("ALAnimatedSpeech", IP, PORT)
            saludaProxy.say("^start(animations/Stand/Waiting/Fitness_3) ^wait(animations/Stand/Waiting/Fitness_3)")
        except:
            print("No puedo")

    def arturito(self):
        print("R2D2")
        pass

    def kingKong(self):
        print("KingKong")
        pass

    def Nope(self):
        print("Nope")
        IP = str(self.win.textIP.text())
        PORT = int(self.win.textPORT.text())
        try:
            bhProxy = ALProxy("ALBehaviorManager", IP, PORT)
            #bhProxy.stop
        except:
            print("")

    def leerSensores(self):
        IP = str(self.win.textIP.text())
        PORT = int(self.win.textPORT.text())
        memoryProxy = ALProxy("ALMemory", IP, PORT)
        sonarProxy = ALProxy("ALSonar", IP, PORT)
        sonarProxy.subscribe("pynao")

        AccX = memoryProxy.getData("Device/SubDeviceList/InertialSensor/AccX/Sensor/Value")
        AccY = memoryProxy.getData("Device/SubDeviceList/InertialSensor/AccY/Sensor/Value")
        AccZ = memoryProxy.getData("Device/SubDeviceList/InertialSensor/AccZ/Sensor/Value")

        GyrX = memoryProxy.getData("Device/SubDeviceList/InertialSensor/GyrX/Sensor/Value")
        GyrY = memoryProxy.getData("Device/SubDeviceList/InertialSensor/GyrY/Sensor/Value")

        usL = memoryProxy.getData("Device/SubDeviceList/US/Left/Sensor/Value")
        usR = memoryProxy.getData("Device/SubDeviceList/US/Right/Sensor/Value")
        sonarProxy.unsubscribe("pynao")
        print(type(AccX))
        print(type(GyrX))
        self.win.AccelXtext.setText("x: " + str(round(AccX, 2)))
        self.win.AccelYtext.setText("y: " + str(round(AccY, 2)))
        self.win.AccelZtext.setText("z: " + str(round(AccZ, 2)))
        self.win.GyroXtext.setText("x: " + str(round(GyrX, 2)))
        self.win.GyroYtext.setText("y: " + str(round(GyrY, 2)))
        self.win.USLeftText.setText("%.2f m" %(usL))
        self.win.USRightText.setText("%.2f m" %(usR))

    def autonoMode(self):
        print("Ya Soy Autonomo")

                #Aquí acaba lo nuuevo, lo demás ahí está

    def avanza(self):
        IP = str(self.win.textIP.text())
        PORT = int(self.win.textPORT.text())
        try:
            motionProxy = ALProxy("ALMotion", IP, PORT)
            motionProxy.wakeUp()
            motionProxy.moveTo(0.5, 0.0, 0)
        except:
            print("no puedo avanzar")

    def retrocede(self):
        IP = str(self.win.textIP.text())
        PORT = int(self.win.textPORT.text())
        try:
            motionProxy = ALProxy("ALMotion", IP, PORT)
            motionProxy.wakeUp()
            motionProxy.moveTo(-0.5, 0.0, 0)
        except:
            print("no pude retroceder")

    def derecha(self):
        IP = str(self.win.textIP.text())
        PORT = int(self.win.textPORT.text())
        try:
            motionProxy = ALProxy("ALMotion", IP, PORT)
            motionProxy.wakeUp()
            motionProxy.moveTo(0.0, -0.5, 0)
        except:
            print("no logro moverme a la derecha")

    def izquierda(self):
        IP = str(self.win.textIP.text())
        PORT = int(self.win.textPORT.text())
        try:
            motionProxy = ALProxy("ALMotion", IP, PORT)
            motionProxy.wakeUp()
            motionProxy.moveTo(0.0, 0.5, 0)
        except:
            print("no logro moerme a la izquierda")

    def sentarse(self):
        IP = str(self.win.textIP.text())
        PORT = int(self.win.textPORT.text())
        try:
            motionProxy = ALProxy("ALMotion", IP, PORT)
            postureProxy = ALProxy("ALRobotPosture", IP, PORT)
            motionProxy.wakeUp()
            postureProxy.goToPosture("Sit", 1.0)
            motionProxy.rest()
        except:
            print("Quizá esto no es así")

    def Saludar(self):
        try:
            IP = str(self.win.textIP.text())
            PORT = int(self.win.textPORT.text())
            saludaProxy = ALProxy("ALAnimatedSpeech", IP, PORT)
            saludaProxy.say("^start(animations/Stand/Gestures/Hey_1) ^wait(animations/Stand/Gestures/Hey_1)")
        except:
            print("No jaló la vida")

    def hablando(self):
        try:
            IP = str(self.win.textIP.text())
            PORT = int(self.win.textPORT.text())
            sayProxy = ALProxy("ALTextToSpeech", IP, PORT)
            texto = str(self.win.sayText.text())
            sayProxy.say(texto)
            print("Ahora sí se pudo")
        except:
            print("Ni pedo, no salió")

    def videoCam(self):
        IP = str(self.win.textIP.text())
        PORT = int(self.win.textPORT.text())
        try:
            camProxy = ALProxy("ALVideoDevice", IP, PORT)
            client = camProxy.subscribe("python_client", vd.kVGA, 11, 5)
            momento = time.strftime("_%H%M%S_%d%m%y")
            image = camProxy.getImageRemote(client)
            camProxy.unsubscribe(client)
            im = Image.frombytes("RGB", (image[0], image[1]), image[6])
            im.save("selfie_%s.png" %momento, "PNG")
        except:
            print("Así no es chavo")

    def turnHead(self):
        IP = str(self.win.textIP.text())
        PORT = int(self.win.textPORT.text())
        angle = self.win.horizontalSlider.value()
        angulo = angle*almath.TO_RAD
        try:
            motionProxy = ALProxy("ALMotion", IP, PORT)
            motionProxy.setStiffnesses("Head", 1.0)
            motionProxy.setAngles("HeadYaw", angulo, 0.2)
            time.sleep(1.0)
            motionProxy.setStiffnesses("Head", 0.0)
        except:
            print("Error al conectar con Head")

    def rest(self):
        IP = str(self.win.textIP.text())
        PORT = int(self.win.textPORT.text())
        try:
            motionProxy = ALProxy("ALMotion", IP, PORT)
            motionProxy.rest()
            print("rest")
        except:
            print("Error Al Descansar")

    def Connect(self):
        print("Connect")
        IP = str(self.win.textIP.text())
        PORT = int(self.win.textPORT.text())
        try:
            ttsProxy = ALProxy("ALTextToSpeech", IP, PORT)
            ttsProxy.say("Conexión establecida")
        except:
            print("Error de conexión")

    def wakeUp(self):
        IP = str(self.win.textIP.text())
        PORT = int(self.win.textPORT.text())
        try:
            motionProxy = ALProxy("ALMotion", IP, PORT)
            motionProxy.wakeUp()
            robotPosture = ALProxy("ALRobotPosture", IP, PORT)
            robotPosture.goToPosture("Stand", 0.7)
            print("Awake")
        except:
            print("Error al despertar")

    def bailaMacarena(self):
        IP = str(self.win.textIP.text())
        PORT = int(self.win.textPORT.text())
        try:
            bh = ALProxy("ALBehaviorManager", IP, PORT)
            if bh.isBehaviorInstalled('User/macarena-566d69/Macarena'):
                print("Pos sí estuvo la macarena")
                bh.runBehavior("User/macarena-566d69/Macarena")
                print("Ya acabé de bailar")
        except Exception, e:
            print(e)


def main():
    app = QtGui.QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
