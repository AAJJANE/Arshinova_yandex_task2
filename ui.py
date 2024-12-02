from PyQt6 import QtCore, QtWidgets


class Ui_qwidget(object):
    def setupUi(self, qwidget):
        qwidget.setObjectName("qwidget")
        qwidget.resize(507, 458)
        self.pushButton = QtWidgets.QPushButton(parent=qwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 410, 100, 30))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(qwidget)
        QtCore.QMetaObject.connectSlotsByName(qwidget)

    def retranslateUi(self, qwidget):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("qwidget", "draw"))
