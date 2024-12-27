# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_hid.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QStackedWidget, QStatusBar,
    QTextEdit, QToolBox, QToolButton, QVBoxLayout,
    QWidget)
import Icons_cr

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1218, 834)
        MainWindow.setMaximumSize(QSize(16777215, 834))
        MainWindow.setContextMenuPolicy(Qt.ActionsContextMenu)
        MainWindow.setStyleSheet(u"background-color: rgb(24, 24, 24);\n"
"\n"
"Qframe{\n"
"	background-color:rgb(100,100,100);\n"
"\n"
"}\n"
"\n"
"QToolBox{\n"
"	text-align:left;\n"
"	\n"
"	\n"
"	background-color: rgb(170, 255, 255);\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"	border-radius:5px;\n"
"\n"
"	\n"
"	background-color: rgb(170, 255, 255);\n"
"	text-align:left;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"\n"
"QLabel{\n"
"\n"
"	color:rgb(255,255,255);\n"
"\n"
"}\n"
"")
        self.formLayout_6 = QFormLayout(self.centralwidget)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.Menu_Esquerdo = QFrame(self.centralwidget)
        self.Menu_Esquerdo.setObjectName(u"Menu_Esquerdo")
        self.Menu_Esquerdo.setMinimumSize(QSize(1, 750))
        self.Menu_Esquerdo.setMaximumSize(QSize(250, 750))
        self.Menu_Esquerdo.setStyleSheet(u"\n"
"\n"
"Qframe{\n"
"	background-color:rgb(100,100,100);\n"
"\n"
"}\n"
"\n"
"QToolBox{\n"
"	text-align:left;\n"
"	\n"
"	\n"
"	background-color: rgb(170, 255, 255);\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"	border-radius:5px;\n"
"\n"
"	\n"
"	background-color: rgb(170, 255, 255);\n"
"	text-align:left;\n"
"}\n"
"\n"
"")
        self.Menu_Esquerdo.setFrameShape(QFrame.StyledPanel)
        self.Menu_Esquerdo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.Menu_Esquerdo)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_12.setContentsMargins(0, -1, 0, -1)
        self.toolBox = QToolBox(self.Menu_Esquerdo)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(192, 0))
        self.toolBox.setMaximumSize(QSize(250, 16777215))
        self.toolBox.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.toolBox.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(65,65,65);	\n"
"	border-top-left-radius:15px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        self.toolBox.setFrameShadow(QFrame.Raised)
        self.Page_home = QWidget()
        self.Page_home.setObjectName(u"Page_home")
        self.Page_home.setGeometry(QRect(0, 0, 192, 640))
        self.verticalLayout_2 = QVBoxLayout(self.Page_home)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.BT_Trecho = QPushButton(self.Page_home)
        self.BT_Trecho.setObjectName(u"BT_Trecho")
        self.BT_Trecho.setMinimumSize(QSize(0, 50))
        self.BT_Trecho.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(11)
        self.BT_Trecho.setFont(font)
        icon = QIcon()
        icon.addFile(u":/PNG/icons AF/TUBO2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BT_Trecho.setIcon(icon)
        self.BT_Trecho.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.BT_Trecho)

        self.BT_Conexao = QPushButton(self.Page_home)
        self.BT_Conexao.setObjectName(u"BT_Conexao")
        self.BT_Conexao.setMinimumSize(QSize(0, 50))
        self.BT_Conexao.setFont(font)
        self.BT_Conexao.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/PNG/icons AF/CONEX2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BT_Conexao.setIcon(icon1)
        self.BT_Conexao.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.BT_Conexao)

        self.BT_Vazao = QPushButton(self.Page_home)
        self.BT_Vazao.setObjectName(u"BT_Vazao")
        self.BT_Vazao.setMinimumSize(QSize(0, 50))
        self.BT_Vazao.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/ICO/icons AF/water_drops_icon_161227.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.BT_Vazao.setIcon(icon2)
        self.BT_Vazao.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.BT_Vazao)

        self.BT_Planilha = QPushButton(self.Page_home)
        self.BT_Planilha.setObjectName(u"BT_Planilha")
        self.BT_Planilha.setMinimumSize(QSize(0, 50))
        self.BT_Planilha.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/ICO/icons AF/Oxygen-Icons.org-Oxygen-Apps-ktorrent.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.BT_Planilha.setIcon(icon3)
        self.BT_Planilha.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.BT_Planilha)

        self.BT_Relatorio = QPushButton(self.Page_home)
        self.BT_Relatorio.setObjectName(u"BT_Relatorio")
        self.BT_Relatorio.setMinimumSize(QSize(0, 50))
        self.BT_Relatorio.setFont(font)
        self.BT_Relatorio.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(0,255,127);	\n"
"	border-top-left-radius:15px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/ICO/icons AF/Icojam-Blue-Bits-Document-checkbox.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.BT_Relatorio.setIcon(icon4)
        self.BT_Relatorio.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.BT_Relatorio)

        self.verticalSpacer = QSpacerItem(20, 146, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.Page_home, u"Home")
        self.Page_info_2 = QWidget()
        self.Page_info_2.setObjectName(u"Page_info_2")
        self.Page_info_2.setGeometry(QRect(0, 0, 192, 640))
        self.verticalLayout_15 = QVBoxLayout(self.Page_info_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.BT_chave = QPushButton(self.Page_info_2)
        self.BT_chave.setObjectName(u"BT_chave")
        self.BT_chave.setMinimumSize(QSize(0, 30))
        self.BT_chave.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(127,255,212);	\n"
"	border-top-left-radius:15px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/ICO/icons AF/icons8-chave-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BT_chave.setIcon(icon5)

        self.verticalLayout_15.addWidget(self.BT_chave)

        self.BT_ajuda = QPushButton(self.Page_info_2)
        self.BT_ajuda.setObjectName(u"BT_ajuda")
        self.BT_ajuda.setMinimumSize(QSize(0, 30))
        self.BT_ajuda.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(127,255,212);	\n"
"	border-top-left-radius:15px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/ICO/icons AF/icons8-ajuda-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BT_ajuda.setIcon(icon6)

        self.verticalLayout_15.addWidget(self.BT_ajuda)

        self.BT_metodologia = QPushButton(self.Page_info_2)
        self.BT_metodologia.setObjectName(u"BT_metodologia")
        self.BT_metodologia.setMinimumSize(QSize(0, 30))
        self.BT_metodologia.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(127,255,212);	\n"
"	border-top-left-radius:15px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/ICO/icons AF/icons8-livro-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BT_metodologia.setIcon(icon7)

        self.verticalLayout_15.addWidget(self.BT_metodologia)

        self.BT_info = QPushButton(self.Page_info_2)
        self.BT_info.setObjectName(u"BT_info")
        self.BT_info.setMinimumSize(QSize(0, 30))
        self.BT_info.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(127,255,212);	\n"
"	border-top-left-radius:15px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/ICO/icons AF/icons8-informa\u00e7\u00e3o-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BT_info.setIcon(icon8)

        self.verticalLayout_15.addWidget(self.BT_info)

        self.BT_termo = QPushButton(self.Page_info_2)
        self.BT_termo.setObjectName(u"BT_termo")
        self.BT_termo.setMinimumSize(QSize(0, 30))
        self.BT_termo.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(127,255,212);	\n"
"	border-top-left-radius:15px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/ICO/icons AF/icons8-contrato-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BT_termo.setIcon(icon9)

        self.verticalLayout_15.addWidget(self.BT_termo)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_2)

        self.toolBox.addItem(self.Page_info_2, u"Info")

        self.verticalLayout_12.addWidget(self.toolBox)

        self.frame_34 = QFrame(self.Menu_Esquerdo)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(0, 30))
        self.frame_34.setStyleSheet(u"image: url(:/ICO/icons AF/logoR06.png);")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_34)


        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.Menu_Esquerdo)

        self.Tela_Direita = QFrame(self.centralwidget)
        self.Tela_Direita.setObjectName(u"Tela_Direita")
        self.Tela_Direita.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.Tela_Direita.setFrameShape(QFrame.StyledPanel)
        self.Tela_Direita.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.Tela_Direita)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.verticalLayout_11.setContentsMargins(0, -1, 0, 0)
        self.BT_Toggle = QToolButton(self.Tela_Direita)
        self.BT_Toggle.setObjectName(u"BT_Toggle")
        self.BT_Toggle.setMinimumSize(QSize(0, 45))
        self.BT_Toggle.setMaximumSize(QSize(16777215, 45))
        self.BT_Toggle.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        icon10 = QIcon()
        icon10.addFile(u":/PNG/icons AF/menu_3876189.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BT_Toggle.setIcon(icon10)
        self.BT_Toggle.setIconSize(QSize(32, 32))
        self.BT_Toggle.setAutoRaise(True)

        self.verticalLayout_11.addWidget(self.BT_Toggle)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.stackedWidget = QStackedWidget(self.Tela_Direita)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 725))
        self.stackedWidget.setMaximumSize(QSize(16777215, 725))
        font1 = QFont()
        font1.setPointSize(10)
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.stackedWidget.setStyleSheet(u"\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	color: rgb(38, 38, 38);\n"
"	\n"
"	QLineEdit-color: rgb(43, 43, 43);")
        self.Page_Vazao = QWidget()
        self.Page_Vazao.setObjectName(u"Page_Vazao")
        self.gridLayout_7 = QGridLayout(self.Page_Vazao)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame = QFrame(self.Page_Vazao)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(400, 400))
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_25 = QFrame(self.frame)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 25))
        self.frame_25.setMaximumSize(QSize(16777215, 30))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.label_71 = QLabel(self.frame_25)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(30, 0, 31, 16))
        self.label_73 = QLabel(self.frame_25)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(100, 0, 31, 16))

        self.gridLayout_2.addWidget(self.frame_25, 0, 1, 1, 2)

        self.frame_16 = QFrame(self.frame)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(250, 16777215))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_16)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_83 = QLabel(self.frame_16)
        self.label_83.setObjectName(u"label_83")

        self.verticalLayout_10.addWidget(self.label_83)

        self.label_34 = QLabel(self.frame_16)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_10.addWidget(self.label_34)

        self.label_37 = QLabel(self.frame_16)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(180, 100))
        self.label_37.setLayoutDirection(Qt.LeftToRight)
        self.label_37.setWordWrap(False)

        self.verticalLayout_10.addWidget(self.label_37)

        self.label_38 = QLabel(self.frame_16)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_10.addWidget(self.label_38)

        self.label_36 = QLabel(self.frame_16)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_10.addWidget(self.label_36)

        self.label_33 = QLabel(self.frame_16)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_10.addWidget(self.label_33)

        self.label_39 = QLabel(self.frame_16)
        self.label_39.setObjectName(u"label_39")

        self.verticalLayout_10.addWidget(self.label_39)

        self.label_35 = QLabel(self.frame_16)
        self.label_35.setObjectName(u"label_35")

        self.verticalLayout_10.addWidget(self.label_35)

        self.label_40 = QLabel(self.frame_16)
        self.label_40.setObjectName(u"label_40")

        self.verticalLayout_10.addWidget(self.label_40)

        self.label_41 = QLabel(self.frame_16)
        self.label_41.setObjectName(u"label_41")

        self.verticalLayout_10.addWidget(self.label_41)


        self.gridLayout_2.addWidget(self.frame_16, 1, 0, 1, 1)

        self.frame_38 = QFrame(self.frame)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMaximumSize(QSize(80, 16777215))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_38)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.TX_P_BA = QDoubleSpinBox(self.frame_38)
        self.TX_P_BA.setObjectName(u"TX_P_BA")
        self.TX_P_BA.setMinimumSize(QSize(60, 20))
        self.TX_P_BA.setMaximumSize(QSize(60, 20))
        self.TX_P_BA.setValue(1.000000000000000)

        self.verticalLayout_8.addWidget(self.TX_P_BA)

        self.TX_P_BD = QDoubleSpinBox(self.frame_38)
        self.TX_P_BD.setObjectName(u"TX_P_BD")
        self.TX_P_BD.setMinimumSize(QSize(60, 20))
        self.TX_P_BD.setMaximumSize(QSize(60, 20))
        self.TX_P_BD.setValue(0.100000000000000)

        self.verticalLayout_8.addWidget(self.TX_P_BD)

        self.TX_P_VSC = QDoubleSpinBox(self.frame_38)
        self.TX_P_VSC.setObjectName(u"TX_P_VSC")
        self.TX_P_VSC.setMinimumSize(QSize(60, 20))
        self.TX_P_VSC.setMaximumSize(QSize(60, 20))
        self.TX_P_VSC.setValue(0.300000000000000)

        self.verticalLayout_8.addWidget(self.TX_P_VSC)

        self.TX_P_VSVD = QDoubleSpinBox(self.frame_38)
        self.TX_P_VSVD.setObjectName(u"TX_P_VSVD")
        self.TX_P_VSVD.setMinimumSize(QSize(60, 20))
        self.TX_P_VSVD.setMaximumSize(QSize(60, 20))
        self.TX_P_VSVD.setValue(32.000000000000000)

        self.verticalLayout_8.addWidget(self.TX_P_VSVD)

        self.TX_P_CH = QDoubleSpinBox(self.frame_38)
        self.TX_P_CH.setObjectName(u"TX_P_CH")
        self.TX_P_CH.setMinimumSize(QSize(60, 20))
        self.TX_P_CH.setMaximumSize(QSize(60, 20))
        self.TX_P_CH.setValue(0.100000000000000)

        self.verticalLayout_8.addWidget(self.TX_P_CH)

        self.TX_P_LV = QDoubleSpinBox(self.frame_38)
        self.TX_P_LV.setObjectName(u"TX_P_LV")
        self.TX_P_LV.setMinimumSize(QSize(60, 20))
        self.TX_P_LV.setMaximumSize(QSize(60, 20))
        self.TX_P_LV.setValue(0.300000000000000)

        self.verticalLayout_8.addWidget(self.TX_P_LV)

        self.TX_P_MIC = QDoubleSpinBox(self.frame_38)
        self.TX_P_MIC.setObjectName(u"TX_P_MIC")
        self.TX_P_MIC.setMinimumSize(QSize(60, 20))
        self.TX_P_MIC.setMaximumSize(QSize(60, 20))
        self.TX_P_MIC.setValue(2.800000000000000)

        self.verticalLayout_8.addWidget(self.TX_P_MIC)

        self.TX_P_DH = QDoubleSpinBox(self.frame_38)
        self.TX_P_DH.setObjectName(u"TX_P_DH")
        self.TX_P_DH.setMinimumSize(QSize(60, 20))
        self.TX_P_DH.setMaximumSize(QSize(60, 20))
        self.TX_P_DH.setValue(0.400000000000000)

        self.verticalLayout_8.addWidget(self.TX_P_DH)

        self.TX_P_MICS = QDoubleSpinBox(self.frame_38)
        self.TX_P_MICS.setObjectName(u"TX_P_MICS")
        self.TX_P_MICS.setMinimumSize(QSize(60, 20))
        self.TX_P_MICS.setMaximumSize(QSize(60, 20))
        self.TX_P_MICS.setValue(0.300000000000000)

        self.verticalLayout_8.addWidget(self.TX_P_MICS)

        self.TX_P_MICC = QDoubleSpinBox(self.frame_38)
        self.TX_P_MICC.setObjectName(u"TX_P_MICC")
        self.TX_P_MICC.setMinimumSize(QSize(60, 20))
        self.TX_P_MICC.setMaximumSize(QSize(60, 20))
        self.TX_P_MICC.setValue(0.300000000000000)

        self.verticalLayout_8.addWidget(self.TX_P_MICC)


        self.gridLayout_2.addWidget(self.frame_38, 1, 1, 1, 1)

        self.frame_14 = QFrame(self.frame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(60, 16777215))
        self.frame_14.setStyleSheet(u"QSpinBox:{\n"
"	\n"
"Border-color: rgb(117, 117, 117);\n"
"\n"
"\n"
"}")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_14)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.TX_Q_BA = QSpinBox(self.frame_14)
        self.TX_Q_BA.setObjectName(u"TX_Q_BA")
        self.TX_Q_BA.setMinimumSize(QSize(0, 20))
        self.TX_Q_BA.setMaximumSize(QSize(40, 20))

        self.verticalLayout_9.addWidget(self.TX_Q_BA)

        self.TX_Q_BD = QSpinBox(self.frame_14)
        self.TX_Q_BD.setObjectName(u"TX_Q_BD")
        self.TX_Q_BD.setMinimumSize(QSize(0, 20))
        self.TX_Q_BD.setMaximumSize(QSize(40, 16777215))

        self.verticalLayout_9.addWidget(self.TX_Q_BD)

        self.TX_Q_VS = QSpinBox(self.frame_14)
        self.TX_Q_VS.setObjectName(u"TX_Q_VS")
        self.TX_Q_VS.setMinimumSize(QSize(0, 20))
        self.TX_Q_VS.setMaximumSize(QSize(40, 16777215))

        self.verticalLayout_9.addWidget(self.TX_Q_VS)

        self.TX_Q_VSVD = QSpinBox(self.frame_14)
        self.TX_Q_VSVD.setObjectName(u"TX_Q_VSVD")
        self.TX_Q_VSVD.setMinimumSize(QSize(0, 20))
        self.TX_Q_VSVD.setMaximumSize(QSize(40, 16777215))

        self.verticalLayout_9.addWidget(self.TX_Q_VSVD)

        self.TX_Q_CH = QSpinBox(self.frame_14)
        self.TX_Q_CH.setObjectName(u"TX_Q_CH")
        self.TX_Q_CH.setMinimumSize(QSize(0, 20))
        self.TX_Q_CH.setMaximumSize(QSize(40, 16777215))

        self.verticalLayout_9.addWidget(self.TX_Q_CH)

        self.TX_Q_LV = QSpinBox(self.frame_14)
        self.TX_Q_LV.setObjectName(u"TX_Q_LV")
        self.TX_Q_LV.setMinimumSize(QSize(0, 20))
        self.TX_Q_LV.setMaximumSize(QSize(40, 16777215))

        self.verticalLayout_9.addWidget(self.TX_Q_LV)

        self.TX_Q_MIC = QSpinBox(self.frame_14)
        self.TX_Q_MIC.setObjectName(u"TX_Q_MIC")
        self.TX_Q_MIC.setMinimumSize(QSize(0, 20))
        self.TX_Q_MIC.setMaximumSize(QSize(40, 16777215))

        self.verticalLayout_9.addWidget(self.TX_Q_MIC)

        self.TX_Q_DH = QSpinBox(self.frame_14)
        self.TX_Q_DH.setObjectName(u"TX_Q_DH")
        self.TX_Q_DH.setMinimumSize(QSize(0, 20))
        self.TX_Q_DH.setMaximumSize(QSize(40, 16777215))

        self.verticalLayout_9.addWidget(self.TX_Q_DH)

        self.TX_Q_MICS = QSpinBox(self.frame_14)
        self.TX_Q_MICS.setObjectName(u"TX_Q_MICS")
        self.TX_Q_MICS.setMinimumSize(QSize(0, 20))
        self.TX_Q_MICS.setMaximumSize(QSize(40, 16777215))

        self.verticalLayout_9.addWidget(self.TX_Q_MICS)

        self.TX_Q_MICC = QSpinBox(self.frame_14)
        self.TX_Q_MICC.setObjectName(u"TX_Q_MICC")
        self.TX_Q_MICC.setMinimumSize(QSize(0, 20))
        self.TX_Q_MICC.setMaximumSize(QSize(40, 16777215))

        self.verticalLayout_9.addWidget(self.TX_Q_MICC)


        self.gridLayout_2.addWidget(self.frame_14, 1, 2, 1, 1)


        self.gridLayout_7.addWidget(self.frame, 3, 0, 1, 1)

        self.frame_10 = QFrame(self.Page_Vazao)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(400, 16777215))
        self.frame_10.setFrameShape(QFrame.WinPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_10)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame_23 = QFrame(self.frame_10)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(250, 16777215))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_23)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_63 = QLabel(self.frame_23)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMaximumSize(QSize(250, 60))

        self.verticalLayout_7.addWidget(self.label_63)

        self.label_78 = QLabel(self.frame_23)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setMaximumSize(QSize(250, 60))

        self.verticalLayout_7.addWidget(self.label_78)

        self.label_42 = QLabel(self.frame_23)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(250, 60))

        self.verticalLayout_7.addWidget(self.label_42)

        self.label_72 = QLabel(self.frame_23)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMaximumSize(QSize(250, 60))

        self.verticalLayout_7.addWidget(self.label_72)


        self.gridLayout_11.addWidget(self.frame_23, 0, 0, 1, 1)

        self.frame_39 = QFrame(self.frame_10)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(80, 0))
        self.frame_39.setMaximumSize(QSize(80, 16777215))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.TX_P_LP = QDoubleSpinBox(self.frame_39)
        self.TX_P_LP.setObjectName(u"TX_P_LP")
        self.TX_P_LP.setGeometry(QRect(10, 36, 60, 20))
        self.TX_P_LP.setMinimumSize(QSize(60, 20))
        self.TX_P_LP.setMaximumSize(QSize(60, 20))
        self.TX_P_LP.setValue(1.000000000000000)
        self.TX_P_PIAE = QDoubleSpinBox(self.frame_39)
        self.TX_P_PIAE.setObjectName(u"TX_P_PIAE")
        self.TX_P_PIAE.setGeometry(QRect(10, 62, 60, 20))
        self.TX_P_PIAE.setMinimumSize(QSize(60, 20))
        self.TX_P_PIAE.setMaximumSize(QSize(60, 20))
        self.TX_P_PIAE.setValue(0.100000000000000)
        self.TX_P_BE = QDoubleSpinBox(self.frame_39)
        self.TX_P_BE.setObjectName(u"TX_P_BE")
        self.TX_P_BE.setGeometry(QRect(10, 88, 60, 20))
        self.TX_P_BE.setMinimumSize(QSize(60, 20))
        self.TX_P_BE.setMaximumSize(QSize(60, 20))
        self.TX_P_BE.setValue(0.100000000000000)
        self.TX_P_PIA_2 = QDoubleSpinBox(self.frame_39)
        self.TX_P_PIA_2.setObjectName(u"TX_P_PIA_2")
        self.TX_P_PIA_2.setGeometry(QRect(10, 10, 60, 20))
        self.TX_P_PIA_2.setMinimumSize(QSize(60, 20))
        self.TX_P_PIA_2.setMaximumSize(QSize(60, 20))
        self.TX_P_PIA_2.setValue(0.700000000000000)

        self.gridLayout_11.addWidget(self.frame_39, 0, 1, 1, 1)

        self.frame_19 = QFrame(self.frame_10)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(60, 16777215))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_19)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.TX_Q_PIA = QSpinBox(self.frame_19)
        self.TX_Q_PIA.setObjectName(u"TX_Q_PIA")
        self.TX_Q_PIA.setMinimumSize(QSize(0, 20))
        self.TX_Q_PIA.setMaximumSize(QSize(40, 60))

        self.verticalLayout_6.addWidget(self.TX_Q_PIA)

        self.TX_Q_LP = QSpinBox(self.frame_19)
        self.TX_Q_LP.setObjectName(u"TX_Q_LP")
        self.TX_Q_LP.setMinimumSize(QSize(0, 20))
        self.TX_Q_LP.setMaximumSize(QSize(40, 60))

        self.verticalLayout_6.addWidget(self.TX_Q_LP)

        self.TX_Q_PIAE = QSpinBox(self.frame_19)
        self.TX_Q_PIAE.setObjectName(u"TX_Q_PIAE")
        self.TX_Q_PIAE.setMinimumSize(QSize(0, 20))
        self.TX_Q_PIAE.setMaximumSize(QSize(40, 60))

        self.verticalLayout_6.addWidget(self.TX_Q_PIAE)

        self.TX_Q_BE = QSpinBox(self.frame_19)
        self.TX_Q_BE.setObjectName(u"TX_Q_BE")
        self.TX_Q_BE.setMinimumSize(QSize(0, 20))
        self.TX_Q_BE.setMaximumSize(QSize(40, 60))

        self.verticalLayout_6.addWidget(self.TX_Q_BE)


        self.gridLayout_11.addWidget(self.frame_19, 0, 2, 1, 1)


        self.gridLayout_7.addWidget(self.frame_10, 5, 0, 1, 1)

        self.frame_12 = QFrame(self.Page_Vazao)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(400, 16777215))
        self.frame_12.setFrameShape(QFrame.WinPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_12)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, -1, -1, -1)
        self.frame_21 = QFrame(self.frame_12)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(250, 16777215))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_21)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_66 = QLabel(self.frame_21)
        self.label_66.setObjectName(u"label_66")

        self.verticalLayout_3.addWidget(self.label_66)

        self.label_75 = QLabel(self.frame_21)
        self.label_75.setObjectName(u"label_75")

        self.verticalLayout_3.addWidget(self.label_75)

        self.label_86 = QLabel(self.frame_21)
        self.label_86.setObjectName(u"label_86")

        self.verticalLayout_3.addWidget(self.label_86)


        self.gridLayout_3.addWidget(self.frame_21, 1, 0, 1, 1)

        self.frame_20 = QFrame(self.frame_12)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(60, 16777215))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TX_Q_TQ = QSpinBox(self.frame_20)
        self.TX_Q_TQ.setObjectName(u"TX_Q_TQ")
        self.TX_Q_TQ.setMaximumSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.TX_Q_TQ)

        self.TX_Q_LR = QSpinBox(self.frame_20)
        self.TX_Q_LR.setObjectName(u"TX_Q_LR")
        self.TX_Q_LR.setMaximumSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.TX_Q_LR)

        self.TX_Q_TL = QSpinBox(self.frame_20)
        self.TX_Q_TL.setObjectName(u"TX_Q_TL")
        self.TX_Q_TL.setMaximumSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.TX_Q_TL)


        self.gridLayout_3.addWidget(self.frame_20, 1, 2, 1, 1)

        self.frame_40 = QFrame(self.frame_12)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(80, 0))
        self.frame_40.setMaximumSize(QSize(80, 16777215))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_40)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.TX_P_TQ = QDoubleSpinBox(self.frame_40)
        self.TX_P_TQ.setObjectName(u"TX_P_TQ")
        self.TX_P_TQ.setMinimumSize(QSize(60, 20))
        self.TX_P_TQ.setMaximumSize(QSize(60, 20))
        self.TX_P_TQ.setValue(0.700000000000000)

        self.verticalLayout_13.addWidget(self.TX_P_TQ)

        self.TX_P_LR = QDoubleSpinBox(self.frame_40)
        self.TX_P_LR.setObjectName(u"TX_P_LR")
        self.TX_P_LR.setMinimumSize(QSize(60, 20))
        self.TX_P_LR.setMaximumSize(QSize(60, 20))
        self.TX_P_LR.setValue(1.000000000000000)

        self.verticalLayout_13.addWidget(self.TX_P_LR)

        self.TX_P_TL = QDoubleSpinBox(self.frame_40)
        self.TX_P_TL.setObjectName(u"TX_P_TL")
        self.TX_P_TL.setMinimumSize(QSize(60, 20))
        self.TX_P_TL.setMaximumSize(QSize(60, 20))
        self.TX_P_TL.setValue(0.400000000000000)

        self.verticalLayout_13.addWidget(self.TX_P_TL)


        self.gridLayout_3.addWidget(self.frame_40, 1, 1, 1, 1)


        self.gridLayout_7.addWidget(self.frame_12, 4, 0, 1, 1)

        self.label_98 = QLabel(self.Page_Vazao)
        self.label_98.setObjectName(u"label_98")
        font2 = QFont()
        font2.setPointSize(14)
        self.label_98.setFont(font2)
        self.label_98.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.label_98, 1, 0, 1, 1)

        self.label_25 = QLabel(self.Page_Vazao)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(0, 30))
        font3 = QFont()
        font3.setPointSize(12)
        self.label_25.setFont(font3)
        self.label_25.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.label_25, 2, 1, 1, 1)

        self.label_24 = QLabel(self.Page_Vazao)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 30))
        self.label_24.setFont(font3)
        self.label_24.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.label_24, 2, 0, 1, 1)

        self.frame_11 = QFrame(self.Page_Vazao)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_17 = QFrame(self.frame_11)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(250, 60))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.formLayout_13 = QFormLayout(self.frame_17)
        self.formLayout_13.setObjectName(u"formLayout_13")
        self.label_81 = QLabel(self.frame_17)
        self.label_81.setObjectName(u"label_81")

        self.formLayout_13.setWidget(0, QFormLayout.LabelRole, self.label_81)

        self.CK_INSERIR_VAZAO = QCheckBox(self.frame_17)
        self.CK_INSERIR_VAZAO.setObjectName(u"CK_INSERIR_VAZAO")
        self.CK_INSERIR_VAZAO.setMaximumSize(QSize(120, 16777215))

        self.formLayout_13.setWidget(1, QFormLayout.LabelRole, self.CK_INSERIR_VAZAO)

        self.SP_Vazao_Trecho = QDoubleSpinBox(self.frame_17)
        self.SP_Vazao_Trecho.setObjectName(u"SP_Vazao_Trecho")
        self.SP_Vazao_Trecho.setMinimumSize(QSize(25, 30))

        self.formLayout_13.setWidget(0, QFormLayout.FieldRole, self.SP_Vazao_Trecho)


        self.verticalLayout_5.addWidget(self.frame_17)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.frame_6 = QFrame(self.frame_11)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(250, 60))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_105 = QLabel(self.frame_6)
        self.label_105.setObjectName(u"label_105")

        self.horizontalLayout_5.addWidget(self.label_105)

        self.SP_velocidade = QDoubleSpinBox(self.frame_6)
        self.SP_velocidade.setObjectName(u"SP_velocidade")
        self.SP_velocidade.setMinimumSize(QSize(0, 30))
        self.SP_velocidade.setValue(2.500000000000000)

        self.horizontalLayout_5.addWidget(self.SP_velocidade)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_11)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(250, 60))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.frame_7)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_106 = QLabel(self.frame_7)
        self.label_106.setObjectName(u"label_106")

        self.gridLayout.addWidget(self.label_106, 0, 0, 1, 1)

        self.Slider_Temperatura = QSlider(self.frame_7)
        self.Slider_Temperatura.setObjectName(u"Slider_Temperatura")
        self.Slider_Temperatura.setMaximum(100)
        self.Slider_Temperatura.setSingleStep(10)
        self.Slider_Temperatura.setValue(20)
        self.Slider_Temperatura.setTracking(False)
        self.Slider_Temperatura.setOrientation(Qt.Horizontal)
        self.Slider_Temperatura.setInvertedAppearance(False)
        self.Slider_Temperatura.setTickPosition(QSlider.TicksBelow)
        self.Slider_Temperatura.setTickInterval(10)

        self.gridLayout.addWidget(self.Slider_Temperatura, 0, 1, 1, 1)

        self.LB_Temperatura = QLabel(self.frame_7)
        self.LB_Temperatura.setObjectName(u"LB_Temperatura")
        self.LB_Temperatura.setFont(font1)
        self.LB_Temperatura.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.LB_Temperatura, 1, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_7)


        self.gridLayout_7.addWidget(self.frame_11, 3, 1, 1, 1)

        self.frame_35 = QFrame(self.Page_Vazao)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"color: rgb(255, 255, 255);")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_35)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.BT_recuar_Vazao = QPushButton(self.frame_35)
        self.BT_recuar_Vazao.setObjectName(u"BT_recuar_Vazao")
        self.BT_recuar_Vazao.setMinimumSize(QSize(80, 30))
        self.BT_recuar_Vazao.setMaximumSize(QSize(80, 30))
        self.BT_recuar_Vazao.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(65,65,65);	\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/PNG/icons AF/rewind_747962.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BT_recuar_Vazao.setIcon(icon11)
        self.BT_recuar_Vazao.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.BT_recuar_Vazao)

        self.BT_Inserir = QPushButton(self.frame_35)
        self.BT_Inserir.setObjectName(u"BT_Inserir")
        self.BT_Inserir.setMinimumSize(QSize(120, 30))
        self.BT_Inserir.setMaximumSize(QSize(80, 30))
        self.BT_Inserir.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(65,65,65);	\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/PNG/icons AF/download_3484405.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BT_Inserir.setIcon(icon12)
        self.BT_Inserir.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.BT_Inserir)


        self.gridLayout_7.addWidget(self.frame_35, 4, 1, 1, 1)

        self.stackedWidget.addWidget(self.Page_Vazao)
        self.Page_Planilha = QWidget()
        self.Page_Planilha.setObjectName(u"Page_Planilha")
        self.verticalLayout_14 = QVBoxLayout(self.Page_Planilha)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_15 = QFrame(self.Page_Planilha)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 50))
        self.frame_15.setStyleSheet(u"\n"
"background-color: rgb(38, 38, 38);\n"
"color: rgb(255, 255, 255);")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_97 = QLabel(self.frame_15)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setMinimumSize(QSize(300, 0))
        self.label_97.setMaximumSize(QSize(300, 30))
        self.label_97.setFont(font2)
        self.label_97.setStyleSheet(u"\n"
"background-color: rgb(38, 38, 38);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.label_97)

        self.LB_aviso_plan = QLabel(self.frame_15)
        self.LB_aviso_plan.setObjectName(u"LB_aviso_plan")
        self.LB_aviso_plan.setMinimumSize(QSize(30, 0))
        self.LB_aviso_plan.setMaximumSize(QSize(150, 16777215))
        self.LB_aviso_plan.setStyleSheet(u"\n"
"background-color: rgb(38, 38, 38);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.LB_aviso_plan)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)


        self.verticalLayout_14.addWidget(self.frame_15)

        self.FR_container_planilha = QFrame(self.Page_Planilha)
        self.FR_container_planilha.setObjectName(u"FR_container_planilha")
        self.FR_container_planilha.setFrameShape(QFrame.StyledPanel)
        self.FR_container_planilha.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.FR_container_planilha)

        self.frame_41 = QFrame(self.Page_Planilha)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMaximumSize(QSize(16777215, 50))
        self.frame_41.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"color: rgb(255, 255, 255);")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_41)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.BT_salvar = QPushButton(self.frame_41)
        self.BT_salvar.setObjectName(u"BT_salvar")
        self.BT_salvar.setMinimumSize(QSize(80, 30))
        self.BT_salvar.setMaximumSize(QSize(80, 30))
        self.BT_salvar.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(65,65,65);	\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/PNG/icons AF/icons8-salvar-como-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BT_salvar.setIcon(icon13)
        self.BT_salvar.setIconSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.BT_salvar, 0, 0, 1, 1)

        self.BT_calcular = QPushButton(self.frame_41)
        self.BT_calcular.setObjectName(u"BT_calcular")
        self.BT_calcular.setMinimumSize(QSize(100, 30))
        self.BT_calcular.setMaximumSize(QSize(100, 30))
        self.BT_calcular.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(65,65,65);	\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/PNG/icons AF/icons8-calculadora-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BT_calcular.setIcon(icon14)
        self.BT_calcular.setIconSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.BT_calcular, 0, 4, 1, 1)

        self.BT_excluir = QPushButton(self.frame_41)
        self.BT_excluir.setObjectName(u"BT_excluir")
        self.BT_excluir.setMaximumSize(QSize(100, 30))
        self.BT_excluir.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(65,65,65);	\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/ICO/icons AF/icons8-excluir-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BT_excluir.setIcon(icon15)
        self.BT_excluir.setIconSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.BT_excluir, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.BT_carregar = QPushButton(self.frame_41)
        self.BT_carregar.setObjectName(u"BT_carregar")
        self.BT_carregar.setMaximumSize(QSize(100, 30))
        self.BT_carregar.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(65,65,65);	\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/PNG/icons AF/refresh_3484421.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BT_carregar.setIcon(icon16)
        self.BT_carregar.setIconSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.BT_carregar, 0, 1, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_41)

        self.frame_9 = QFrame(self.Page_Planilha)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 50))
        self.frame_9.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"color: rgb(255, 255, 255);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.SP_vazao_max = QDoubleSpinBox(self.frame_9)
        self.SP_vazao_max.setObjectName(u"SP_vazao_max")
        self.SP_vazao_max.setMinimumSize(QSize(60, 30))
        self.SP_vazao_max.setMaximumSize(QSize(60, 30))
        self.SP_vazao_max.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.horizontalLayout_6.addWidget(self.SP_vazao_max)

        self.label_23 = QLabel(self.frame_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(150, 0))
        self.label_23.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_6.addWidget(self.label_23)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.SP_reservatorio = QDoubleSpinBox(self.frame_9)
        self.SP_reservatorio.setObjectName(u"SP_reservatorio")
        self.SP_reservatorio.setMinimumSize(QSize(60, 30))
        self.SP_reservatorio.setMaximumSize(QSize(60, 16777215))
        font4 = QFont()
        font4.setKerning(True)
        self.SP_reservatorio.setFont(font4)
        self.SP_reservatorio.setFrame(True)
        self.SP_reservatorio.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.SP_reservatorio.setKeyboardTracking(True)

        self.horizontalLayout_6.addWidget(self.SP_reservatorio)

        self.label_30 = QLabel(self.frame_9)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(350, 30))
        self.label_30.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_6.addWidget(self.label_30)


        self.verticalLayout_14.addWidget(self.frame_9)

        self.stackedWidget.addWidget(self.Page_Planilha)
        self.Page_ajuda = QWidget()
        self.Page_ajuda.setObjectName(u"Page_ajuda")
        self.verticalLayout_16 = QVBoxLayout(self.Page_ajuda)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.txt_ajuda = QTextEdit(self.Page_ajuda)
        self.txt_ajuda.setObjectName(u"txt_ajuda")
        self.txt_ajuda.setEnabled(True)

        self.verticalLayout_16.addWidget(self.txt_ajuda)

        self.stackedWidget.addWidget(self.Page_ajuda)
        self.Page_info = QWidget()
        self.Page_info.setObjectName(u"Page_info")
        self.verticalLayout_18 = QVBoxLayout(self.Page_info)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.txt_info = QTextEdit(self.Page_info)
        self.txt_info.setObjectName(u"txt_info")
        self.txt_info.setEnabled(True)

        self.verticalLayout_18.addWidget(self.txt_info)

        self.stackedWidget.addWidget(self.Page_info)
        self.Page_metodologia = QWidget()
        self.Page_metodologia.setObjectName(u"Page_metodologia")
        self.verticalLayout_19 = QVBoxLayout(self.Page_metodologia)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.textEdit = QTextEdit(self.Page_metodologia)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_19.addWidget(self.textEdit)

        self.stackedWidget.addWidget(self.Page_metodologia)
        self.Page_termos = QWidget()
        self.Page_termos.setObjectName(u"Page_termos")
        self.verticalLayout_17 = QVBoxLayout(self.Page_termos)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.txt_termo = QTextEdit(self.Page_termos)
        self.txt_termo.setObjectName(u"txt_termo")
        self.txt_termo.setEnabled(True)

        self.verticalLayout_17.addWidget(self.txt_termo)

        self.stackedWidget.addWidget(self.Page_termos)
        self.Page_ativacao = QWidget()
        self.Page_ativacao.setObjectName(u"Page_ativacao")
        self.verticalLayout_21 = QVBoxLayout(self.Page_ativacao)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_13 = QFrame(self.Page_ativacao)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(500, 150))
        self.frame_13.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"color: rgb(255, 255, 255);")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_13)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.LB_ativacao = QLabel(self.frame_13)
        self.LB_ativacao.setObjectName(u"LB_ativacao")
        self.LB_ativacao.setMinimumSize(QSize(0, 30))
        self.LB_ativacao.setMaximumSize(QSize(16777215, 30))
        self.LB_ativacao.setFont(font1)
        self.LB_ativacao.setStyleSheet(u"")

        self.verticalLayout_20.addWidget(self.LB_ativacao)

        self.TX_ativacao = QLineEdit(self.frame_13)
        self.TX_ativacao.setObjectName(u"TX_ativacao")
        self.TX_ativacao.setMinimumSize(QSize(0, 30))
        self.TX_ativacao.setMaximumSize(QSize(350, 16777215))
        self.TX_ativacao.setFont(font)

        self.verticalLayout_20.addWidget(self.TX_ativacao)

        self.BT_ativacao = QPushButton(self.frame_13)
        self.BT_ativacao.setObjectName(u"BT_ativacao")
        self.BT_ativacao.setMinimumSize(QSize(0, 30))
        self.BT_ativacao.setMaximumSize(QSize(100, 16777215))
        self.BT_ativacao.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(127,255,212);	\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")

        self.verticalLayout_20.addWidget(self.BT_ativacao)


        self.verticalLayout_21.addWidget(self.frame_13)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_4)

        self.stackedWidget.addWidget(self.Page_ativacao)
        self.Page_Trecho = QWidget()
        self.Page_Trecho.setObjectName(u"Page_Trecho")
        self.gridLayout_5 = QGridLayout(self.Page_Trecho)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_37 = QFrame(self.Page_Trecho)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(500, 500))
        self.frame_37.setMaximumSize(QSize(500, 16777215))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_37)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_100 = QLabel(self.frame_37)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setMinimumSize(QSize(150, 30))
        self.label_100.setMaximumSize(QSize(16777215, 25))
        self.label_100.setFont(font)
        self.label_100.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_22.addWidget(self.label_100)

        self.tx_Nome = QTextEdit(self.frame_37)
        self.tx_Nome.setObjectName(u"tx_Nome")
        self.tx_Nome.setMinimumSize(QSize(150, 30))
        self.tx_Nome.setMaximumSize(QSize(150, 30))
        self.tx_Nome.setFont(font3)

        self.verticalLayout_22.addWidget(self.tx_Nome)

        self.verticalSpacer_6 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_22.addItem(self.verticalSpacer_6)

        self.label_101 = QLabel(self.frame_37)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setMinimumSize(QSize(150, 30))
        self.label_101.setMaximumSize(QSize(16777215, 25))
        self.label_101.setFont(font)

        self.verticalLayout_22.addWidget(self.label_101)

        self.CB_Origem_2 = QComboBox(self.frame_37)
        self.CB_Origem_2.setObjectName(u"CB_Origem_2")
        self.CB_Origem_2.setMinimumSize(QSize(150, 30))
        self.CB_Origem_2.setMaximumSize(QSize(150, 16777215))
        self.CB_Origem_2.setFont(font3)
        self.CB_Origem_2.setMaxVisibleItems(100000)

        self.verticalLayout_22.addWidget(self.CB_Origem_2)

        self.label_102 = QLabel(self.frame_37)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setMinimumSize(QSize(150, 30))
        self.label_102.setMaximumSize(QSize(16777215, 25))
        self.label_102.setFont(font)

        self.verticalLayout_22.addWidget(self.label_102)

        self.CB_Material = QComboBox(self.frame_37)
        self.CB_Material.setObjectName(u"CB_Material")
        self.CB_Material.setMinimumSize(QSize(150, 30))
        self.CB_Material.setMaximumSize(QSize(150, 16777215))
        self.CB_Material.setFont(font3)

        self.verticalLayout_22.addWidget(self.CB_Material)

        self.label_103 = QLabel(self.frame_37)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setMinimumSize(QSize(150, 30))
        self.label_103.setMaximumSize(QSize(16777215, 25))
        self.label_103.setFont(font)

        self.verticalLayout_22.addWidget(self.label_103)

        self.SP_Altura_Trecho = QDoubleSpinBox(self.frame_37)
        self.SP_Altura_Trecho.setObjectName(u"SP_Altura_Trecho")
        self.SP_Altura_Trecho.setMinimumSize(QSize(60, 30))
        self.SP_Altura_Trecho.setMaximumSize(QSize(80, 16777215))
        self.SP_Altura_Trecho.setFont(font1)
        self.SP_Altura_Trecho.setMaximum(1000000.000000000000000)

        self.verticalLayout_22.addWidget(self.SP_Altura_Trecho)

        self.label_104 = QLabel(self.frame_37)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setMinimumSize(QSize(150, 30))
        self.label_104.setMaximumSize(QSize(16777215, 25))
        self.label_104.setFont(font)

        self.verticalLayout_22.addWidget(self.label_104)

        self.SP_Comprimento = QDoubleSpinBox(self.frame_37)
        self.SP_Comprimento.setObjectName(u"SP_Comprimento")
        self.SP_Comprimento.setMinimumSize(QSize(60, 30))
        self.SP_Comprimento.setMaximumSize(QSize(80, 30))
        self.SP_Comprimento.setFont(font1)
        self.SP_Comprimento.setMaximum(10000000.000000000000000)

        self.verticalLayout_22.addWidget(self.SP_Comprimento)

        self.label_132 = QLabel(self.frame_37)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setMinimumSize(QSize(150, 30))
        self.label_132.setMaximumSize(QSize(16777215, 25))
        self.label_132.setFont(font)

        self.verticalLayout_22.addWidget(self.label_132)

        self.SP_pressao_nec_trecho = QDoubleSpinBox(self.frame_37)
        self.SP_pressao_nec_trecho.setObjectName(u"SP_pressao_nec_trecho")
        self.SP_pressao_nec_trecho.setMinimumSize(QSize(60, 30))
        self.SP_pressao_nec_trecho.setMaximumSize(QSize(80, 16777215))
        self.SP_pressao_nec_trecho.setFont(font1)
        self.SP_pressao_nec_trecho.setMaximum(10000000.000000000000000)

        self.verticalLayout_22.addWidget(self.SP_pressao_nec_trecho)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_7)


        self.gridLayout_5.addWidget(self.frame_37, 0, 0, 1, 1)

        self.frame_36 = QFrame(self.Page_Trecho)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(120, 100))
        self.frame_36.setMaximumSize(QSize(120, 100))
        self.frame_36.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"color: rgb(255, 255, 255);")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.BT_avancar_trecho = QPushButton(self.frame_36)
        self.BT_avancar_trecho.setObjectName(u"BT_avancar_trecho")
        self.BT_avancar_trecho.setGeometry(QRect(20, 30, 80, 30))
        self.BT_avancar_trecho.setMinimumSize(QSize(80, 30))
        self.BT_avancar_trecho.setMaximumSize(QSize(80, 30))
        self.BT_avancar_trecho.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(65,65,65);	\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/PNG/icons AF/fast-forward_747954 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.BT_avancar_trecho.setIcon(icon17)
        self.BT_avancar_trecho.setIconSize(QSize(30, 30))

        self.gridLayout_5.addWidget(self.frame_36, 0, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 0, 3, 1, 1)

        self.stackedWidget.addWidget(self.Page_Trecho)
        self.Page_conexao_PVC = QWidget()
        self.Page_conexao_PVC.setObjectName(u"Page_conexao_PVC")
        self.gridLayout_6 = QGridLayout(self.Page_conexao_PVC)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_99 = QLabel(self.Page_conexao_PVC)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setMaximumSize(QSize(16777215, 30))
        self.label_99.setFont(font2)
        self.label_99.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.label_99, 0, 0, 1, 2)

        self.frame_3 = QFrame(self.Page_conexao_PVC)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.BT_recuar_conexaoPVC = QPushButton(self.frame_3)
        self.BT_recuar_conexaoPVC.setObjectName(u"BT_recuar_conexaoPVC")
        self.BT_recuar_conexaoPVC.setMinimumSize(QSize(80, 30))
        self.BT_recuar_conexaoPVC.setMaximumSize(QSize(80, 30))
        self.BT_recuar_conexaoPVC.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(65,65,65);	\n"
"}")
        self.BT_recuar_conexaoPVC.setIcon(icon11)
        self.BT_recuar_conexaoPVC.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.BT_recuar_conexaoPVC)

        self.BT_avancar_conexaoPVC = QPushButton(self.frame_3)
        self.BT_avancar_conexaoPVC.setObjectName(u"BT_avancar_conexaoPVC")
        self.BT_avancar_conexaoPVC.setMinimumSize(QSize(80, 30))
        self.BT_avancar_conexaoPVC.setMaximumSize(QSize(80, 30))
        self.BT_avancar_conexaoPVC.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(65,65,65);	\n"
"}")
        self.BT_avancar_conexaoPVC.setIcon(icon17)
        self.BT_avancar_conexaoPVC.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.BT_avancar_conexaoPVC)


        self.gridLayout_6.addWidget(self.frame_3, 4, 0, 1, 1)

        self.frame_33 = QFrame(self.Page_conexao_PVC)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.formLayout_8 = QFormLayout(self.frame_33)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.frame_28 = QFrame(self.frame_33)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(300, 250))
        self.frame_28.setMaximumSize(QSize(300, 300))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_28)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label = QLabel(self.frame_28)
        self.label.setObjectName(u"label")

        self.gridLayout_9.addWidget(self.label, 0, 0, 1, 1)

        self.SP_COT90 = QSpinBox(self.frame_28)
        self.SP_COT90.setObjectName(u"SP_COT90")
        self.SP_COT90.setMinimumSize(QSize(50, 30))
        self.SP_COT90.setMaximumSize(QSize(50, 30))
        self.SP_COT90.setSizeIncrement(QSize(0, 0))

        self.gridLayout_9.addWidget(self.SP_COT90, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame_28)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_9.addWidget(self.label_2, 1, 0, 1, 1)

        self.SP_COT45 = QSpinBox(self.frame_28)
        self.SP_COT45.setObjectName(u"SP_COT45")
        self.SP_COT45.setMinimumSize(QSize(50, 30))
        self.SP_COT45.setMaximumSize(QSize(50, 30))
        self.SP_COT45.setSizeIncrement(QSize(0, 0))

        self.gridLayout_9.addWidget(self.SP_COT45, 1, 1, 1, 1)

        self.label_3 = QLabel(self.frame_28)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_9.addWidget(self.label_3, 2, 0, 1, 1)

        self.SP_CURV90 = QSpinBox(self.frame_28)
        self.SP_CURV90.setObjectName(u"SP_CURV90")
        self.SP_CURV90.setMinimumSize(QSize(50, 30))
        self.SP_CURV90.setMaximumSize(QSize(50, 30))
        self.SP_CURV90.setSizeIncrement(QSize(0, 0))

        self.gridLayout_9.addWidget(self.SP_CURV90, 2, 1, 1, 1)

        self.label_4 = QLabel(self.frame_28)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_9.addWidget(self.label_4, 3, 0, 1, 1)

        self.SP_CURV45 = QSpinBox(self.frame_28)
        self.SP_CURV45.setObjectName(u"SP_CURV45")
        self.SP_CURV45.setMinimumSize(QSize(50, 30))
        self.SP_CURV45.setMaximumSize(QSize(50, 30))
        self.SP_CURV45.setSizeIncrement(QSize(0, 0))

        self.gridLayout_9.addWidget(self.SP_CURV45, 3, 1, 1, 1)


        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.frame_28)

        self.frame_29 = QFrame(self.frame_33)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(300, 0))
        self.frame_29.setMaximumSize(QSize(300, 300))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_29)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_6 = QLabel(self.frame_29)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_12.addWidget(self.label_6, 0, 0, 1, 1)

        self.SP_RG_GAV = QSpinBox(self.frame_29)
        self.SP_RG_GAV.setObjectName(u"SP_RG_GAV")
        self.SP_RG_GAV.setMinimumSize(QSize(50, 30))
        self.SP_RG_GAV.setMaximumSize(QSize(50, 30))
        self.SP_RG_GAV.setSizeIncrement(QSize(0, 0))

        self.gridLayout_12.addWidget(self.SP_RG_GAV, 0, 1, 1, 1)

        self.label_8 = QLabel(self.frame_29)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_12.addWidget(self.label_8, 1, 0, 1, 1)

        self.SP_RG_RP = QSpinBox(self.frame_29)
        self.SP_RG_RP.setObjectName(u"SP_RG_RP")
        self.SP_RG_RP.setMinimumSize(QSize(50, 30))
        self.SP_RG_RP.setMaximumSize(QSize(50, 30))
        self.SP_RG_RP.setSizeIncrement(QSize(0, 0))

        self.gridLayout_12.addWidget(self.SP_RG_RP, 1, 1, 1, 1)

        self.label_10 = QLabel(self.frame_29)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_12.addWidget(self.label_10, 2, 0, 1, 1)

        self.spinBox_3 = QSpinBox(self.frame_29)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMinimumSize(QSize(50, 30))
        self.spinBox_3.setMaximumSize(QSize(50, 30))
        self.spinBox_3.setSizeIncrement(QSize(0, 0))

        self.gridLayout_12.addWidget(self.spinBox_3, 2, 1, 1, 1)

        self.label_13 = QLabel(self.frame_29)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_12.addWidget(self.label_13, 3, 0, 1, 1)

        self.SP_RG_ANG = QSpinBox(self.frame_29)
        self.SP_RG_ANG.setObjectName(u"SP_RG_ANG")
        self.SP_RG_ANG.setMinimumSize(QSize(50, 30))
        self.SP_RG_ANG.setMaximumSize(QSize(50, 30))
        self.SP_RG_ANG.setSizeIncrement(QSize(0, 0))

        self.gridLayout_12.addWidget(self.SP_RG_ANG, 3, 1, 1, 1)


        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.frame_29)

        self.frame_2 = QFrame(self.frame_33)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(300, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 300))
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_10.addWidget(self.label_5, 0, 0, 1, 1)

        self.SP_TDIR = QSpinBox(self.frame_2)
        self.SP_TDIR.setObjectName(u"SP_TDIR")
        self.SP_TDIR.setMinimumSize(QSize(50, 30))
        self.SP_TDIR.setMaximumSize(QSize(50, 30))
        self.SP_TDIR.setSizeIncrement(QSize(0, 0))

        self.gridLayout_10.addWidget(self.SP_TDIR, 0, 1, 1, 1)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_10.addWidget(self.label_7, 1, 0, 1, 1)

        self.SP_TLAT = QSpinBox(self.frame_2)
        self.SP_TLAT.setObjectName(u"SP_TLAT")
        self.SP_TLAT.setMinimumSize(QSize(50, 30))
        self.SP_TLAT.setMaximumSize(QSize(50, 30))
        self.SP_TLAT.setSizeIncrement(QSize(0, 0))

        self.gridLayout_10.addWidget(self.SP_TLAT, 1, 1, 1, 1)


        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.frame_2)

        self.frame_31 = QFrame(self.frame_33)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(300, 0))
        self.frame_31.setMaximumSize(QSize(300, 300))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_31)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_11 = QLabel(self.frame_31)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_13.addWidget(self.label_11, 0, 0, 1, 1)

        self.SP_ENTRADA_N = QSpinBox(self.frame_31)
        self.SP_ENTRADA_N.setObjectName(u"SP_ENTRADA_N")
        self.SP_ENTRADA_N.setMinimumSize(QSize(50, 30))
        self.SP_ENTRADA_N.setMaximumSize(QSize(50, 30))
        self.SP_ENTRADA_N.setSizeIncrement(QSize(0, 0))

        self.gridLayout_13.addWidget(self.SP_ENTRADA_N, 0, 1, 1, 1)

        self.label_14 = QLabel(self.frame_31)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_13.addWidget(self.label_14, 1, 0, 1, 1)

        self.SP_ENTRADA_B = QSpinBox(self.frame_31)
        self.SP_ENTRADA_B.setObjectName(u"SP_ENTRADA_B")
        self.SP_ENTRADA_B.setMinimumSize(QSize(50, 30))
        self.SP_ENTRADA_B.setMaximumSize(QSize(50, 30))
        self.SP_ENTRADA_B.setSizeIncrement(QSize(0, 0))

        self.gridLayout_13.addWidget(self.SP_ENTRADA_B, 1, 1, 1, 1)

        self.label_9 = QLabel(self.frame_31)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_13.addWidget(self.label_9, 2, 0, 1, 1)

        self.SP_ENTRADA_SC = QSpinBox(self.frame_31)
        self.SP_ENTRADA_SC.setObjectName(u"SP_ENTRADA_SC")
        self.SP_ENTRADA_SC.setMinimumSize(QSize(50, 30))
        self.SP_ENTRADA_SC.setMaximumSize(QSize(50, 30))
        self.SP_ENTRADA_SC.setSizeIncrement(QSize(0, 0))

        self.gridLayout_13.addWidget(self.SP_ENTRADA_SC, 2, 1, 1, 1)


        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.frame_31)

        self.frame_30 = QFrame(self.frame_33)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(300, 0))
        self.frame_30.setMaximumSize(QSize(300, 300))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_30)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_12 = QLabel(self.frame_30)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_14.addWidget(self.label_12, 0, 0, 1, 1)

        self.SP_VALV_PE = QSpinBox(self.frame_30)
        self.SP_VALV_PE.setObjectName(u"SP_VALV_PE")
        self.SP_VALV_PE.setMinimumSize(QSize(50, 30))
        self.SP_VALV_PE.setMaximumSize(QSize(50, 30))
        self.SP_VALV_PE.setSizeIncrement(QSize(0, 0))

        self.gridLayout_14.addWidget(self.SP_VALV_PE, 0, 1, 1, 1)

        self.label_15 = QLabel(self.frame_30)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_14.addWidget(self.label_15, 1, 0, 1, 1)

        self.SP_VALV_V = QSpinBox(self.frame_30)
        self.SP_VALV_V.setObjectName(u"SP_VALV_V")
        self.SP_VALV_V.setMinimumSize(QSize(50, 30))
        self.SP_VALV_V.setMaximumSize(QSize(50, 30))
        self.SP_VALV_V.setSizeIncrement(QSize(0, 0))

        self.gridLayout_14.addWidget(self.SP_VALV_V, 1, 1, 1, 1)

        self.label_16 = QLabel(self.frame_30)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_14.addWidget(self.label_16, 2, 0, 1, 1)

        self.SP_VALV_H = QSpinBox(self.frame_30)
        self.SP_VALV_H.setObjectName(u"SP_VALV_H")
        self.SP_VALV_H.setMinimumSize(QSize(50, 30))
        self.SP_VALV_H.setMaximumSize(QSize(50, 30))
        self.SP_VALV_H.setSizeIncrement(QSize(0, 0))

        self.gridLayout_14.addWidget(self.SP_VALV_H, 2, 1, 1, 1)


        self.formLayout_8.setWidget(2, QFormLayout.LabelRole, self.frame_30)


        self.gridLayout_6.addWidget(self.frame_33, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.Page_conexao_PVC)
        self.Page_conexao_FERRO = QWidget()
        self.Page_conexao_FERRO.setObjectName(u"Page_conexao_FERRO")
        self.verticalLayout_4 = QVBoxLayout(self.Page_conexao_FERRO)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_26 = QLabel(self.Page_conexao_FERRO)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 30))
        self.label_26.setMaximumSize(QSize(16777215, 30))
        self.label_26.setFont(font2)
        self.label_26.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label_26)

        self.frame_32 = QFrame(self.Page_conexao_FERRO)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_32)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_26 = QFrame(self.frame_32)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.formLayout_5 = QFormLayout(self.frame_26)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_21 = QLabel(self.frame_26)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_21)

        self.label_114 = QLabel(self.frame_26)
        self.label_114.setObjectName(u"label_114")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_114)

        self.SP_ENTRADA_N_F = QSpinBox(self.frame_26)
        self.SP_ENTRADA_N_F.setObjectName(u"SP_ENTRADA_N_F")
        self.SP_ENTRADA_N_F.setMinimumSize(QSize(50, 20))
        self.SP_ENTRADA_N_F.setMaximumSize(QSize(50, 20))

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.SP_ENTRADA_N_F)

        self.label_115 = QLabel(self.frame_26)
        self.label_115.setObjectName(u"label_115")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_115)

        self.SP_ENTRADA_B_F = QSpinBox(self.frame_26)
        self.SP_ENTRADA_B_F.setObjectName(u"SP_ENTRADA_B_F")
        self.SP_ENTRADA_B_F.setMinimumSize(QSize(50, 20))
        self.SP_ENTRADA_B_F.setMaximumSize(QSize(50, 20))

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.SP_ENTRADA_B_F)

        self.label_116 = QLabel(self.frame_26)
        self.label_116.setObjectName(u"label_116")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.label_116)

        self.SP_ENTRADA_SC_F = QSpinBox(self.frame_26)
        self.SP_ENTRADA_SC_F.setObjectName(u"SP_ENTRADA_SC_F")
        self.SP_ENTRADA_SC_F.setMinimumSize(QSize(50, 20))
        self.SP_ENTRADA_SC_F.setMaximumSize(QSize(50, 20))

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.SP_ENTRADA_SC_F)

        self.label_117 = QLabel(self.frame_26)
        self.label_117.setObjectName(u"label_117")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.label_117)

        self.SP_VALV_PE_F = QSpinBox(self.frame_26)
        self.SP_VALV_PE_F.setObjectName(u"SP_VALV_PE_F")
        self.SP_VALV_PE_F.setMinimumSize(QSize(50, 20))
        self.SP_VALV_PE_F.setMaximumSize(QSize(50, 20))

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.SP_VALV_PE_F)


        self.gridLayout_8.addWidget(self.frame_26, 1, 0, 1, 1)

        self.frame_8 = QFrame(self.frame_32)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_8)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_22 = QLabel(self.frame_8)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_22)

        self.label_118 = QLabel(self.frame_8)
        self.label_118.setObjectName(u"label_118")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_118)

        self.SP_VALV_V_4 = QSpinBox(self.frame_8)
        self.SP_VALV_V_4.setObjectName(u"SP_VALV_V_4")
        self.SP_VALV_V_4.setMinimumSize(QSize(50, 20))
        self.SP_VALV_V_4.setMaximumSize(QSize(50, 20))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.SP_VALV_V_4)

        self.label_119 = QLabel(self.frame_8)
        self.label_119.setObjectName(u"label_119")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_119)

        self.SP_VALV_H_25 = QSpinBox(self.frame_8)
        self.SP_VALV_H_25.setObjectName(u"SP_VALV_H_25")
        self.SP_VALV_H_25.setMinimumSize(QSize(50, 20))
        self.SP_VALV_H_25.setMaximumSize(QSize(50, 20))

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.SP_VALV_H_25)

        self.label_124 = QLabel(self.frame_8)
        self.label_124.setObjectName(u"label_124")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_124)

        self.SP_VALV_H_30 = QSpinBox(self.frame_8)
        self.SP_VALV_H_30.setObjectName(u"SP_VALV_H_30")
        self.SP_VALV_H_30.setMinimumSize(QSize(50, 20))
        self.SP_VALV_H_30.setMaximumSize(QSize(50, 20))

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.SP_VALV_H_30)

        self.label_130 = QLabel(self.frame_8)
        self.label_130.setObjectName(u"label_130")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_130)

        self.SP_VALV_H_36 = QSpinBox(self.frame_8)
        self.SP_VALV_H_36.setObjectName(u"SP_VALV_H_36")
        self.SP_VALV_H_36.setMinimumSize(QSize(50, 20))
        self.SP_VALV_H_36.setMaximumSize(QSize(50, 20))

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.SP_VALV_H_36)

        self.label_131 = QLabel(self.frame_8)
        self.label_131.setObjectName(u"label_131")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_131)

        self.SP_VALV_H_37 = QSpinBox(self.frame_8)
        self.SP_VALV_H_37.setObjectName(u"SP_VALV_H_37")
        self.SP_VALV_H_37.setMinimumSize(QSize(50, 20))
        self.SP_VALV_H_37.setMaximumSize(QSize(50, 20))

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.SP_VALV_H_37)

        self.label_143 = QLabel(self.frame_8)
        self.label_143.setObjectName(u"label_143")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_143)

        self.SP_TE_Red_12 = QSpinBox(self.frame_8)
        self.SP_TE_Red_12.setObjectName(u"SP_TE_Red_12")
        self.SP_TE_Red_12.setMinimumSize(QSize(50, 20))
        self.SP_TE_Red_12.setMaximumSize(QSize(50, 20))
        font5 = QFont()
        font5.setPointSize(8)
        self.SP_TE_Red_12.setFont(font5)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.SP_TE_Red_12)


        self.gridLayout_8.addWidget(self.frame_8, 0, 2, 1, 1)

        self.frame_18 = QFrame(self.frame_32)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.formLayout_4 = QFormLayout(self.frame_18)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_20 = QLabel(self.frame_18)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_20)

        self.label_110 = QLabel(self.frame_18)
        self.label_110.setObjectName(u"label_110")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_110)

        self.SP_RG_GAV_F = QSpinBox(self.frame_18)
        self.SP_RG_GAV_F.setObjectName(u"SP_RG_GAV_F")
        self.SP_RG_GAV_F.setMinimumSize(QSize(50, 20))
        self.SP_RG_GAV_F.setMaximumSize(QSize(50, 20))

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.SP_RG_GAV_F)

        self.label_111 = QLabel(self.frame_18)
        self.label_111.setObjectName(u"label_111")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_111)

        self.SP_RG_RP_F = QSpinBox(self.frame_18)
        self.SP_RG_RP_F.setObjectName(u"SP_RG_RP_F")
        self.SP_RG_RP_F.setMinimumSize(QSize(50, 20))
        self.SP_RG_RP_F.setMaximumSize(QSize(50, 20))

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.SP_RG_RP_F)

        self.label_112 = QLabel(self.frame_18)
        self.label_112.setObjectName(u"label_112")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_112)

        self.SP_RG_ESF_F = QSpinBox(self.frame_18)
        self.SP_RG_ESF_F.setObjectName(u"SP_RG_ESF_F")
        self.SP_RG_ESF_F.setMinimumSize(QSize(50, 20))
        self.SP_RG_ESF_F.setMaximumSize(QSize(50, 20))

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.SP_RG_ESF_F)

        self.label_113 = QLabel(self.frame_18)
        self.label_113.setObjectName(u"label_113")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.label_113)

        self.SP_RG_ANG_F = QSpinBox(self.frame_18)
        self.SP_RG_ANG_F.setObjectName(u"SP_RG_ANG_F")
        self.SP_RG_ANG_F.setMinimumSize(QSize(50, 20))
        self.SP_RG_ANG_F.setMaximumSize(QSize(50, 20))

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.SP_RG_ANG_F)


        self.gridLayout_8.addWidget(self.frame_18, 1, 2, 1, 1)

        self.frame_5 = QFrame(self.frame_32)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_5)
        self.formLayout.setObjectName(u"formLayout")
        self.label_19 = QLabel(self.frame_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_19)

        self.label_108 = QLabel(self.frame_5)
        self.label_108.setObjectName(u"label_108")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_108)

        self.SP_TDIR_4 = QSpinBox(self.frame_5)
        self.SP_TDIR_4.setObjectName(u"SP_TDIR_4")
        self.SP_TDIR_4.setMinimumSize(QSize(50, 20))
        self.SP_TDIR_4.setMaximumSize(QSize(20, 50))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.SP_TDIR_4)

        self.label_109 = QLabel(self.frame_5)
        self.label_109.setObjectName(u"label_109")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_109)

        self.SP_TLAT_4 = QSpinBox(self.frame_5)
        self.SP_TLAT_4.setObjectName(u"SP_TLAT_4")
        self.SP_TLAT_4.setMinimumSize(QSize(50, 20))
        self.SP_TLAT_4.setMaximumSize(QSize(50, 20))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.SP_TLAT_4)

        self.label_125 = QLabel(self.frame_5)
        self.label_125.setObjectName(u"label_125")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_125)

        self.SP_VALV_H_33 = QSpinBox(self.frame_5)
        self.SP_VALV_H_33.setObjectName(u"SP_VALV_H_33")
        self.SP_VALV_H_33.setMinimumSize(QSize(50, 20))
        self.SP_VALV_H_33.setMaximumSize(QSize(50, 20))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.SP_VALV_H_33)

        self.label_126 = QLabel(self.frame_5)
        self.label_126.setObjectName(u"label_126")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_126)

        self.SP_VALV_H_32 = QSpinBox(self.frame_5)
        self.SP_VALV_H_32.setObjectName(u"SP_VALV_H_32")
        self.SP_VALV_H_32.setMinimumSize(QSize(50, 20))
        self.SP_VALV_H_32.setMaximumSize(QSize(50, 20))

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.SP_VALV_H_32)

        self.label_127 = QLabel(self.frame_5)
        self.label_127.setObjectName(u"label_127")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_127)

        self.SP_VALV_H_31 = QSpinBox(self.frame_5)
        self.SP_VALV_H_31.setObjectName(u"SP_VALV_H_31")
        self.SP_VALV_H_31.setMinimumSize(QSize(50, 20))
        self.SP_VALV_H_31.setMaximumSize(QSize(50, 20))

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.SP_VALV_H_31)

        self.label_128 = QLabel(self.frame_5)
        self.label_128.setObjectName(u"label_128")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_128)

        self.SP_VALV_H_34 = QSpinBox(self.frame_5)
        self.SP_VALV_H_34.setObjectName(u"SP_VALV_H_34")
        self.SP_VALV_H_34.setMinimumSize(QSize(50, 20))
        self.SP_VALV_H_34.setMaximumSize(QSize(50, 20))

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.SP_VALV_H_34)

        self.label_129 = QLabel(self.frame_5)
        self.label_129.setObjectName(u"label_129")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_129)

        self.SP_VALV_H_35 = QSpinBox(self.frame_5)
        self.SP_VALV_H_35.setObjectName(u"SP_VALV_H_35")
        self.SP_VALV_H_35.setMinimumSize(QSize(50, 20))
        self.SP_VALV_H_35.setMaximumSize(QSize(50, 20))

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.SP_VALV_H_35)


        self.gridLayout_8.addWidget(self.frame_5, 0, 1, 1, 1)

        self.frame_4 = QFrame(self.frame_32)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.frame_4)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_18 = QLabel(self.frame_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_18)

        self.label_46 = QLabel(self.frame_4)
        self.label_46.setObjectName(u"label_46")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_46)

        self.SP_COT90_F = QSpinBox(self.frame_4)
        self.SP_COT90_F.setObjectName(u"SP_COT90_F")
        self.SP_COT90_F.setMinimumSize(QSize(50, 20))
        self.SP_COT90_F.setMaximumSize(QSize(50, 20))

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.SP_COT90_F)

        self.label_67 = QLabel(self.frame_4)
        self.label_67.setObjectName(u"label_67")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_67)

        self.SP_COT45_F = QSpinBox(self.frame_4)
        self.SP_COT45_F.setObjectName(u"SP_COT45_F")
        self.SP_COT45_F.setMinimumSize(QSize(50, 20))
        self.SP_COT45_F.setMaximumSize(QSize(50, 20))

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.SP_COT45_F)

        self.label_68 = QLabel(self.frame_4)
        self.label_68.setObjectName(u"label_68")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_68)

        self.SP_CURV90_F = QSpinBox(self.frame_4)
        self.SP_CURV90_F.setObjectName(u"SP_CURV90_F")
        self.SP_CURV90_F.setMinimumSize(QSize(50, 20))
        self.SP_CURV90_F.setMaximumSize(QSize(50, 20))

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.SP_CURV90_F)

        self.label_107 = QLabel(self.frame_4)
        self.label_107.setObjectName(u"label_107")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_107)

        self.SP_CURV45_F = QSpinBox(self.frame_4)
        self.SP_CURV45_F.setObjectName(u"SP_CURV45_F")
        self.SP_CURV45_F.setMinimumSize(QSize(50, 20))
        self.SP_CURV45_F.setMaximumSize(QSize(50, 20))

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.SP_CURV45_F)

        self.label_121 = QLabel(self.frame_4)
        self.label_121.setObjectName(u"label_121")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.label_121)

        self.SP_CURV90_Fem_F = QSpinBox(self.frame_4)
        self.SP_CURV90_Fem_F.setObjectName(u"SP_CURV90_Fem_F")
        self.SP_CURV90_Fem_F.setMinimumSize(QSize(50, 20))
        self.SP_CURV90_Fem_F.setMaximumSize(QSize(50, 20))

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.SP_CURV90_Fem_F)

        self.label_122 = QLabel(self.frame_4)
        self.label_122.setObjectName(u"label_122")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.label_122)

        self.SP_CURV90_MF_F = QSpinBox(self.frame_4)
        self.SP_CURV90_MF_F.setObjectName(u"SP_CURV90_MF_F")
        self.SP_CURV90_MF_F.setMinimumSize(QSize(50, 20))
        self.SP_CURV90_MF_F.setMaximumSize(QSize(50, 20))

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.SP_CURV90_MF_F)

        self.label_123 = QLabel(self.frame_4)
        self.label_123.setObjectName(u"label_123")

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.label_123)

        self.SP_CURV90_M_F = QSpinBox(self.frame_4)
        self.SP_CURV90_M_F.setObjectName(u"SP_CURV90_M_F")
        self.SP_CURV90_M_F.setMinimumSize(QSize(50, 20))
        self.SP_CURV90_M_F.setMaximumSize(QSize(50, 20))

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.SP_CURV90_M_F)

        self.label_120 = QLabel(self.frame_4)
        self.label_120.setObjectName(u"label_120")

        self.formLayout_3.setWidget(8, QFormLayout.LabelRole, self.label_120)

        self.SP_COT90_SLat_F = QSpinBox(self.frame_4)
        self.SP_COT90_SLat_F.setObjectName(u"SP_COT90_SLat_F")
        self.SP_COT90_SLat_F.setMinimumSize(QSize(50, 20))
        self.SP_COT90_SLat_F.setMaximumSize(QSize(50, 20))

        self.formLayout_3.setWidget(8, QFormLayout.FieldRole, self.SP_COT90_SLat_F)


        self.gridLayout_8.addWidget(self.frame_4, 0, 0, 1, 1)

        self.frame_22 = QFrame(self.frame_32)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 80))
        self.frame_22.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"color: rgb(255, 255, 255);")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.BT_recuar_conexaoFERRO = QPushButton(self.frame_22)
        self.BT_recuar_conexaoFERRO.setObjectName(u"BT_recuar_conexaoFERRO")
        self.BT_recuar_conexaoFERRO.setMinimumSize(QSize(80, 30))
        self.BT_recuar_conexaoFERRO.setMaximumSize(QSize(80, 30))
        self.BT_recuar_conexaoFERRO.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(65,65,65);	\n"
"}")
        self.BT_recuar_conexaoFERRO.setIcon(icon11)
        self.BT_recuar_conexaoFERRO.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.BT_recuar_conexaoFERRO)

        self.BT_avancar_conexaoFERRO = QPushButton(self.frame_22)
        self.BT_avancar_conexaoFERRO.setObjectName(u"BT_avancar_conexaoFERRO")
        self.BT_avancar_conexaoFERRO.setMinimumSize(QSize(80, 30))
        self.BT_avancar_conexaoFERRO.setMaximumSize(QSize(80, 30))
        self.BT_avancar_conexaoFERRO.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(65,65,65);	\n"
"}")
        self.BT_avancar_conexaoFERRO.setIcon(icon17)
        self.BT_avancar_conexaoFERRO.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.BT_avancar_conexaoFERRO)


        self.gridLayout_8.addWidget(self.frame_22, 2, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_32)

        self.stackedWidget.addWidget(self.Page_conexao_FERRO)

        self.verticalLayout_11.addWidget(self.stackedWidget)


        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.Tela_Direita)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(2)
        self.CB_Material.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.BT_Trecho.setText(QCoreApplication.translate("MainWindow", u"                Trecho", None))
        self.BT_Conexao.setText(QCoreApplication.translate("MainWindow", u"            Conex\u00f5es", None))
        self.BT_Vazao.setText(QCoreApplication.translate("MainWindow", u"  Vaz\u00e3o de Projeto", None))
        self.BT_Planilha.setText(QCoreApplication.translate("MainWindow", u"Planilha de Press\u00f5es", None))
        self.BT_Relatorio.setText(QCoreApplication.translate("MainWindow", u"           Gerar Excel", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Page_home), QCoreApplication.translate("MainWindow", u"Home", None))
        self.BT_chave.setText(QCoreApplication.translate("MainWindow", u"                 Chave de Ativa\u00e7\u00e3o", None))
        self.BT_ajuda.setText(QCoreApplication.translate("MainWindow", u"                                      Ajuda", None))
        self.BT_metodologia.setText(QCoreApplication.translate("MainWindow", u"                            Metodologia", None))
        self.BT_info.setText(QCoreApplication.translate("MainWindow", u"                            Informa\u00e7\u00f5es", None))
        self.BT_termo.setText(QCoreApplication.translate("MainWindow", u"                         Termos de uso", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Page_info_2), QCoreApplication.translate("MainWindow", u"Info", None))
        self.BT_Toggle.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"peso", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"qtda", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"BANHEIRA", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"BIDE", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"VASO SAN. C/ CAIXA", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"VASO SAN. C/ V\u00c1LVULA", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"CHUVEIRO EL\u00c9TRICO", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"LAVAT\u00d3RIO", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"MICT\u00d3RIO C/ SIF\u00c3O", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"DUCHA", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"MICT\u00d3RIO S/ SIF\u00c3O", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"MICT\u00d3RIO CALHA", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"PIA", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"LAVADOURA DE PRATOS", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"PIA TORNEIRA EL\u00c9TRICA", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"BEBEDOURO", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"TANQUE", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"LAVADOURA DE ROUPAS", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"TORNEIRA DE LAVAGEM", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"> Vaz\u00e3o de Projeto</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_25.setToolTip(QCoreApplication.translate("MainWindow", u"Especifique uma vaz\u00e3o para o trecho", None))
#endif // QT_CONFIG(tooltip)
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Vaz\u00e3o definida", None))
#if QT_CONFIG(tooltip)
        self.label_24.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/TUTORIAL/icons AF/tutorial/RES_MCMV_VILE_vazaoTrecho_AB.png\" height=\"200\"/><img src=\":/TUTORIAL/icons AF/tutorial/RES_MCMV_VILE_vazao_BC.png\" height=\"200\"/></p><p>M\u00e9todo dos pesos determina a vaz\u00e3o ponderada por simultaneidade de uso das <br/>pe\u00e7as de acordo com as pe\u00e7as a serem atendidas a montante do trecho </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"M\u00e9todo dos Pesos", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"VAZ\u00c3O DE PROJETO [L/s]", None))
        self.CK_INSERIR_VAZAO.setText(QCoreApplication.translate("MainWindow", u"Especificar vaz\u00e3o", None))
#if QT_CONFIG(tooltip)
        self.label_105.setToolTip(QCoreApplication.translate("MainWindow", u"Velocidade m\u00e1xima no trecho, recomenda-se que n\u00e3o passe de 3 m/s", None))
#endif // QT_CONFIG(tooltip)
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Velocidade m\u00e1xima [m/s]", None))
#if QT_CONFIG(tooltip)
        self.frame_7.setToolTip(QCoreApplication.translate("MainWindow", u"Personalize a temperatura da \u00e1gua", None))
#endif // QT_CONFIG(tooltip)
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Temperatura [\u00b0C]", None))
#if QT_CONFIG(tooltip)
        self.Slider_Temperatura.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/ICO/icons AF/Fatcow-Farm-Fresh-Temperature-1.ico\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.LB_Temperatura.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.BT_recuar_Vazao.setText(QCoreApplication.translate("MainWindow", u"Recuar", None))
#if QT_CONFIG(tooltip)
        self.BT_Inserir.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.BT_Inserir.setText(QCoreApplication.translate("MainWindow", u"Inserir Trecho", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#959595;\">Planilha de Press\u00e3o</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.LB_aviso_plan.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u00c9 necess\u00e1rio recalcular a planilha sempre que houver modifica\u00e7\u00f5es</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.LB_aviso_plan.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/ICO/icons AF/icons8-general-warning-sign-48.png\" width=\"22\"/></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.BT_salvar.setStatusTip(QCoreApplication.translate("MainWindow", u"Salvar os c\u00e1lculos", None))
#endif // QT_CONFIG(statustip)
        self.BT_salvar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
#if QT_CONFIG(tooltip)
        self.BT_calcular.setToolTip(QCoreApplication.translate("MainWindow", u"Calcula a press\u00e3o para especifica\u00e7\u00e3o de pressurizadora ou altua do reservat\u00f3rio", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.BT_calcular.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.BT_calcular.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.BT_calcular.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.BT_calcular.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
#if QT_CONFIG(tooltip)
        self.BT_excluir.setToolTip(QCoreApplication.translate("MainWindow", u"Selecione uma linha para excluir", None))
#endif // QT_CONFIG(tooltip)
        self.BT_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.BT_carregar.setText(QCoreApplication.translate("MainWindow", u"Carregar", None))
#if QT_CONFIG(statustip)
        self.label_23.setStatusTip(QCoreApplication.translate("MainWindow", u"Vaz\u00e3o m\u00e1xima para especifica\u00e7\u00e3o de pressurizadora", None))
#endif // QT_CONFIG(statustip)
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Vaz\u00e3o m\u00e1xima (m\u00b3/h)", None))
#if QT_CONFIG(statustip)
        self.label_30.setStatusTip(QCoreApplication.translate("MainWindow", u"Press\u00e3o manom\u00e9trica em (mca), ou altura do reservat\u00f3rio em (m)", None))
#endif // QT_CONFIG(statustip)
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Altura necess\u00e1ria do reservat\u00f3rio a partir da refer\u00eancia (m)<br/>ou press\u00e3o em (mca) para pressurizadoras.</p></body></html>", None))
        self.txt_ajuda.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\"> </span><a name=\"_Toc149643819\"></a><span style=\" font-size:8pt; font-weight:600;\">1</span><span style=\" font-size:8pt; font-weight:600;\"> INSERINDO TRECHO</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8.5pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0p"
                        "x; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">1.1</span><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\"> Adicione um nome para identificar o trecho em NOME</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">1.2</span><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\"> Escolha a origem do trecho, de onde ele parte, ou onde come\u00e7a. Deve-se lembrar que a origem \u00e9 importante para que se saiba a perda de carga acumulada em"
                        " quaisquer pontos.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">1.3</span><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\"> Insira a altura do em que o trecho se encontra, a partir de uma refer\u00eancia escolhida, recomendamos que seja o n\u00edvel do piso t\u00e9rreo como altura 0.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">todas as alturas inseridas"
                        " ser\u00e3o relativas a ela. Se o reservat\u00f3rio estiver a 30 m de altura, ser\u00e1 30m a partir do ponto escolhido para altura 0.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">1.4 Material:</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">Escolha o material da tubula\u00e7\u00e3o, que \u00e9 importante para o c\u00e1lculo da perda de carga.</span><span style=\" font-si"
                        "ze:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">1.5 Comprimento do Trecho:</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">Adicione o comprimento total do trecho em an\u00e1lise em metros</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-se"
                        "rif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">1.6 Press\u00e3o necess\u00e1ria:</span><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\"><br />Insira a press\u00e3o necess\u00e1ria no trecho em [mca] metro coluna d'\u00e1gua, 1 mca = 10 kPa em unidade de press\u00e3o. Normalmente \u00e9 necess\u00e1rio que em qualquer trecho<br />da tubula\u00e7\u00e3o tenha pelo menos 0.5 mca de press\u00e3o, ou 5 kPa. Em pontos de utiliza\u00e7\u00e3o, as pe\u00e7as hidr\u00e1ulicas requerem pelo menos 1mca, pode variar de equipamento para equipamento</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-"
                        "size:8pt;\">isso deve ser verificado em projeto. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00c9 necess\u00e1rio atentar-se as press\u00f5es m\u00e1ximas e m\u00ednimas, sendo a press\u00e3o din\u00e2mica m\u00e1xima nos pontos de utiliza\u00e7\u00e3o 40 mca = 400 kPa, exceto se especificado pelo fabricante. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">press\u00e3o m\u00ednima de 1mca. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-lef"
                        "t:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8.5pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"_Toc149643820\"></a><span style=\" font-size:8pt; font-weight:600;\">2</span><span style=\" font-size:8pt; font-weight:600;\">. CONEX\u00d5ES</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">\u00a0</span><span style=\" font-size:8pt;\"> </span><"
                        "/p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">Insira a quantidade de conex\u00f5es, presentes no trecho.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8.5pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8.5pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"_Toc149643821\"></a><span style=\" font-size:8pt; font-weight:600;\">3</span><span styl"
                        "e=\" font-size:8pt; font-weight:600;\">. VAZ\u00c3O DE PROJETO</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8.5pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">3.1 M\u00c9TODO DOS PESOS</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span s"
                        "tyle=\" font-family:'Arial,sans-serif'; font-size:8pt;\">Nesse item define-se qual ser\u00e1 a vaz\u00e3o de projeto do trecho em Litros por Segundo [L/s]. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">No m\u00e9todo dos pesos atribui-se um peso de acordo com a frequ\u00eancia e simultaneidade de uso das pe\u00e7as, de maneira a resultar em di\u00e2metros menores, \u00e9 o m\u00e9todo comumente </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">utilizado na maioria dos projetos, note que os pesos n\u00e3o s\u00e3o normativos e podem ser personalizados de acordo com o perfil de uso do empreendimento </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent"
                        ":0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">3.2 VAZ\u00c3O DEFINIDA</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">Esse m\u00e9todo pode-se calcular o trecho indicando qual \u00e9 a vaz\u00e3o previamente calculada ou especificada em [L/s]</span><span style=\" "
                        "font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">pode ser utilizada para calcular sistema de hidrantes por exemplo, inserindo a vaz\u00e3o necess\u00e1ria no trecho, lembrando sempre de somar as vaz\u00f5es quando </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">do trecho parte mais de um hidrante. As vaz\u00f5es necess\u00e1rias e press\u00f5es a serem a atendidas podem ser verificadas nas instru\u00e7\u00f5es t\u00e9cnicas do Corpo de Bombeiros</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:60"
                        "0;\">3.3 VELOCIDADE:</span><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\"><br />Especifique qual a velocidade no trecho, as normas costumam recomendar que n\u00e3o ultrapasse 3 m/s, para que se evite patologias de origem hidr\u00e1ulica. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">3.4 TEMPERATURA:<br /></span><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">Insira a temperatura da \u00e1gua, por padr\u00e3o os c\u00e1lculos s\u00e3o realizados a 20 \u00b0C, apresentando pouca influ\u00eancia nos resultados. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0"
                        "px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8.5pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"_Toc149643822\"></a><span style=\" font-size:8pt; font-weight:600;\">4</span><span style=\" font-size:8pt; font-weight:600;\">. PLANILHA DE PRESS\u00c3O </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">4.1 </span><span style=\" font-family:'Arial,sans-serif'; font-size:"
                        "8pt;\">Ap\u00f3s inserir todos os trechos do projeto, ou o(s) trecho cr\u00edtico(s). \u00c9 necess\u00e1rio clicar no Bot\u00e3o Calcular para obter a altura do reservat\u00f3rio e a press\u00e3o manom\u00e9trica, </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">deve-se atentar no tipo de alimenta\u00e7\u00e3o se for pressurizado com reservat\u00f3rio inferior atendendo direto aos pontos, a altura do reservat\u00f3rio ser\u00e1 a press\u00e3o necess\u00e1ria para </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">a pressurizadora. Se a alimenta\u00e7\u00e3o por reservat\u00f3rio superior, a press\u00e3o necess\u00e1ria \u00e9 a diferen\u00e7a entre a altura do reservat\u00f3rio e o maior trecho na planilha. </spa"
                        "n></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">A Vaz\u00e3o em [m\u00b3/h] \u00e9 a vaz\u00e3o m\u00e1xima convertida de litros por segundo para metros c\u00fabicos por hora.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8.5pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"_Toc149643823\"><"
                        "/a><span style=\" font-size:8pt; font-weight:600;\">5</span><span style=\" font-size:8pt; font-weight:600;\">. SUBSTITUINDO UM TRECHO</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8.5pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">Para substituir um trecho j\u00e1 inserido calculado ou n\u00e3o, basta inserir novamente usando o mesmo nome de trecho e as informa\u00e7\u00f5es ser\u00e3o subscritas, lembrando a necessidade de recalcular o projeto para que o programa identifique qual a situa\u00e7\u00e3o mais cr\u00edtica e determine a press\u00e3o necess\u00e1ria</span><span style=\" font-family:'Arial,sans-serif'; font-size:8."
                        "5pt;\">. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8.5pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"_Toc149643824\"></a><span style=\" font-size:8pt; font-weight:600;\">6</span><span style=\" font-size:8pt; font-weight:600;\">. EXCLUINDO UM TRECHO</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8.5pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'"
                        "; font-size:8pt;\">Para excluir um trecho, basta selecionar a linha do trecho na tabela e clicar no Bot\u00e3o excluir, vale lembrar sempre que sempre que for alterado informa\u00e7\u00f5es na tabela, \u00e9 necess\u00e1rio </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">recalcular o trecho.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8.5pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"_Toc149643825\"></a><span style=\" font-size:8pt; font-weight:600;\">7</span><span style=\" font-size:8pt; font-weight:600;\">. SALVANDO</span"
                        "><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8.5pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">Os dados da tabela podem ser salvos em formato CSV ou XLSX, e recarregados novamente caso seja necess\u00e1rio, apenas clicando no bot\u00e3o SALVAR, ou GERAR EXCEl </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8.5pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-inde"
                        "nt:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8.5pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"_Toc149643826\"></a><span style=\" font-size:8pt; font-weight:600;\">8</span><span style=\" font-size:8pt; font-weight:600;\">. Nomenclaturas</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8.5pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">Planilha de press\u00e3o</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0"
                        "px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">Colunas:</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">Trecho</span><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\"> = Nome escolhido para o trecho em an\u00e1lise</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0"
                        "</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">Origem </span><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">= Onde inicia o trecho ou a partir de qual.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">Mat</span><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\"> = Material da tubula\u00e7\u00e3o </span></p>\n"
"<p style=\" marg"
                        "in-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">DN[mm]</span><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\"> = Di\u00e2metro Nominal da tubula\u00e7\u00e3o em mil\u00edmetros</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-famil"
                        "y:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">Di[mm</span><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">] = di\u00e2metro interno da tubula\u00e7\u00e3o em mil\u00edmetros</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">L[m]</span><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\"> = comprimento do trecho em an\u00e1lise em metros</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font"
                        "-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">L eq[m]</span><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\"> = comprimento equivalente devido as conex\u00f5es em metros.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">L tot[m</span><span style=\" font-family:'Arial,sans-serif'; font-size:8"
                        "pt;\">] = comprimento equivalente + comprimento do trecho em metros</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">h[m]</span><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\"> = altura do trecho em an\u00e1lise em metros a partir da refer\u00eancia escolhida</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span><"
                        "/p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">V[m/s]</span><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\"> = velocidade de escoamento no trecho em metros por segundo. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">Q[L/s]</span><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\"> = vaz\u00e3o do trecho em litros por segundo</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin"
                        "-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">Dh[mca]</span><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\"> = perda de carga(perda de press\u00e3o) do trecho em metro coluna d'\u00e1gua.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'A"
                        "rial,sans-serif'; font-size:8pt; font-weight:600;\">P disp[mca</span><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">] = press\u00e3o dispon\u00edvel em metro coluna d'\u00e1gua</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">temp[\u00b0C</span><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">] = temperatura da \u00e1gua em celcius</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'"
                        "Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">P nec [mca] </span><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">= Press\u00e3o necess\u00e1ria no ponto de utiliza\u00e7\u00e3o ou no interior da tubula\u00e7\u00e3o em metro coluna d'\u00e1gua</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">P res[mc"
                        "a]</span><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\"> = P nec + P disp</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">P resultante[mca</span><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">] = press\u00e3o calculada para que haja press\u00e3o o suficiente no trecho desfavor\u00e1vel menos a press\u00e3o residual (P res). </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</"
                        "span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">FoFo</span><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\"> = Tubula\u00e7\u00f5es em Ferro fundido</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\">\u00a0</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,sans-serif'; font-size:8pt; font-weight:600;\">mca</span><span style=\" font-family:'Arial,sans-serif'; font-size:8pt;\"> = unidade de medida de press\u00e3o em metro coluna d'\u00e1gua</span><spa"
                        "n style=\" font-size:8pt;\"> </span></p></body></html>", None))
        self.txt_info.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Informa\u00e7\u00f5es </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Athena Devs</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-"
                        "type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">contato:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"athenadevs9@gmail.com\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">athenadevs9@gmail.com</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-righ"
                        "t:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Refer\u00eancia de  icons</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"www.icons8.com.br\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">www.icons8.com.br</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"><br /></span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Equa\u00e7\u00e3o Universal de Darcy-Weisbach</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-inden"
                        "t:0; text-indent:0px;\"><img src=\":/TUTORIAL/icons AF/tutorial/EQ_darcy.png\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Regime de Escoamento e fator de atrito</sp"
                        "an></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/TUTORIAL/icons AF/tutorial/f laminar.png\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/TUTORIAL/icons AF/tutorial/escoamento turbulento.png\" /><img src=\":/TUTORIAL/icons AF/tutorial/reynold.png\" /><img src=\":/TUTORIAL/icons AF/tutorial/turbulento transitorio e turbulento rugoso.png\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -"
                        "qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/TUTORIAL/icons AF/tutorial/escoamento transtorio.png\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; "
                        "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/TUTORIAL/icons AF/tutorial/tabela criterio.png\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></"
                        "html>", None))
        self.txt_termo.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">CONTRATO E TERMO DE USO DE SOFTWARE </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">\u00a0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1. LICEN\u00c7A DE SOFTWARE </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0"
                        "px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">\u00a0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1.1. O Licenciante concede ao Usu\u00e1rio uma licen\u00e7a n\u00e3o exclusiva e intransfer\u00edvel para usar o software especificado abaixo, sujeito aos termos e condi\u00e7\u00f5es estabelecidos neste Contrato. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2. DIREITOS AUTORAIS E PROPRIEDADE INTELECTUAL \u00a0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2.1. O software, incluindo, mas n\u00e3o se limitando a, c\u00f3digos-fonte, interfaces gr\u00e1ficas, e toda a documenta\u00e7\u00e3o associada, \u00e9 protegido"
                        " por leis de direitos autorais e tratados internacionais de propriedade intelectual. \u00a0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2.2. O Usu\u00e1rio concorda em n\u00e3o copiar, modificar, redistribuir ou explorar comercialmente qualquer parte do software sem a autoriza\u00e7\u00e3o expressa por escrito do Licenciante. \u00a0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3. PROIBI\u00c7\u00c3O DE PIRATARIA E USO INADEQUADO \u00a0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3.1. O Usu\u00e1rio concorda em n\u00e3o participar de atividades de pirataria, engenharia reversa, descompila\u00e7\u00e3o, desmontagem ou qualquer outra forma "
                        "de viola\u00e7\u00e3o de propriedade intelectual relacionada ao software. \u00a0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3.2. O Usu\u00e1rio concorda em n\u00e3o usar o software para qualquer finalidade ilegal, fraudulenta ou que viole os direitos de terceiros. \u00a0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">4. ATUALIZA\u00c7\u00d5ES E SUPORTE \u00a0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">4.1. O Licenciante poder\u00e1 fornecer atualiza\u00e7\u00f5es peri\u00f3dicas do software, sujeitas a termos adicionais. \u00a0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-i"
                        "ndent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">4.2. O suporte t\u00e9cnico pode ser fornecido de acordo com as pol\u00edticas do Licenciante. \u00a0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">5. LIMITA\u00c7\u00c3O DE RESPONSABILIDADE \u00a0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">5.1. O software \u00e9 fornecido &quot;no estado em que se encontra&quot;, sem garantias de qualquer tipo, expressas ou impl\u00edcitas. \u00a0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">5.2. O Licenciante n\u00e3o ser\u00e1 respons\u00e1vel por quaisquer danos diretos, indiretos, incidentais, especiais, consequentes ou punitivos decorrentes"
                        " do uso ou impossibilidade de uso do software. \u00a0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">6. VIG\u00caNCIA E RESCIS\u00c3O \u00a0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">6.1. Este Contrato ter\u00e1 vig\u00eancia a partir da data de aceita\u00e7\u00e3o pelo Usu\u00e1rio at\u00e9 sua rescis\u00e3o. \u00a0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">6.2. O Licenciante reserva-se o direito de rescindir este Contrato se o Usu\u00e1rio violar seus termos. \u00a0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\""
                        ">7. LEI APLIC\u00c1VEL E JURISDI\u00c7\u00c3O \u00a0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">7.1. Este Contrato ser\u00e1 regido pelas leis da Rep\u00fablica Federativa do Brasil. \u00a0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">7.2. Qualquer disputa decorrente ou relacionada a este Contrato ser\u00e1 de compet\u00eancia exclusiva dos tribunais competentes no Brasil. </span></p></body></html>", None))
        self.LB_ativacao.setText(QCoreApplication.translate("MainWindow", u"Insira a Chave de Ativa\u00e7\u00e3o:", None))
        self.BT_ativacao.setText(QCoreApplication.translate("MainWindow", u"Ativar", None))
#if QT_CONFIG(tooltip)
        self.label_100.setToolTip(QCoreApplication.translate("MainWindow", u"Insira um nome para identificar o trecho", None))
#endif // QT_CONFIG(tooltip)
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Trecho", None))
#if QT_CONFIG(tooltip)
        self.label_101.setToolTip(QCoreApplication.translate("MainWindow", u"Especifique a origem do trecho, onde ele come\u00e7a.", None))
#endif // QT_CONFIG(tooltip)
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Origem de refer\u00eancia do Trecho", None))
        self.CB_Origem_2.setCurrentText("")
#if QT_CONFIG(tooltip)
        self.label_102.setToolTip(QCoreApplication.translate("MainWindow", u"Escolha o material da tubula\u00e7\u00e3o", None))
#endif // QT_CONFIG(tooltip)
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Material da tubula\u00e7\u00e3o", None))
        self.CB_Material.setCurrentText("")
#if QT_CONFIG(tooltip)
        self.label_103.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/TUTORIAL/icons AF/tutorial/ESQUEMA_CORTADO.png\", width=\"600\" height=\"500\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Altura  do trecho [m]", None))
        self.SP_Altura_Trecho.setSuffix("")
#if QT_CONFIG(tooltip)
        self.label_104.setToolTip(QCoreApplication.translate("MainWindow", u"Especifique o comprimento total do trecho em an\u00e1lise", None))
#endif // QT_CONFIG(tooltip)
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Comprimento Total do Trecho [m]", None))
        self.SP_Comprimento.setSuffix("")
#if QT_CONFIG(tooltip)
        self.label_132.setToolTip(QCoreApplication.translate("MainWindow", u"Press\u00e3o necess\u00e1ria no ponto de utiliza\u00e7\u00e3o da pe\u00e7a ou tubula\u00e7\u00e3o", None))
#endif // QT_CONFIG(tooltip)
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"Press\u00e3o necess\u00e1ria no trecho [mca]", None))
        self.SP_pressao_nec_trecho.setSuffix("")
        self.BT_avancar_trecho.setText(QCoreApplication.translate("MainWindow", u"Avan\u00e7ar", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Conex\u00f5es ", None))
        self.BT_recuar_conexaoPVC.setText(QCoreApplication.translate("MainWindow", u"Recuar", None))
        self.BT_avancar_conexaoPVC.setText(QCoreApplication.translate("MainWindow", u"Avan\u00e7ar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cotovelo de 90", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Cotovelo de 45", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Curva de 90", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Curva de 45", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"RG de gaveta", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"RG de press\u00e3o", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"RG de esfera", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"RG de angular", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TE sa\u00edda direta", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TE sa\u00edda perpendicular", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Entrada normal", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Entrada de borda", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Sa\u00edda de canaliza\u00e7\u00e3o", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"V\u00e1lvula de p\u00e9 e Crivo", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"V\u00e1lvula de reten\u00e7\u00e3o vertical", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"V\u00e1lvula de reten\u00e7\u00e3o horizontal", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Conex\u00f5es ", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Sa\u00edda e Entrada ", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"Entrada normal", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Entrada de borda", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"Sa\u00edda de canaliza\u00e7\u00e3o", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"V\u00e1lvula de p\u00e9 e Crivo", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Acess\u00f3rios", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"V\u00e1lvula de reten\u00e7\u00e3o vertical", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"V\u00e1lvula de reten\u00e7\u00e3o horizontal", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"Transposi\u00e7\u00e3o", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"Luvas", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"Uni\u00e3o Flange Oval", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"Redu\u00e7\u00e3o", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Registros", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"RG de gaveta", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"RG de press\u00e3o", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"RG de esfera", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"RG de angular", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"TE's", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"TE sa\u00edda direta", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"TE sa\u00edda perpendicular", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"TE Direto 45", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"TE Perpendicular 45", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"Cruzeta Perpendicular", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"TE Curva Sa\u00edda Dupla ", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"TE Curva Entrada Dupla ", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Curvas", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Cotovelo de 90", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Cotovelo de 45", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Curva de 90", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Curva de 45", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"Curva 90 Femea", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"Curva 90 Macho Femea", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"Curva 90 Macho", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"Cotovelo Sa\u00edda Lateral", None))
        self.BT_recuar_conexaoFERRO.setText(QCoreApplication.translate("MainWindow", u"Recuar", None))
        self.BT_avancar_conexaoFERRO.setText(QCoreApplication.translate("MainWindow", u"Avan\u00e7ar", None))
    # retranslateUi

