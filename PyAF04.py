from PySide6 import QtCore
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox,QLineEdit, QItemDelegate, QComboBox, QTableView, QFileDialog,QVBoxLayout)
from main_hid import Ui_MainWindow
import sys
import pandas as pd
import numpy as np
import math
import os

# criar ambiente virtual
# python -m venv nome_ambiente_virtual
# converte arquivo
# pyside6-uic main_hid.ui -o main_hid.py
# pyside6-rcc Icons-AF.qrc -o Icons_cr.py
# quando tem janela que interage precisa por o pyinstaller --onefile PyAF04.py -i icone_hid.ico  -w 

class DataFrameModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        super(DataFrameModel, self).__init__(parent)
        self._data = data
             
    def rowCount(self, parent):
        return len(self._data.index)

    def columnCount(self, parent):
        return len(self._data.columns)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
        
            return str(self._data.iat[index.row(), index.column()])
        
        return


    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            self._data.iat[index.row(), index.column()] = value

            if index.column() == 1:
                # Se a coluna 1 (combobox) for alterada, atualize a coluna 4
                self.data[index.row()][4] = self.get_value_for_row(self.data[index.row()][3])
                self.data[index.row()][3] = self.get_value_for_row(self.data[index.row()][2])
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index):
        editavel = [3,5,8,14]
        if index.column() in editavel:
            return super().flags(index) | QtCore.Qt.ItemIsEditable
        return super().flags(index)
    

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                # Retorna o nome da coluna como título
                return str(self._data.columns[section])
            elif orientation == QtCore.Qt.Vertical:
                # Retorna o número da linha como título
                return str(section + 1)
            

    def add_row(self, values):
        # Adiciona uma nova linha ao DataFrame usando concat
        new_row = pd.DataFrame([values], columns=self._data.columns)
        self._data = pd.concat([self._data, new_row], ignore_index=True)

        # Notifica a tabela sobre as mudanças
        self.layoutChanged.emit()

    def remove_row(self, row):
        self.beginRemoveRows(QtCore.QModelIndex(), row, row)
        self._data = self._data.drop(self._data.index[row])
        self.endRemoveRows()

class LineEditDelegate(QItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        return editor

class ComboBoxDelegate(QItemDelegate):
    def createEditor(self, parent, option, index):
       
        combo_box = QComboBox(parent)
        row_value = index.siblingAtColumn(2).data()
        label_visivel = MainWindow().LB_aviso_plan.setVisible(True)
        lista_dn = MainWindow().combobox_dn(row_value)
        combo_box.addItems(lista_dn)
        #combo_box.currentIndexChanged.connect(self.handle_combo_box_change)
        combo_box.currentIndexChanged.connect(label_visivel)
        return combo_box
    
    def setEditorData(self, editor, index):
        editor.setCurrentText(index.data())

    def setModelData(self, editor, model, index):
        model.setData(index, editor.currentText(), QtCore.Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

    #def handle_combo_box_change(self, index):
        #editor = self.sender()
        #if editor is not None:
            #tableview = self.parent()
            #model = tableview.model()
            #current_index = tableview.currentIndex()
            #next_index = model.index(current_index.row(), current_index.column() + 1)
            #if next_index.isValid():
                #model.setData(next_index, editor.currentText(), QtCore.Qt.EditRole)


class ComboBoxDelegate_origem(QItemDelegate):
    def createEditor(self, parent, option, index):
       
        combo_box = QComboBox(parent)
        row_value = index.siblingAtColumn(2).data()
        lista_dn = MainWindow().combobox_tabview_origem_lista()
        combo_box.addItems(lista_dn)
        combo_box.currentIndexChanged.connect(self.handle_combo_box_change)
        return combo_box
    
    def setEditorData(self, editor, index):
        editor.setCurrentText(index.data())

    def setModelData(self, editor, model, index):
        model.setData(index, editor.currentText(), QtCore.Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

    def handle_combo_box_change(self, index):
        editor = self.sender()
        if editor is not None:
            tableview = self.parent()
            model = tableview.model()
            current_index = tableview.currentIndex()
            next_index = model.index(current_index.row(), current_index.column() + 1)
            if next_index.isValid():
                model.setData(next_index, editor.currentText(), QtCore.Qt.EditRole)    

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
       
        self.setupUi(self)
        self.setWindowTitle("Sistema de Hidráulica")
        appIcon = QIcon(u":/ICO/icons AF/icone_hid.png")
    
        self.setWindowIcon(appIcon)


        # VERIFICAÇÃO DE ACESSO POR CHAVE
        # 
        # lista de restrição 
        self.df_restrito = pd.Series()
        
        # database de chaves 
        self.data_chave = pd.read_csv("sis_eng")       
        self.data_chave = self.data_chave['Chave'].apply(self.descriptografar)
       
        print('descriptografado:',self.data_chave)
    

        #formatacao Qline Edit
        
        
        if self.carrega_chave_txt() != '':
            carrega_chave_txt = str(self.carrega_chave_txt())
            self.TX_ativacao.setText(carrega_chave_txt)

        self.TX_ativacao.setStyleSheet("background-color: grey21;")
        self.TX_ativacao.setReadOnly(False)

        # chama a função para que não seja necessário clicar sempre no botão verficiar
        self.gate_acesso()
        self.BT_ativacao.clicked.connect(self.gate_acesso) 


        # DATAFRAME DE PESQUISA 
        self.df_PVC = pd.read_excel(r"T:\MEUS CODIGOS\venv\tabs\Tabela_Diametro_Equivalente.xlsx", sheet_name="TABELA_PVC")

        self.df_FERRO = pd.read_excel(r"T:\MEUS CODIGOS\venv\tabs\Tabela_Diametro_Equivalente.xlsx", sheet_name="TABELA_FERRO")

        #dataframe conexões
        self.df_pvc = pd.DataFrame(columns=['Conexão', 'Qtda'])
        self.df3_ferro = pd.DataFrame(columns=['Conexão', 'Qtda'])

        # dataframe total equivalente
        self.df_comp_eq_fe = pd.DataFrame(columns =[])
        self.df_comp_eq_pvc = pd.DataFrame(columns =[])


        # DATAFRAME PRINCIPAL____________________________________________________________________
        self.df = pd.DataFrame(columns=['Trecho', 'Origem', 'Mat', 'DN[mm]','Di[mm]', 'L[m]', 'L eq[m]', 'L tot[m]', 'h[m]', 'V[m/s]', 'Q[L/s]','Dh[mca]', 'P disp[mca]', 'temp[°C]', 'P nec[mca]','P res[mca]','P result[mca]'])

        # arrumar velociddae na tabela daddlinha está dando nan
    
        self.df_pressurizadora = pd.DataFrame(columns=['Vazão max[m³/h]', 'Pressão manométrica[mca]','h reservatório[m]'])


        layout = QVBoxLayout(self.FR_container_planilha)
        self.tableview = QTableView()
        self.tableview.setGeometry(50,50,900,400)
       
        self._locked_columns = [1,2,4,6,8,10,12,13,15,16] 
        self.LB_aviso_plan.setVisible(False)

        layout.addWidget(self.tableview)

        self.setLayout(layout)
        self.tableview.resizeColumnsToContents()

        self.sinal_atualizar_dataframe =  QtCore.Signal(DataFrameModel(self.df))
  
        #############################
        #Toggle Button
        self.BT_Toggle.clicked.connect(self.LeftMenu)
        #############################

        # trava a vazão editável
        self.SP_Vazao_Trecho.setEnabled(False)
        self.SP_vazao_max.setEnabled(False)
      
        
        # widgets da pagina trecho
        self.combobox_origem()
        self.combobox_material()
        
        
        self.CB_Material.currentTextChanged.connect(self.Material_selecionado)
        

        
        #BOTÕES INFO 
        self.BT_ajuda.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Page_ajuda))
        self.BT_termo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Page_termos))
        self.BT_info.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Page_info))
        self.BT_metodologia.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Page_metodologia))
        self.BT_chave.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Page_ativacao))

       


        self.txt_ajuda.setReadOnly(True)
        self.txt_termo.setReadOnly(True)
        self.txt_info.setReadOnly(True)
        self.textEdit.setReadOnly(True) # metodologia

        #buttons para funcionamento do sistema ###################################     
        
        self.BT_Planilha.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Page_Planilha) )
        self.BT_Trecho.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Page_Trecho))
        self.BT_Vazao.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Page_Vazao))

        self.BT_Relatorio.clicked.connect(self.save_to_excel)

        #pagina de conexões ferro
        self.BT_recuar_conexaoFERRO.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Page_Trecho))
        self.BT_avancar_conexaoFERRO.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Page_Vazao))
        
        #pagina de conexões pvc
        self.BT_recuar_conexaoPVC.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Page_Trecho))

        self.BT_avancar_conexaoPVC.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Page_Vazao))

        #pagina de vazao
        self.BT_recuar_Vazao.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Page_Trecho))
        # estudar se precisa disso 

        # BOTÃO QUE ADICIONA LINHA DE TRECHO E CALCULA 

        self.BT_Inserir.clicked.connect(self.add_linha)
 
      
        # BOTÕES TABELA DE PRESSÃO 
        self.BT_excluir.clicked.connect(self.remove_selected_rows)
        self.BT_calcular.clicked.connect(self.calcular_dataframe)
        self.BT_salvar.clicked.connect(self.save_dataframe)
        self.BT_carregar.clicked.connect(self.load_dataframe)

        
        # configuração do slider de temperatura
        self.Slider_Temperatura.setMinimum(0)
        self.Slider_Temperatura.setMaximum(100)
        self.Slider_Temperatura.setSingleStep(10)
        self.Slider_Temperatura.setTickInterval(10)
        self.Slider_Temperatura.setSliderPosition(20)
        self.Slider_Temperatura.moveEvent(self.Slider_Temperatura.setTickInterval(10))
        self.Slider_Temperatura.valueChanged.connect(self.Slider_Valor)
        self.LB_Temperatura.setText(f'{20} °C')
        
        #configuração da check box para definir qual será a vazão 
        self.CK_INSERIR_VAZAO.stateChanged.connect(self.CheckBox_Vazao)
        self.CheckBox_Vazao(1)


    def Slider_Valor(self):
        Temperatura_agua = self.Slider_Temperatura.value()

        if Temperatura_agua < 5:
            Temperatura_agua = 0
            self.Slider_Temperatura.setSliderPosition(0)

        if Temperatura_agua >= 5 and Temperatura_agua < 15:
            Temperatura_agua = 10
            self.Slider_Temperatura.setSliderPosition(10)

        if Temperatura_agua >= 15 and Temperatura_agua < 25:
            Temperatura_agua = 20
            self.Slider_Temperatura.setSliderPosition(20)

        if Temperatura_agua >= 25 and Temperatura_agua < 35:
            Temperatura_agua = 30
            self.Slider_Temperatura.setSliderPosition(30)
        
        if Temperatura_agua >= 35 and Temperatura_agua < 45:
            Temperatura_agua = 40
            self.Slider_Temperatura.setSliderPosition(40)
        
        if Temperatura_agua >= 45 and Temperatura_agua < 55:
            Temperatura_agua = 50
            self.Slider_Temperatura.setSliderPosition(50)
        
        if Temperatura_agua >= 55 and Temperatura_agua < 65:
            Temperatura_agua = 60
            self.Slider_Temperatura.setSliderPosition(60)
        
        if Temperatura_agua >= 65 and Temperatura_agua < 75:
            Temperatura_agua = 70
            self.Slider_Temperatura.setSliderPosition(70)
        
        if Temperatura_agua >= 75 and Temperatura_agua < 85:
            Temperatura_agua = 80
            self.Slider_Temperatura.setSliderPosition(80)
        
        if Temperatura_agua >= 85 and Temperatura_agua < 95:
            Temperatura_agua = 90
            self.Slider_Temperatura.setSliderPosition(90)
        
        if Temperatura_agua >= 95 and Temperatura_agua <= 100:
            Temperatura_agua = 100
            self.Slider_Temperatura.setSliderPosition(100)

        if Temperatura_agua >= 36:
            self.LB_Temperatura.setStyleSheet('color: red')
        else:
            self.LB_Temperatura.setStyleSheet('color: blue')


        self.LB_Temperatura.setText(f'{Temperatura_agua} °C')
        print(f'temperatura da água: {Temperatura_agua}')
        return (Temperatura_agua)    

    def CheckBox_Vazao(self,state):
       # tentar mudar esse para um botão de alternância
        if state == 2:
           
            self.SP_Vazao_Trecho.setEnabled(True)
        else:
            self.SP_Vazao_Trecho.setEnabled(False)

        return (state)
       
    def Material_selecionado(self):

        Material = self.CB_Material.currentText()
        print(f'material selecionado: {Material}')
        self.limpar_conexões()

        if Material == "PVC" or Material == "Cobre" or Material == "Latão" or Material == "Vidro":

            # avançar trecho
            self.BT_avancar_trecho.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Page_conexao_PVC))
            # copiar recuar vazao aqui
            self.BT_recuar_Vazao.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Page_conexao_PVC))

            #botão conexões principal 
            self.BT_Conexao.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Page_conexao_PVC))
            # combobox DN
            df = self.df_PVC
           
            self.diametro_nominal = df['Diametro_Nominal'].astype(str)
            self.diametro_nominal = self.diametro_nominal.tolist()
            
            print('diametro_nominal:',self.diametro_nominal)
            #self.CB_dn.addItems(self.diametro_nominal)

            self.CB_Material.setStyleSheet('background-color: white;')

        else:

            if Material =="Selecione o material":
                # se não escolher material
                self.BT_avancar_trecho.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Page_Trecho))
                # copiar recuar vazao aqui
                self.BT_recuar_Vazao.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Page_Trecho))
                #botão conexões principal 
                self.BT_Conexao.clicked.disconnect(lambda: self.stackedWidget.setCurrentWidget(self.Page_conexao_FERRO))
                self.BT_Conexao.clicked.disconnect(lambda: self.stackedWidget.setCurrentWidget(self.Page_conexao_PVC))
                


            else:
                # se não avançar
                self.BT_avancar_trecho.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Page_conexao_FERRO))
                # copiar recuar vazao aqui
                self.BT_recuar_Vazao.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Page_conexao_FERRO))

                self.BT_Conexao.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Page_conexao_FERRO))

                # combobox DN
                df = self.df_FERRO
               
                self.diametro_nominal = df['Diametro_Nominal'].astype(str)
                self.diametro_nominal = self.diametro_nominal.tolist()
                self.diametro_nominal = [valor for valor in self.diametro_nominal if valor != '0']
                print('diametro_nominal:',self.diametro_nominal)
                #self.CB_dn.addItems(diametro_nominal)
                

                self.CB_Material.setStyleSheet('background-color: white;')


        print('MATERIAL SELECIONADO OK:', Material)

        return(Material)

# comprimentos equivalentes 
    def Comprimento_tabview_PVC(self):

        # isso é para PVC vai usar esses valores 
        #df = pd.read_excel(r"T:\MEUS CODIGOS\venv\tabs\Tabela_Diametro_Equivalente.xlsx", sheet_name="TABELA_PVC")

        df = self.df_PVC

        # calculo comprimento equivalente 
        Cotovelo_90Q = self.SP_COT90.value()	
        Cotovelo_45Q = self.SP_COT45.value()
        Curva_90Q = self.SP_CURV90.value()
        Curva_45Q = self.SP_CURV45.value()	
        TE_DiretoQ = self.SP_TDIR.value()
        T_PerpendicularQ = self.SP_TLAT.value()	
        Valvula_PEQ = self.SP_VALV_PE.value()	
        Valvula_Retencao_HorizontalQ = self.SP_VALV_H.value()
        Valvula_Retencao_VerticalQ = self.SP_VALV_V.value()	
        RG_EsferaQ = self.spinBox_3.value()	
        RG_GavetaQ = self.SP_RG_GAV.value()	
        RG_PressaoQ = self.SP_RG_RP.value()	
        RG_AngularQ = self.SP_RG_ANG.value()
        Entrada_NormalQ = self.SP_ENTRADA_N.value()	
        Entrada_BordaQ = self.SP_ENTRADA_B.value()
        Saida_CanalizacaoQ = self.SP_ENTRADA_SC.value()

  
        dn_15_Cotovelo_90 = float(df['Cotovelo_90'][0]) * Cotovelo_90Q
        dn_15_Cotovelo_45 = float(df['Cotovelo_45'][0]) * Cotovelo_45Q
        dn_15_Curva_90 = float(df['Curva_90'][0]) * Curva_90Q
        dn_15_Curva_45 = float(df['Curva_45'][0]) * Curva_45Q
        dn_15_TE_Direto = float(df['TE_Direto'][0]) * TE_DiretoQ
        dn_15_T_Perpendicular = float(df['T_Perpendicular'][0]) * T_PerpendicularQ
        dn_15_Valvula_PE = float(df['Valvula_PE'][0]) * Valvula_PEQ
        dn_15_Valvula_Retencao_Horizontal = float(df['Valvula_Retencao_Horizontal'][0]) * Valvula_PEQ*Valvula_Retencao_HorizontalQ
        dn_15_Valvula_Retencao_Vertical = float(df['Valvula_Retencao_Vertical'][0]) *Valvula_Retencao_VerticalQ
        dn_15_RG_Esfera = float(df['RG_Esfera'][0]) *RG_EsferaQ
        dn_15_RG_Gaveta = float(df['RG_Gaveta'][0]) *RG_GavetaQ
        dn_15_RG_Pressao = float(df['RG_Pressao'][0]) *RG_PressaoQ
        dn_15_RG_Angular = float(df['RG_Angular'][0]) *RG_AngularQ
        dn_15_Entrada_Normal = float(df['RG_Angular'][0]) *Entrada_NormalQ
        dn_15_Entrada_Borda = float(df['Entrada_Borda'][0]) *Entrada_BordaQ
        dn_15_Saida_Canalizacao = float(df['Saida_Canalizacao'][0]) *Saida_CanalizacaoQ


        equi_15 = {
                    'Conexão':[dn_15_Cotovelo_90,	
                            dn_15_Cotovelo_45,	
                            dn_15_Curva_90,	
                            dn_15_Curva_45,	
                            dn_15_TE_Direto,	
                            dn_15_T_Perpendicular,
                            dn_15_Valvula_PE,	
                            dn_15_Valvula_Retencao_Horizontal,	
                            dn_15_Valvula_Retencao_Vertical,	
                            dn_15_RG_Esfera,	
                            dn_15_RG_Gaveta,	
                            dn_15_RG_Pressao,	
                            dn_15_RG_Angular,	
                            dn_15_Entrada_Normal,	
                            dn_15_Entrada_Borda,	
                            dn_15_Saida_Canalizacao,
                            ]
        }

        df_15= pd.DataFrame(equi_15)
        SR_15 = pd.Series(df_15['Conexão'])    
        EQ_15 = SR_15.sum()


        dn_20_Cotovelo_90 = float(df['Cotovelo_90'][1]) * Cotovelo_90Q
        dn_20_Cotovelo_45 = float(df['Cotovelo_45'][1]) * Cotovelo_45Q
        dn_20_Curva_90 = float(df['Curva_90'][1]) * Curva_90Q
        dn_20_Curva_45 = float(df['Curva_45'][1]) * Curva_45Q
        dn_20_TE_Direto = float(df['TE_Direto'][1]) * TE_DiretoQ
        dn_20_T_Perpendicular = float(df['T_Perpendicular'][1]) * T_PerpendicularQ
        dn_20_Valvula_PE = float(df['Valvula_PE'][1]) * Valvula_PEQ
        dn_20_Valvula_Retencao_Horizontal = float(df['Valvula_Retencao_Horizontal'][1]) * Valvula_PEQ*Valvula_Retencao_HorizontalQ
        dn_20_Valvula_Retencao_Vertical = float(df['Valvula_Retencao_Vertical'][1]) *Valvula_Retencao_VerticalQ
        dn_20_RG_Esfera = float(df['RG_Esfera'][1]) *RG_EsferaQ
        dn_20_RG_Gaveta = float(df['RG_Gaveta'][1]) *RG_GavetaQ
        dn_20_RG_Pressao = float(df['RG_Pressao'][1]) *RG_PressaoQ
        dn_20_RG_Angular = float(df['RG_Angular'][1]) *RG_AngularQ
        dn_20_Entrada_Normal = float(df['RG_Angular'][1]) *Entrada_NormalQ
        dn_20_Entrada_Borda = float(df['Entrada_Borda'][1]) *Entrada_BordaQ
        dn_20_Saida_Canalizacao = float(df['Saida_Canalizacao'][1]) *Saida_CanalizacaoQ

        equi_20 = {
                    'Conexão':[dn_20_Cotovelo_90,	
                            dn_20_Cotovelo_45,	
                            dn_20_Curva_90,	
                            dn_20_Curva_45,	
                            dn_20_TE_Direto,	
                            dn_20_T_Perpendicular,
                            dn_20_Valvula_PE,	
                            dn_20_Valvula_Retencao_Horizontal,	
                            dn_20_Valvula_Retencao_Vertical,	
                            dn_20_RG_Esfera,	
                            dn_20_RG_Gaveta,	
                            dn_20_RG_Pressao,	
                            dn_20_RG_Angular,	
                            dn_20_Entrada_Normal,	
                            dn_20_Entrada_Borda,	
                            dn_20_Saida_Canalizacao,
                            ]
        }

        df_20= pd.DataFrame(equi_20)
        SR_20= pd.Series(df_20['Conexão'])    
        EQ_20 = SR_20.sum()


        dn_25_Cotovelo_90 = float(df['Cotovelo_90'][2]) * Cotovelo_90Q
        dn_25_Cotovelo_45 = float(df['Cotovelo_45'][2]) * Cotovelo_45Q
        dn_25_Curva_90 = float(df['Curva_90'][2]) * Curva_90Q
        dn_25_Curva_45 = float(df['Curva_45'][2]) * Curva_45Q
        dn_25_TE_Direto = float(df['TE_Direto'][2]) * TE_DiretoQ
        dn_25_T_Perpendicular = float(df['T_Perpendicular'][2]) * T_PerpendicularQ
        dn_25_Valvula_PE = float(df['Valvula_PE'][2]) * Valvula_PEQ
        dn_25_Valvula_Retencao_Horizontal = float(df['Valvula_Retencao_Horizontal'][2]) * Valvula_PEQ*Valvula_Retencao_HorizontalQ
        dn_25_Valvula_Retencao_Vertical = float(df['Valvula_Retencao_Vertical'][2]) *Valvula_Retencao_VerticalQ
        dn_25_RG_Esfera = float(df['RG_Esfera'][2]) *RG_EsferaQ
        dn_25_RG_Gaveta = float(df['RG_Gaveta'][2]) *RG_GavetaQ
        dn_25_RG_Pressao = float(df['RG_Pressao'][2]) *RG_PressaoQ
        dn_25_RG_Angular = float(df['RG_Angular'][2]) *RG_AngularQ
        dn_25_Entrada_Normal = float(df['RG_Angular'][2]) *Entrada_NormalQ
        dn_25_Entrada_Borda = float(df['Entrada_Borda'][2]) *Entrada_BordaQ
        dn_25_Saida_Canalizacao = float(df['Saida_Canalizacao'][2]) *Saida_CanalizacaoQ


        equi_25 = {
                    'Conexão':[dn_25_Cotovelo_90,	
                            dn_25_Cotovelo_45,	
                            dn_25_Curva_90,	
                            dn_25_Curva_45,	
                            dn_25_TE_Direto,	
                            dn_25_T_Perpendicular,
                            dn_25_Valvula_PE,	
                            dn_25_Valvula_Retencao_Horizontal,	
                            dn_25_Valvula_Retencao_Vertical,	
                            dn_25_RG_Esfera,	
                            dn_25_RG_Gaveta,	
                            dn_25_RG_Pressao,	
                            dn_25_RG_Angular,	
                            dn_25_Entrada_Normal,	
                            dn_25_Entrada_Borda,	
                            dn_25_Saida_Canalizacao,
                            ]
        }

        df_25= pd.DataFrame(equi_25)
        SR_25 = pd.Series(df_25['Conexão']) 
        EQ_25 = SR_25.sum()


        dn_32_Cotovelo_90 = float(df['Cotovelo_90'][3]) * Cotovelo_90Q
        dn_32_Cotovelo_45 = float(df['Cotovelo_45'][3]) * Cotovelo_45Q
        dn_32_Curva_90 = float(df['Curva_90'][3]) * Curva_90Q
        dn_32_Curva_45 = float(df['Curva_45'][3]) * Curva_45Q
        dn_32_TE_Direto = float(df['TE_Direto'][3]) * TE_DiretoQ
        dn_32_T_Perpendicular = float(df['T_Perpendicular'][3]) * T_PerpendicularQ
        dn_32_Valvula_PE = float(df['Valvula_PE'][3]) * Valvula_PEQ
        dn_32_Valvula_Retencao_Horizontal = float(df['Valvula_Retencao_Horizontal'][3]) * Valvula_PEQ*Valvula_Retencao_HorizontalQ
        dn_32_Valvula_Retencao_Vertical = float(df['Valvula_Retencao_Vertical'][3]) *Valvula_Retencao_VerticalQ
        dn_32_RG_Esfera = float(df['RG_Esfera'][3]) *RG_EsferaQ
        dn_32_RG_Gaveta = float(df['RG_Gaveta'][3]) *RG_GavetaQ
        dn_32_RG_Pressao = float(df['RG_Pressao'][3]) *RG_PressaoQ
        dn_32_RG_Angular = float(df['RG_Angular'][3]) *RG_AngularQ
        dn_32_Entrada_Normal = float(df['RG_Angular'][3]) *Entrada_NormalQ
        dn_32_Entrada_Borda = float(df['Entrada_Borda'][3]) *Entrada_BordaQ
        dn_32_Saida_Canalizacao = float(df['Saida_Canalizacao'][3]) *Saida_CanalizacaoQ


        equi_32 = {
                    'Conexão':[dn_32_Cotovelo_90,	
                            dn_32_Cotovelo_45,	
                            dn_32_Curva_90,	
                            dn_32_Curva_45,	
                            dn_32_TE_Direto,	
                            dn_32_T_Perpendicular,
                            dn_32_Valvula_PE,	
                            dn_32_Valvula_Retencao_Horizontal,	
                            dn_32_Valvula_Retencao_Vertical,	
                            dn_32_RG_Esfera,	
                            dn_32_RG_Gaveta,	
                            dn_32_RG_Pressao,	
                            dn_32_RG_Angular,	
                            dn_32_Entrada_Normal,	
                            dn_32_Entrada_Borda,	
                            dn_32_Saida_Canalizacao,
                            ]
        }

        df_32= pd.DataFrame(equi_32)
        SR_32 = pd.Series(df_32['Conexão'])
        EQ_32 = SR_32.sum()


        dn_40_Cotovelo_90 = float(df['Cotovelo_90'][4]) * Cotovelo_90Q
        dn_40_Cotovelo_45 = float(df['Cotovelo_45'][4]) * Cotovelo_45Q
        dn_40_Curva_90 = float(df['Curva_90'][4]) * Curva_90Q
        dn_40_Curva_45 = float(df['Curva_45'][4]) * Curva_45Q
        dn_40_TE_Direto = float(df['TE_Direto'][4]) * TE_DiretoQ
        dn_40_T_Perpendicular = float(df['T_Perpendicular'][4]) * T_PerpendicularQ
        dn_40_Valvula_PE = float(df['Valvula_PE'][4]) * Valvula_PEQ
        dn_40_Valvula_Retencao_Horizontal = float(df['Valvula_Retencao_Horizontal'][4]) * Valvula_PEQ*Valvula_Retencao_HorizontalQ
        dn_40_Valvula_Retencao_Vertical = float(df['Valvula_Retencao_Vertical'][4]) *Valvula_Retencao_VerticalQ
        dn_40_RG_Esfera = float(df['RG_Esfera'][4]) *RG_EsferaQ
        dn_40_RG_Gaveta = float(df['RG_Gaveta'][4]) *RG_GavetaQ
        dn_40_RG_Pressao = float(df['RG_Pressao'][4]) *RG_PressaoQ
        dn_40_RG_Angular = float(df['RG_Angular'][4]) *RG_AngularQ
        dn_40_Entrada_Normal = float(df['RG_Angular'][4]) *Entrada_NormalQ
        dn_40_Entrada_Borda = float(df['Entrada_Borda'][4]) *Entrada_BordaQ
        dn_40_Saida_Canalizacao = float(df['Saida_Canalizacao'][4]) *Saida_CanalizacaoQ
    

        equi_40 = {
                    'Conexão':[dn_40_Cotovelo_90,	
                            dn_40_Cotovelo_45,	
                            dn_40_Curva_90,	
                            dn_40_Curva_45,	
                            dn_40_TE_Direto,	
                            dn_40_T_Perpendicular,
                            dn_40_Valvula_PE,	
                            dn_40_Valvula_Retencao_Horizontal,	
                            dn_40_Valvula_Retencao_Vertical,	
                            dn_40_RG_Esfera,	
                            dn_40_RG_Gaveta,	
                            dn_40_RG_Pressao,	
                            dn_40_RG_Angular,	
                            dn_40_Entrada_Normal,	
                            dn_40_Entrada_Borda,	
                            dn_40_Saida_Canalizacao,
                            ]
        }

        df_40= pd.DataFrame(equi_40)
        SR_40 = pd.Series(df_40['Conexão'])
        EQ_40 = SR_40.sum()


        dn_50_Cotovelo_90 = float(df['Cotovelo_90'][5]) * Cotovelo_90Q
        dn_50_Cotovelo_45 = float(df['Cotovelo_45'][5]) * Cotovelo_45Q
        dn_50_Curva_90 = float(df['Curva_90'][5]) * Curva_90Q
        dn_50_Curva_45 = float(df['Curva_45'][5]) * Curva_45Q
        dn_50_TE_Direto = float(df['TE_Direto'][5]) * TE_DiretoQ
        dn_50_T_Perpendicular = float(df['T_Perpendicular'][5]) * T_PerpendicularQ
        dn_50_Valvula_PE = float(df['Valvula_PE'][5]) * Valvula_PEQ
        dn_50_Valvula_Retencao_Vertical = float(df['Valvula_Retencao_Vertical'][5]) *Valvula_Retencao_VerticalQ
        dn_50_Valvula_Retencao_Horizontal = float(df['Valvula_Retencao_Horizontal'][5]) * Valvula_PEQ*Valvula_Retencao_HorizontalQ
        dn_50_RG_Esfera = float(df['RG_Esfera'][5]) *RG_EsferaQ
        dn_50_RG_Gaveta = float(df['RG_Gaveta'][5]) *RG_GavetaQ
        dn_50_RG_Pressao = float(df['RG_Pressao'][5]) *RG_PressaoQ
        dn_50_RG_Angular = float(df['RG_Angular'][5]) *RG_AngularQ
        dn_50_Entrada_Normal = float(df['RG_Angular'][5]) *Entrada_NormalQ
        dn_50_Entrada_Borda = float(df['Entrada_Borda'][5]) *Entrada_BordaQ
        dn_50_Saida_Canalizacao = float(df['Saida_Canalizacao'][5]) *Saida_CanalizacaoQ

        equi_50 = {
                    'Conexão':[dn_50_Cotovelo_90,	
                            dn_50_Cotovelo_45,	
                            dn_50_Curva_90,	
                            dn_50_Curva_45,	
                            dn_50_TE_Direto,	
                            dn_50_T_Perpendicular,
                            dn_50_Valvula_PE,	
                            dn_50_Valvula_Retencao_Horizontal,	
                            dn_50_Valvula_Retencao_Vertical,	
                            dn_50_RG_Esfera,	
                            dn_50_RG_Gaveta,	
                            dn_50_RG_Pressao,	
                            dn_50_RG_Angular,	
                            dn_50_Entrada_Normal,	
                            dn_50_Entrada_Borda,	
                            dn_50_Saida_Canalizacao,
                            ]
        }

        df_50= pd.DataFrame(equi_50)
        SR_50= pd.Series(df_50['Conexão'])
        EQ_50 = SR_50.sum()

        dn_65_Cotovelo_90 = float(df['Cotovelo_90'][6]) * Cotovelo_90Q
        dn_65_Cotovelo_45 = float(df['Cotovelo_45'][6]) * Cotovelo_45Q
        dn_65_Curva_90 = float(df['Curva_90'][6]) * Curva_90Q
        dn_65_Curva_45 = float(df['Curva_45'][6]) * Curva_45Q
        dn_65_TE_Direto = float(df['TE_Direto'][6]) * TE_DiretoQ
        dn_65_T_Perpendicular = float(df['T_Perpendicular'][6]) * T_PerpendicularQ
        dn_65_Valvula_PE = float(df['Valvula_PE'][6]) * Valvula_PEQ
        dn_65_Valvula_Retencao_Horizontal = float(df['Valvula_Retencao_Horizontal'][6]) * Valvula_PEQ*Valvula_Retencao_HorizontalQ
        dn_65_Valvula_Retencao_Vertical = float(df['Valvula_Retencao_Vertical'][6]) *Valvula_Retencao_VerticalQ
        dn_65_RG_Esfera = float(df['RG_Esfera'][6]) *RG_EsferaQ
        dn_65_RG_Gaveta = float(df['RG_Gaveta'][6]) *RG_GavetaQ
        dn_65_RG_Pressao = float(df['RG_Pressao'][6]) *RG_PressaoQ
        dn_65_RG_Angular = float(df['RG_Angular'][6]) *RG_AngularQ
        dn_65_Entrada_Normal = float(df['RG_Angular'][6]) *Entrada_NormalQ
        dn_65_Entrada_Borda = float(df['Entrada_Borda'][6]) *Entrada_BordaQ
        dn_65_Saida_Canalizacao = float(df['Saida_Canalizacao'][6]) *Saida_CanalizacaoQ



        equi_65 = {
            'Conexão':[dn_65_Cotovelo_90,	
                    dn_65_Cotovelo_45,	
                    dn_65_Curva_90,	
                    dn_65_Curva_45,	
                    dn_65_TE_Direto,	
                    dn_65_T_Perpendicular,
                    dn_65_Valvula_PE,	
                    dn_65_Valvula_Retencao_Horizontal,	
                    dn_65_Valvula_Retencao_Vertical,	
                    dn_65_RG_Esfera,	
                    dn_65_RG_Gaveta,	
                    dn_65_RG_Pressao,	
                    dn_65_RG_Angular,	
                    dn_65_Entrada_Normal,	
                    dn_65_Entrada_Borda,	
                    dn_65_Saida_Canalizacao,
                    ]
                }

        df_65= pd.DataFrame(equi_65)
        SR_65 = pd.Series(df_65['Conexão'])     
        EQ_65 = SR_65.sum()


        dn_80_Cotovelo_90 = float(df['Cotovelo_90'][7]) * Cotovelo_90Q
        dn_80_Cotovelo_45 = float(df['Cotovelo_45'][7]) * Cotovelo_45Q
        dn_80_Curva_90 = float(df['Curva_90'][7]) * Curva_90Q
        dn_80_Curva_45 = float(df['Curva_45'][7]) * Curva_45Q
        dn_80_TE_Direto = float(df['TE_Direto'][7]) * TE_DiretoQ
        dn_80_T_Perpendicular = float(df['T_Perpendicular'][7]) * T_PerpendicularQ
        dn_80_Valvula_PE = float(df['Valvula_PE'][7]) * Valvula_PEQ
        dn_80_Valvula_Retencao_Horizontal = float(df['Valvula_Retencao_Horizontal'][7]) * Valvula_PEQ*Valvula_Retencao_HorizontalQ
        dn_80_Valvula_Retencao_Vertical = float(df['Valvula_Retencao_Vertical'][7]) *Valvula_Retencao_VerticalQ
        dn_80_RG_Esfera = float(df['RG_Esfera'][7]) *RG_EsferaQ
        dn_80_RG_Gaveta = float(df['RG_Gaveta'][7]) *RG_GavetaQ
        dn_80_RG_Pressao = float(df['RG_Pressao'][7]) *RG_PressaoQ
        dn_80_RG_Angular = float(df['RG_Angular'][7]) *RG_AngularQ
        dn_80_Entrada_Normal = float(df['RG_Angular'][7]) *Entrada_NormalQ
        dn_80_Entrada_Borda = float(df['Entrada_Borda'][7]) *Entrada_BordaQ
        dn_80_Saida_Canalizacao = float(df['Saida_Canalizacao'][7]) *Saida_CanalizacaoQ


        equi_80 = {
            'Conexão':[dn_80_Cotovelo_90,	
                    dn_80_Cotovelo_45,	
                    dn_80_Curva_90,	
                    dn_80_Curva_45,	
                    dn_80_TE_Direto,	
                    dn_80_T_Perpendicular,
                    dn_80_Valvula_PE,	
                    dn_80_Valvula_Retencao_Horizontal,	
                    dn_80_Valvula_Retencao_Vertical,	
                    dn_80_RG_Esfera,	
                    dn_80_RG_Gaveta,	
                    dn_80_RG_Pressao,	
                    dn_80_RG_Angular,	
                    dn_80_Entrada_Normal,	
                    dn_80_Entrada_Borda,	
                    dn_80_Saida_Canalizacao,
                    ]
                }

        df_80= pd.DataFrame(equi_80)
        SR_80 = pd.Series(df_80['Conexão'])
        EQ_80 = SR_80.sum()


        dn_110_Cotovelo_90 = float(df['Cotovelo_90'][8]) * Cotovelo_90Q
        dn_110_Cotovelo_45 = float(df['Cotovelo_45'][8]) * Cotovelo_45Q
        dn_110_Curva_90 = float(df['Curva_90'][8]) * Curva_90Q
        dn_110_Curva_45 = float(df['Curva_45'][8]) * Curva_45Q
        dn_110_TE_Direto = float(df['TE_Direto'][8]) *TE_DiretoQ 
        dn_110_T_Perpendicular = float(df['T_Perpendicular'][8]) * T_PerpendicularQ
        dn_110_Valvula_PE = float(df['Valvula_PE'][8])* Valvula_PEQ
        dn_110_Valvula_Retencao_Horizontal = float(df['Valvula_Retencao_Horizontal'][8])* Valvula_PEQ*Valvula_Retencao_HorizontalQ
        dn_110_Valvula_Retencao_Vertical = float(df['Valvula_Retencao_Vertical'][8])*Valvula_Retencao_VerticalQ
        dn_110_RG_Esfera = float(df['RG_Esfera'][8])*RG_EsferaQ
        dn_110_RG_Gaveta = float(df['RG_Gaveta'][8])*RG_GavetaQ
        dn_110_RG_Pressao = float(df['RG_Pressao'][8])*RG_PressaoQ
        dn_110_RG_Angular = float(df['RG_Angular'][8])*RG_AngularQ 
        dn_110_Entrada_Normal = float(df['RG_Angular'][8]) *Entrada_NormalQ
        dn_110_Entrada_Borda = float(df['Entrada_Borda'][8]) *Entrada_BordaQ
        dn_110_Saida_Canalizacao = float(df['Saida_Canalizacao'][8]) *Saida_CanalizacaoQ


        equi_110 = {
            'Conexão':[dn_110_Cotovelo_90,	
                    dn_110_Cotovelo_45,	
                    dn_110_Curva_90,	
                    dn_110_Curva_45,	
                    dn_110_TE_Direto,	
                    dn_110_T_Perpendicular,
                    dn_110_Valvula_PE,	
                    dn_110_Valvula_Retencao_Horizontal,	
                    dn_110_Valvula_Retencao_Vertical,	
                    dn_110_RG_Esfera,	
                    dn_110_RG_Gaveta,	
                    dn_110_RG_Pressao,	
                    dn_110_RG_Angular,	
                    dn_110_Entrada_Normal,	
                    dn_110_Entrada_Borda,	
                    dn_110_Saida_Canalizacao,
                    ]
                }

        df_110= pd.DataFrame(equi_110)
        SR_110 = pd.Series(df_110['Conexão'])
        EQ_110 = SR_110.sum()

        comp_eq_pvc_dn = [
                                EQ_15,
                                EQ_20,
                                EQ_25,
                                EQ_32,
                                EQ_40,
                                EQ_50,
                                EQ_65,
                                EQ_80,
                                EQ_110
                            ]


        return(comp_eq_pvc_dn)
       
    def Comprimento_Equivalente(self, diametro):

        # isso é para PVC vai usar esses valores 
        df = pd.read_excel(r"T:\MEUS CODIGOS\venv\tabs\Tabela_Diametro_Equivalente.xlsx", sheet_name="TABELA_PVC")

        # busca diâmetro interno comercial e a linha de referência para as conexões
        Linha_ref= self.Diametro_interno_PVC(diametro)
        Linha_ref= int(Linha_ref[1])
        print('LINHA REF PROBLEMA!!!!', Linha_ref)
        
        # calculo comprimento equivalente 
        Cotovelo_90Q = self.SP_COT90.value()	
        Cotovelo_45Q = self.SP_COT45.value()
        Curva_90Q = self.SP_CURV90.value()
        Curva_45Q = self.SP_CURV45.value()	
        TE_DiretoQ = self.SP_TDIR.value()
        T_PerpendicularQ = self.SP_TLAT.value()	
        Valvula_PEQ = self.SP_VALV_PE.value()	
        Valvula_Retencao_HorizontalQ = self.SP_VALV_H.value()
        Valvula_Retencao_VerticalQ = self.SP_VALV_V.value()	
        RG_EsferaQ = self.spinBox_3.value()	
        RG_GavetaQ = self.SP_RG_GAV.value()	
        RG_PressaoQ = self.SP_RG_RP.value()	
        RG_AngularQ = self.SP_RG_ANG.value()
        Entrada_NormalQ = self.SP_ENTRADA_N.value()	
        Entrada_BordaQ = self.SP_ENTRADA_B.value()
        Saida_CanalizacaoQ = self.SP_ENTRADA_SC.value()

        


        Cotovelo_90 = float(df['Cotovelo_90'][Linha_ref])	
        Cotovelo_45	= float(df['Cotovelo_45'][Linha_ref])
        Curva_90 = float(df['Curva_90'][Linha_ref])	
        Curva_45 = float(df['Curva_45'][Linha_ref])	
        TE_Direto = float(df['TE_Direto'][Linha_ref])	
        T_Perpendicular = float(df['T_Perpendicular'][Linha_ref])	
        Valvula_PE = float(df['Valvula_PE'][Linha_ref])	
        Valvula_Retencao_Horizontal	= float(df['Valvula_Retencao_Horizontal'][Linha_ref])
        Valvula_Retencao_Vertical = float(df['Valvula_Retencao_Vertical'][Linha_ref])	
        RG_Esfera = float(df['RG_Esfera'][Linha_ref])	
        RG_Gaveta = float(df['RG_Gaveta'][Linha_ref])	
        RG_Pressao = float(df['RG_Pressao'][Linha_ref])	
        RG_Angular = float(df['RG_Angular'][Linha_ref])	
        Entrada_Normal = float(df['Entrada_Normal'][Linha_ref])	
        Entrada_Borda = float(df['Entrada_Borda'][Linha_ref])	
        Saida_Canalizacao = float(df['Saida_Canalizacao'][Linha_ref])

        Conexoes_Tab = {
                    'Pç':['Cotovelo_90',	
                            "Cotovelo_45",	
                            "Curva_90",	
                            "Curva_45",	
                            'TE_Direto',	
                            'T_Perpendicular',
                            'Valvula_PE',	
                            'Valvula_Retencao_Horizontal',	
                            'Valvula_Retencao_Vertical',	
                            'RG_Esfera',	
                            'RG_Gaveta',	
                            'RG_Pressao',	
                            'RG_Angular',	
                            'Entrada_Normal',	
                            'Entrada_Borda',	
                            'Saida_Canalizacao',
                            ],
                    'Conexão':[Cotovelo_90,	
                            Cotovelo_45,	
                            Curva_90,	
                            Curva_45,	
                            TE_Direto,	
                            T_Perpendicular,
                            Valvula_PE,	
                            Valvula_Retencao_Horizontal,	
                            Valvula_Retencao_Vertical,	
                            RG_Esfera,	
                            RG_Gaveta,	
                            RG_Pressao,	
                            RG_Angular,	
                            Entrada_Normal,	
                            Entrada_Borda,	
                            Saida_Canalizacao,
                            ],
                    'Qtda':[Cotovelo_90Q,	
                            Cotovelo_45Q,	
                            Curva_90Q,	
                            Curva_45Q,	
                            TE_DiretoQ,	
                            T_PerpendicularQ,
                            Valvula_PEQ,	
                            Valvula_Retencao_HorizontalQ,	
                            Valvula_Retencao_VerticalQ,	
                            RG_EsferaQ,	
                            RG_GavetaQ,	
                            RG_PressaoQ,	
                            RG_AngularQ,	
                            Entrada_NormalQ,	
                            Entrada_BordaQ,	
                            Saida_CanalizacaoQ,
                            ]


        }

        df2= pd.DataFrame(Conexoes_Tab)

        SR_conexoes = pd.Series(df2['Conexão'])
        SR_Qtda = pd.Series(df2['Qtda'])
        SR_ComprimentoEQ = SR_conexoes * SR_Qtda
        df2['Total'] = SR_ComprimentoEQ

        # comprimento equivalente total
        ComprimentoEQ_Total = SR_ComprimentoEQ.sum()
        # aqui encerra 
      
        return(ComprimentoEQ_Total, df2)

    def Comprimento_Equivalente_Fe(self, diametro):
        
        # ISSO é para tubos metálicos 
        #df = pd.read_excel(r"T:\MEUS CODIGOS\venv\tabs\Tabela_Diametro_Equivalente.xlsx", #sheet_name="TABELA_FERRO")

        df = self.df_FERRO
        # respectivamente busca a linha de referencia e o diametro interno comercial
     

        Linha_ref= self.Diametro_interno_FERRO(diametro)
        Linha_ref= int(Linha_ref[1])
        print('linha ref:', Linha_ref)

        # comprimento equivalente conexões FERRO
        Cotovelo_90 = float(df['Cotovelo_90'][Linha_ref])	
        Cotovelo_45	= float(df['Cotovelo_45'][Linha_ref])
        Cotovelo_Saida_Lateral	= float(df['Cotovelo_Saida_Lateral'][Linha_ref])
        Curva_90 = float(df['Curva_90'][Linha_ref])	
        Curva_90_Femea= float(df['Curva_90_Femea'][Linha_ref])	
        Curva_90_Macho_Femea= float(df['Curva_90_Macho_Femea'][Linha_ref])	
        Curva_90_Macho= float(df['Curva_90_Macho'][Linha_ref])	
        Curva_45= float(df['Curva_45'][Linha_ref])	
        Transposicao= float(df['Transposicao'][Linha_ref])	
        TE_Direto= float(df['TE_Direto'][Linha_ref])	
        T_Perpendicular= float(df['T_Perpendicular'][Linha_ref])		
        T_Direto_45= float(df['T_Direto_45'][Linha_ref])	
        T_Perpendicular_45= float(df['T_Perpendicular_45'][Linha_ref])		
        Cruzeta_Perpendicular= float(df['Cruzeta_Perpendicular'][Linha_ref])	
        T_Curva_Dupla_Saida= float(df['T_Curva_Dupla_Saida'][Linha_ref])	
        T_Curva_Dupla_Entrada= float(df['T_Curva_Dupla_Entrada'][Linha_ref])	
        Luvas= float(df['Luvas'][Linha_ref])		
        Uniao_Flange_Ovais= float(df['Uniao_Flange_Ovais'][Linha_ref])	
        Valvula_PE= float(df['Valvula_PE'][Linha_ref])	
        Valvula_Retencao_Horizontal= float(df['Valvula_Retencao_Horizontal'][Linha_ref])	
        Valvula_Retencao_Vertical= float(df['Valvula_Retencao_Vertical'][Linha_ref])	
        RG_Esfera= float(df['RG_Esfera'][Linha_ref])	
        RG_Gaveta= float(df['RG_Gaveta'][Linha_ref])	
        RG_Pressao= float(df['RG_Pressao'][Linha_ref])	
        RG_Angular= float(df['RG_Angular'][Linha_ref])	
        Entrada_Normal= float(df['Entrada_Normal'][Linha_ref])	
        Entrada_Borda= float(df['Entrada_Borda'][Linha_ref])	
        Saida_Canalizacao= float(df['Saida_Canalizacao'][Linha_ref])
        Reducao= float(df['Perda_Carga_Reducao'][Linha_ref])

        # Quantidade conexões FERRO
        Cotovelo_90Q = self.SP_COT90_F.value()
        Cotovelo_45Q = self.SP_COT45_F.value()	
        Cotovelo_Saida_LateralQ = self.SP_COT90_SLat_F.value()	
        Curva_90Q = self.SP_CURV90_F.value()	
        Curva_90_FemeaQ	= self.SP_CURV90_Fem_F.value()
        Curva_90_Macho_FemeaQ = self.SP_CURV90_MF_F.value()	
        Curva_90_MachoQ	= self.SP_CURV90_M_F.value()
        Curva_45Q = self.SP_CURV45_F.value()	
        TransposicaoQ = self.SP_VALV_H_30.value()	
        TE_DiretoQ = self.SP_TDIR_4.value()
        T_PerpendicularQ = self.SP_TLAT_4.value()	
        T_Direto_45Q = self.SP_VALV_H_32.value()	
        T_Perpendicular_45Q = self.SP_VALV_H_33.value()		
        Cruzeta_PerpendicularQ = self.SP_VALV_H_31.value()	
        T_Curva_Dupla_SaidaQ = self.SP_VALV_H_34.value()
        T_Curva_Dupla_EntradaQ = self.SP_VALV_H_35.value()
        LuvasQ = self.SP_VALV_H_36.value()		
        Uniao_Flange_OvaisQ = self.SP_VALV_H_37.value()	
        Valvula_PEQ	= self.SP_VALV_PE_F.value()
        Valvula_Retencao_HorizontalQ = self.SP_VALV_H_25.value()	
        Valvula_Retencao_VerticalQ	= self.SP_VALV_V_4.value()
        RG_EsferaQ = self.SP_RG_ESF_F.value()	
        RG_GavetaQ = self.SP_RG_GAV_F.value()	
        RG_PressaoQ = self.SP_RG_RP_F.value()	
        RG_AngularQ	= self.SP_RG_ANG_F.value()
        Entrada_NormalQ = self.SP_ENTRADA_N_F.value()	
        Entrada_BordaQ = self.SP_ENTRADA_B_F.value()	
        Saida_CanalizacaoQ = self.SP_ENTRADA_SC_F.value()
        ReducaoQ = self.SP_TE_Red_12.value()


        Conexoes_Tab_Fe = {
                                      
                            'Conexão':[Cotovelo_90,	
                                    Cotovelo_45,	
                                    Cotovelo_Saida_Lateral,	
                                    Curva_90,	
                                    Curva_90_Femea,	
                                    Curva_90_Macho_Femea,	
                                    Curva_90_Macho,	
                                    Curva_45,		
                                    Transposicao,	
                                    TE_Direto,	
                                    T_Perpendicular,		
                                    T_Direto_45,	
                                    T_Perpendicular_45,	
                                    Cruzeta_Perpendicular,	
                                    T_Curva_Dupla_Saida,	
                                    T_Curva_Dupla_Entrada,	
                                    Luvas,	
                                    Uniao_Flange_Ovais,	
                                    Valvula_PE,	
                                    Valvula_Retencao_Horizontal,	
                                    Valvula_Retencao_Vertical,	
                                    RG_Esfera,	
                                    RG_Gaveta,	
                                    RG_Pressao,	
                                    RG_Angular,	
                                    Entrada_Normal,	
                                    Entrada_Borda,	
                                    Saida_Canalizacao,
                                    Reducao,
                                    ],
                            'Qtda':[Cotovelo_90Q,		
                                    Cotovelo_45Q,	
                                    Cotovelo_Saida_LateralQ,	
                                    Curva_90Q,	
                                    Curva_90_FemeaQ,	
                                    Curva_90_Macho_FemeaQ,	
                                    Curva_90_MachoQ,	
                                    Curva_45Q,		
                                    TransposicaoQ,	
                                    TE_DiretoQ,	
                                    T_PerpendicularQ,		
                                    T_Direto_45Q,	
                                    T_Perpendicular_45Q,	
                                    Cruzeta_PerpendicularQ,	
                                    T_Curva_Dupla_SaidaQ,	
                                    T_Curva_Dupla_EntradaQ,	
                                    LuvasQ,	
                                    Uniao_Flange_OvaisQ,	
                                    Valvula_PEQ,	
                                    Valvula_Retencao_HorizontalQ,	
                                    Valvula_Retencao_VerticalQ,	
                                    RG_EsferaQ,	
                                    RG_GavetaQ,	
                                    RG_PressaoQ,	
                                    RG_AngularQ,	
                                    Entrada_NormalQ,	
                                    Entrada_BordaQ,	
                                    Saida_CanalizacaoQ,
                                    ReducaoQ,

                                    ]

                            }

        df3= pd.DataFrame(Conexoes_Tab_Fe)
        SR_conexoes = pd.Series(df3['Conexão'])
        SR_Qtda = pd.Series(df3['Qtda'])
        SR_ComprimentoEQ = SR_conexoes * SR_Qtda
        df3['Total'] = SR_ComprimentoEQ
        print('comprimento total FERRO série:')
        print(df3['Total'])
                
        # comprimento equivalente total
        ComprimentoEQ_Total = SR_ComprimentoEQ.sum()
        print('COMPRIMENTO EQUIVALENTE OK:', ComprimentoEQ_Total)


        return(ComprimentoEQ_Total, df3)

    def Comprimento_tabview_Fe(self):
        
        # ISSO é para tubos metálicos 
        #df = pd.read_excel(r"T:\MEUS CODIGOS\venv\tabs\Tabela_Diametro_Equivalente.xlsx", #sheet_name="TABELA_FERRO")
        df = self.df_FERRO
        # respectivamente busca a linha de referencia e o diametro interno comercial
     

        # Quantidade conexões FERRO
        Cotovelo_90Q = self.SP_COT90_F.value()
        Cotovelo_45Q = self.SP_COT45_F.value()	
        Cotovelo_Saida_LateralQ = self.SP_COT90_SLat_F.value()	
        Curva_90Q = self.SP_CURV90_F.value()	
        Curva_90_FemeaQ	= self.SP_CURV90_Fem_F.value()
        Curva_90_Macho_FemeaQ = self.SP_CURV90_MF_F.value()	
        Curva_90_MachoQ	= self.SP_CURV90_M_F.value()
        Curva_45Q = self.SP_CURV45_F.value()	
        TransposicaoQ = self.SP_VALV_H_30.value()	
        TE_DiretoQ = self.SP_TDIR_4.value()
        T_PerpendicularQ = self.SP_TLAT_4.value()	
        T_Direto_45Q = self.SP_VALV_H_32.value()	
        T_Perpendicular_45Q = self.SP_VALV_H_33.value()		
        Cruzeta_PerpendicularQ = self.SP_VALV_H_31.value()	
        T_Curva_Dupla_SaidaQ = self.SP_VALV_H_34.value()
        T_Curva_Dupla_EntradaQ = self.SP_VALV_H_35.value()
        LuvasQ = self.SP_VALV_H_36.value()		
        Uniao_Flange_OvaisQ = self.SP_VALV_H_37.value()	
        Valvula_PEQ	= self.SP_VALV_PE_F.value()
        Valvula_Retencao_HorizontalQ = self.SP_VALV_H_25.value()	
        Valvula_Retencao_VerticalQ	= self.SP_VALV_V_4.value()
        RG_EsferaQ = self.SP_RG_ESF_F.value()	
        RG_GavetaQ = self.SP_RG_GAV_F.value()	
        RG_PressaoQ = self.SP_RG_RP_F.value()	
        RG_AngularQ	= self.SP_RG_ANG_F.value()
        Entrada_NormalQ = self.SP_ENTRADA_N_F.value()	
        Entrada_BordaQ = self.SP_ENTRADA_B_F.value()	
        Saida_CanalizacaoQ = self.SP_ENTRADA_SC_F.value()
        ReducaoQ = self.SP_TE_Red_12.value()

        #dn_13_
        dn_13_Cotovelo_90 = float(df['Cotovelo_90'][2])*Cotovelo_90Q
        dn_13_Cotovelo_45= float(df['Cotovelo_45'][2])* Cotovelo_45Q
        dn_13_Cotovelo_Saida_Lateral= float(df['Cotovelo_Saida_Lateral'][2])*Cotovelo_Saida_LateralQ
        dn_13_Curva_90 = float(df['Curva_90'][2])*Curva_90Q	
        dn_13_Curva_90_Femea= float(df['Curva_90_Femea'][2])*	Curva_90_FemeaQ
        dn_13_Curva_90_Macho_Femea= float(df['Curva_90_Macho_Femea'][2])*	Curva_90_Macho_FemeaQ
        dn_13_Curva_90_Macho= float(df['Curva_90_Macho'][2])*	Curva_90_MachoQ
        dn_13_Curva_45= float(df['Curva_45'][2])*	Curva_45Q
        dn_13_Transposicao= float(df['Transposicao'][2])*	TransposicaoQ
        dn_13_TE_Direto= float(df['TE_Direto'][2])* TE_DiretoQ	
        dn_13_T_Perpendicular= float(df['T_Perpendicular'][2])* T_PerpendicularQ		
        dn_13_T_Direto_45= float(df['T_Direto_45'][2])*T_Direto_45Q 	
        dn_13_T_Perpendicular_45= float(df['T_Perpendicular_45'][2])*T_Perpendicular_45Q		
        dn_13_Cruzeta_Perpendicular= float(df['Cruzeta_Perpendicular'][2])*Cruzeta_PerpendicularQ	
        dn_13_T_Curva_Dupla_Saida= float(df['T_Curva_Dupla_Saida'][2])*T_Curva_Dupla_SaidaQ	
        dn_13_T_Curva_Dupla_Entrada= float(df['T_Curva_Dupla_Entrada'][2])*T_Curva_Dupla_EntradaQ	
        dn_13_Luvas= float(df['Luvas'][2])*LuvasQ		
        dn_13_Uniao_Flange_Ovais= float(df['Uniao_Flange_Ovais'][2])*Uniao_Flange_OvaisQ	
        dn_13_Valvula_PE= float(df['Valvula_PE'][2])*Valvula_PEQ	
        dn_13_Valvula_Retencao_Horizontal= float(df['Valvula_Retencao_Horizontal'][2])*Valvula_Retencao_HorizontalQ	
        dn_13_Valvula_Retencao_Vertical= float(df['Valvula_Retencao_Vertical'][2])*Valvula_Retencao_VerticalQ	
        dn_13_RG_Esfera= float(df['RG_Esfera'][2])*RG_EsferaQ	
        dn_13_RG_Gaveta= float(df['RG_Gaveta'][2])*RG_GavetaQ	
        dn_13_RG_Pressao= float(df['RG_Pressao'][2])*RG_PressaoQ	
        dn_13_RG_Angular= float(df['RG_Angular'][2])*RG_AngularQ		
        dn_13_Entrada_Normal= float(df['Entrada_Normal'][2])*Entrada_NormalQ	
        dn_13_Entrada_Borda= float(df['Entrada_Borda'][2])*Entrada_BordaQ	
        dn_13_Saida_Canalizacao= float(df['Saida_Canalizacao'][2])*Saida_CanalizacaoQ
        dn_13_Reducao= float(df['Perda_Carga_Reducao'][2])*ReducaoQ

        equi_13 = {
            'Conexão':[dn_13_Cotovelo_90,	
                            dn_13_Cotovelo_45,	
                            dn_13_Cotovelo_Saida_Lateral,	
                            dn_13_Curva_90,	
                            dn_13_Curva_90_Femea,	
                            dn_13_Curva_90_Macho_Femea,	
                            dn_13_Curva_90_Macho,	
                            dn_13_Curva_45,		
                            dn_13_Transposicao,	
                            dn_13_TE_Direto,	
                            dn_13_T_Perpendicular,		
                            dn_13_T_Direto_45,	
                            dn_13_T_Perpendicular_45,	
                            dn_13_Cruzeta_Perpendicular,	
                            dn_13_T_Curva_Dupla_Saida,	
                            dn_13_T_Curva_Dupla_Entrada,	
                            dn_13_Luvas,	
                            dn_13_Uniao_Flange_Ovais,	
                            dn_13_Valvula_PE,	
                            dn_13_Valvula_Retencao_Horizontal,	
                            dn_13_Valvula_Retencao_Vertical,	
                            dn_13_RG_Esfera,	
                            dn_13_RG_Gaveta,	
                            dn_13_RG_Pressao,	
                            dn_13_RG_Angular,	
                            dn_13_Entrada_Normal,	
                            dn_13_Entrada_Borda,	
                            dn_13_Saida_Canalizacao,
                            dn_13_Reducao,
                    ]
                }

        df_13= pd.DataFrame(equi_13)
        SR_13 = pd.Series(df_13['Conexão'])
        EQ_13 = SR_13.sum()

        #dn_19_
        dn_19_Cotovelo_90 = float(df['Cotovelo_90'][3])*Cotovelo_90Q
        dn_19_Cotovelo_45= float(df['Cotovelo_45'][3])* Cotovelo_45Q
        dn_19_Cotovelo_Saida_Lateral= float(df['Cotovelo_Saida_Lateral'][3])*Cotovelo_Saida_LateralQ
        dn_19_Curva_90 = float(df['Curva_90'][3])*Curva_90Q	
        dn_19_Curva_90_Femea= float(df['Curva_90_Femea'][3])*	Curva_90_FemeaQ
        dn_19_Curva_90_Macho_Femea= float(df['Curva_90_Macho_Femea'][3])*	Curva_90_Macho_FemeaQ
        dn_19_Curva_90_Macho= float(df['Curva_90_Macho'][3])*	Curva_90_MachoQ
        dn_19_Curva_45= float(df['Curva_45'][3])*	Curva_45Q
        dn_19_Transposicao= float(df['Transposicao'][3])*	TransposicaoQ
        dn_19_TE_Direto= float(df['TE_Direto'][3])* TE_DiretoQ	
        dn_19_T_Perpendicular= float(df['T_Perpendicular'][3])* T_PerpendicularQ		
        dn_19_T_Direto_45= float(df['T_Direto_45'][3])*T_Direto_45Q 	
        dn_19_T_Perpendicular_45= float(df['T_Perpendicular_45'][3])*T_Perpendicular_45Q		
        dn_19_Cruzeta_Perpendicular= float(df['Cruzeta_Perpendicular'][3])*Cruzeta_PerpendicularQ	
        dn_19_T_Curva_Dupla_Saida= float(df['T_Curva_Dupla_Saida'][3])*T_Curva_Dupla_SaidaQ	
        dn_19_T_Curva_Dupla_Entrada= float(df['T_Curva_Dupla_Entrada'][3])*T_Curva_Dupla_EntradaQ	
        dn_19_Luvas= float(df['Luvas'][3])*LuvasQ		
        dn_19_Uniao_Flange_Ovais= float(df['Uniao_Flange_Ovais'][3])*Uniao_Flange_OvaisQ	
        dn_19_Valvula_PE= float(df['Valvula_PE'][3])*Valvula_PEQ	
        dn_19_Valvula_Retencao_Horizontal= float(df['Valvula_Retencao_Horizontal'][3])*Valvula_Retencao_HorizontalQ	
        dn_19_Valvula_Retencao_Vertical= float(df['Valvula_Retencao_Vertical'][3])*Valvula_Retencao_VerticalQ	
        dn_19_RG_Esfera= float(df['RG_Esfera'][3])*RG_EsferaQ	
        dn_19_RG_Gaveta= float(df['RG_Gaveta'][3])*RG_GavetaQ	
        dn_19_RG_Pressao= float(df['RG_Pressao'][3])*RG_PressaoQ	
        dn_19_RG_Angular= float(df['RG_Angular'][3])*RG_AngularQ		
        dn_19_Entrada_Normal= float(df['Entrada_Normal'][3])*Entrada_NormalQ	
        dn_19_Entrada_Borda= float(df['Entrada_Borda'][3])*Entrada_BordaQ	
        dn_19_Saida_Canalizacao= float(df['Saida_Canalizacao'][3])*Saida_CanalizacaoQ
        dn_19_Reducao= float(df['Perda_Carga_Reducao'][3])*ReducaoQ

        equi_19 = {
            'Conexão':[dn_19_Cotovelo_90,	
                            dn_19_Cotovelo_45,	
                            dn_19_Cotovelo_Saida_Lateral,	
                            dn_19_Curva_90,	
                            dn_19_Curva_90_Femea,	
                            dn_19_Curva_90_Macho_Femea,	
                            dn_19_Curva_90_Macho,	
                            dn_19_Curva_45,		
                            dn_19_Transposicao,	
                            dn_19_TE_Direto,	
                            dn_19_T_Perpendicular,		
                            dn_19_T_Direto_45,	
                            dn_19_T_Perpendicular_45,	
                            dn_19_Cruzeta_Perpendicular,	
                            dn_19_T_Curva_Dupla_Saida,	
                            dn_19_T_Curva_Dupla_Entrada,	
                            dn_19_Luvas,	
                            dn_19_Uniao_Flange_Ovais,	
                            dn_19_Valvula_PE,	
                            dn_19_Valvula_Retencao_Horizontal,	
                            dn_19_Valvula_Retencao_Vertical,	
                            dn_19_RG_Esfera,	
                            dn_19_RG_Gaveta,	
                            dn_19_RG_Pressao,	
                            dn_19_RG_Angular,	
                            dn_19_Entrada_Normal,	
                            dn_19_Entrada_Borda,	
                            dn_19_Saida_Canalizacao,
                            dn_19_Reducao,
                    ]
                }

        df_19= pd.DataFrame(equi_19)
        SR_19 = pd.Series(df_19['Conexão'])
        EQ_19 = SR_19.sum()


        #dn_25_
        dn_25_Cotovelo_90 = float(df['Cotovelo_90'][4])*Cotovelo_90Q
        dn_25_Cotovelo_45= float(df['Cotovelo_45'][4])* Cotovelo_45Q
        dn_25_Cotovelo_Saida_Lateral= float(df['Cotovelo_Saida_Lateral'][4])*Cotovelo_Saida_LateralQ
        dn_25_Curva_90 = float(df['Curva_90'][4])*Curva_90Q	
        dn_25_Curva_90_Femea= float(df['Curva_90_Femea'][4])*	Curva_90_FemeaQ
        dn_25_Curva_90_Macho_Femea= float(df['Curva_90_Macho_Femea'][4])*	Curva_90_Macho_FemeaQ
        dn_25_Curva_90_Macho= float(df['Curva_90_Macho'][4])*	Curva_90_MachoQ
        dn_25_Curva_45= float(df['Curva_45'][4])*	Curva_45Q
        dn_25_Transposicao= float(df['Transposicao'][4])*	TransposicaoQ
        dn_25_TE_Direto= float(df['TE_Direto'][4])* TE_DiretoQ	
        dn_25_T_Perpendicular= float(df['T_Perpendicular'][4])* T_PerpendicularQ		
        dn_25_T_Direto_45= float(df['T_Direto_45'][4])*T_Direto_45Q 	
        dn_25_T_Perpendicular_45= float(df['T_Perpendicular_45'][4])*T_Perpendicular_45Q		
        dn_25_Cruzeta_Perpendicular= float(df['Cruzeta_Perpendicular'][4])*Cruzeta_PerpendicularQ	
        dn_25_T_Curva_Dupla_Saida= float(df['T_Curva_Dupla_Saida'][4])*T_Curva_Dupla_SaidaQ	
        dn_25_T_Curva_Dupla_Entrada= float(df['T_Curva_Dupla_Entrada'][4])*T_Curva_Dupla_EntradaQ	
        dn_25_Luvas= float(df['Luvas'][4])*LuvasQ		
        dn_25_Uniao_Flange_Ovais= float(df['Uniao_Flange_Ovais'][4])*Uniao_Flange_OvaisQ	
        dn_25_Valvula_PE= float(df['Valvula_PE'][4])*Valvula_PEQ	
        dn_25_Valvula_Retencao_Horizontal= float(df['Valvula_Retencao_Horizontal'][4])*Valvula_Retencao_HorizontalQ	
        dn_25_Valvula_Retencao_Vertical= float(df['Valvula_Retencao_Vertical'][4])*Valvula_Retencao_VerticalQ	
        dn_25_RG_Esfera= float(df['RG_Esfera'][4])*RG_EsferaQ	
        dn_25_RG_Gaveta= float(df['RG_Gaveta'][4])*RG_GavetaQ	
        dn_25_RG_Pressao= float(df['RG_Pressao'][4])*RG_PressaoQ	
        dn_25_RG_Angular= float(df['RG_Angular'][4])*RG_AngularQ		
        dn_25_Entrada_Normal= float(df['Entrada_Normal'][4])*Entrada_NormalQ	
        dn_25_Entrada_Borda= float(df['Entrada_Borda'][4])*Entrada_BordaQ	
        dn_25_Saida_Canalizacao= float(df['Saida_Canalizacao'][4])*Saida_CanalizacaoQ
        dn_25_Reducao= float(df['Perda_Carga_Reducao'][4])*ReducaoQ

        equi_25 = {
            'Conexão':[dn_25_Cotovelo_90,	
                            dn_25_Cotovelo_45,	
                            dn_25_Cotovelo_Saida_Lateral,	
                            dn_25_Curva_90,	
                            dn_25_Curva_90_Femea,	
                            dn_25_Curva_90_Macho_Femea,	
                            dn_25_Curva_90_Macho,	
                            dn_25_Curva_45,		
                            dn_25_Transposicao,	
                            dn_25_TE_Direto,	
                            dn_25_T_Perpendicular,		
                            dn_25_T_Direto_45,	
                            dn_25_T_Perpendicular_45,	
                            dn_25_Cruzeta_Perpendicular,	
                            dn_25_T_Curva_Dupla_Saida,	
                            dn_25_T_Curva_Dupla_Entrada,	
                            dn_25_Luvas,	
                            dn_25_Uniao_Flange_Ovais,	
                            dn_25_Valvula_PE,	
                            dn_25_Valvula_Retencao_Horizontal,	
                            dn_25_Valvula_Retencao_Vertical,	
                            dn_25_RG_Esfera,	
                            dn_25_RG_Gaveta,	
                            dn_25_RG_Pressao,	
                            dn_25_RG_Angular,	
                            dn_25_Entrada_Normal,	
                            dn_25_Entrada_Borda,	
                            dn_25_Saida_Canalizacao,
                            dn_25_Reducao,
                    ]
                }

        df_25= pd.DataFrame(equi_25)
        SR_25 = pd.Series(df_25['Conexão'])
        EQ_25 = SR_25.sum()

        #dn_32_
        dn_32_Cotovelo_90 = float(df['Cotovelo_90'][5])*Cotovelo_90Q
        dn_32_Cotovelo_45= float(df['Cotovelo_45'][5])* Cotovelo_45Q
        dn_32_Cotovelo_Saida_Lateral= float(df['Cotovelo_Saida_Lateral'][5])*Cotovelo_Saida_LateralQ
        dn_32_Curva_90 = float(df['Curva_90'][5])*Curva_90Q	
        dn_32_Curva_90_Femea= float(df['Curva_90_Femea'][5])*	Curva_90_FemeaQ
        dn_32_Curva_90_Macho_Femea= float(df['Curva_90_Macho_Femea'][5])*	Curva_90_Macho_FemeaQ
        dn_32_Curva_90_Macho= float(df['Curva_90_Macho'][5])*	Curva_90_MachoQ
        dn_32_Curva_45= float(df['Curva_45'][5])*	Curva_45Q
        dn_32_Transposicao= float(df['Transposicao'][5])*	TransposicaoQ
        dn_32_TE_Direto= float(df['TE_Direto'][5])* TE_DiretoQ	
        dn_32_T_Perpendicular= float(df['T_Perpendicular'][5])* T_PerpendicularQ		
        dn_32_T_Direto_45= float(df['T_Direto_45'][5])*T_Direto_45Q 	
        dn_32_T_Perpendicular_45= float(df['T_Perpendicular_45'][5])*T_Perpendicular_45Q		
        dn_32_Cruzeta_Perpendicular= float(df['Cruzeta_Perpendicular'][5])*Cruzeta_PerpendicularQ	
        dn_32_T_Curva_Dupla_Saida= float(df['T_Curva_Dupla_Saida'][5])*T_Curva_Dupla_SaidaQ	
        dn_32_T_Curva_Dupla_Entrada= float(df['T_Curva_Dupla_Entrada'][5])*T_Curva_Dupla_EntradaQ	
        dn_32_Luvas= float(df['Luvas'][5])*LuvasQ		
        dn_32_Uniao_Flange_Ovais= float(df['Uniao_Flange_Ovais'][5])*Uniao_Flange_OvaisQ	
        dn_32_Valvula_PE= float(df['Valvula_PE'][5])*Valvula_PEQ	
        dn_32_Valvula_Retencao_Horizontal= float(df['Valvula_Retencao_Horizontal'][5])*Valvula_Retencao_HorizontalQ	
        dn_32_Valvula_Retencao_Vertical= float(df['Valvula_Retencao_Vertical'][5])*Valvula_Retencao_VerticalQ	
        dn_32_RG_Esfera= float(df['RG_Esfera'][5])*RG_EsferaQ	
        dn_32_RG_Gaveta= float(df['RG_Gaveta'][5])*RG_GavetaQ	
        dn_32_RG_Pressao= float(df['RG_Pressao'][5])*RG_PressaoQ	
        dn_32_RG_Angular= float(df['RG_Angular'][5])*RG_AngularQ		
        dn_32_Entrada_Normal= float(df['Entrada_Normal'][5])*Entrada_NormalQ	
        dn_32_Entrada_Borda= float(df['Entrada_Borda'][5])*Entrada_BordaQ	
        dn_32_Saida_Canalizacao= float(df['Saida_Canalizacao'][5])*Saida_CanalizacaoQ
        dn_32_Reducao= float(df['Perda_Carga_Reducao'][5])*ReducaoQ

        equi_32 = {
            'Conexão':[dn_32_Cotovelo_90,	
                            dn_32_Cotovelo_45,	
                            dn_32_Cotovelo_Saida_Lateral,	
                            dn_32_Curva_90,	
                            dn_32_Curva_90_Femea,	
                            dn_32_Curva_90_Macho_Femea,	
                            dn_32_Curva_90_Macho,	
                            dn_32_Curva_45,		
                            dn_32_Transposicao,	
                            dn_32_TE_Direto,	
                            dn_32_T_Perpendicular,		
                            dn_32_T_Direto_45,	
                            dn_32_T_Perpendicular_45,	
                            dn_32_Cruzeta_Perpendicular,	
                            dn_32_T_Curva_Dupla_Saida,	
                            dn_32_T_Curva_Dupla_Entrada,	
                            dn_32_Luvas,	
                            dn_32_Uniao_Flange_Ovais,	
                            dn_32_Valvula_PE,	
                            dn_32_Valvula_Retencao_Horizontal,	
                            dn_32_Valvula_Retencao_Vertical,	
                            dn_32_RG_Esfera,	
                            dn_32_RG_Gaveta,	
                            dn_32_RG_Pressao,	
                            dn_32_RG_Angular,	
                            dn_32_Entrada_Normal,	
                            dn_32_Entrada_Borda,	
                            dn_32_Saida_Canalizacao,
                            dn_32_Reducao,
                    ]
                }

        df_32= pd.DataFrame(equi_32)
        SR_32 = pd.Series(df_32['Conexão'])
        EQ_32 = SR_32.sum()

        #dn_38_
        dn_38_Cotovelo_90 = float(df['Cotovelo_90'][6])*Cotovelo_90Q
        dn_38_Cotovelo_45= float(df['Cotovelo_45'][6])* Cotovelo_45Q
        dn_38_Cotovelo_Saida_Lateral= float(df['Cotovelo_Saida_Lateral'][6])*Cotovelo_Saida_LateralQ
        dn_38_Curva_90 = float(df['Curva_90'][6])*Curva_90Q	
        dn_38_Curva_90_Femea= float(df['Curva_90_Femea'][6])*	Curva_90_FemeaQ
        dn_38_Curva_90_Macho_Femea= float(df['Curva_90_Macho_Femea'][6])*	Curva_90_Macho_FemeaQ
        dn_38_Curva_90_Macho= float(df['Curva_90_Macho'][6])*	Curva_90_MachoQ
        dn_38_Curva_45= float(df['Curva_45'][6])*	Curva_45Q
        dn_38_Transposicao= float(df['Transposicao'][6])*	TransposicaoQ
        dn_38_TE_Direto= float(df['TE_Direto'][6])* TE_DiretoQ	
        dn_38_T_Perpendicular= float(df['T_Perpendicular'][6])* T_PerpendicularQ		
        dn_38_T_Direto_45= float(df['T_Direto_45'][6])*T_Direto_45Q 	
        dn_38_T_Perpendicular_45= float(df['T_Perpendicular_45'][6])*T_Perpendicular_45Q		
        dn_38_Cruzeta_Perpendicular= float(df['Cruzeta_Perpendicular'][6])*Cruzeta_PerpendicularQ	
        dn_38_T_Curva_Dupla_Saida= float(df['T_Curva_Dupla_Saida'][6])*T_Curva_Dupla_SaidaQ	
        dn_38_T_Curva_Dupla_Entrada= float(df['T_Curva_Dupla_Entrada'][6])*T_Curva_Dupla_EntradaQ	
        dn_38_Luvas= float(df['Luvas'][6])*LuvasQ		
        dn_38_Uniao_Flange_Ovais= float(df['Uniao_Flange_Ovais'][6])*Uniao_Flange_OvaisQ	
        dn_38_Valvula_PE= float(df['Valvula_PE'][6])*Valvula_PEQ	
        dn_38_Valvula_Retencao_Horizontal= float(df['Valvula_Retencao_Horizontal'][6])*Valvula_Retencao_HorizontalQ	
        dn_38_Valvula_Retencao_Vertical= float(df['Valvula_Retencao_Vertical'][6])*Valvula_Retencao_VerticalQ	
        dn_38_RG_Esfera= float(df['RG_Esfera'][6])*RG_EsferaQ	
        dn_38_RG_Gaveta= float(df['RG_Gaveta'][6])*RG_GavetaQ	
        dn_38_RG_Pressao= float(df['RG_Pressao'][6])*RG_PressaoQ	
        dn_38_RG_Angular= float(df['RG_Angular'][6])*RG_AngularQ		
        dn_38_Entrada_Normal= float(df['Entrada_Normal'][6])*Entrada_NormalQ	
        dn_38_Entrada_Borda= float(df['Entrada_Borda'][6])*Entrada_BordaQ	
        dn_38_Saida_Canalizacao= float(df['Saida_Canalizacao'][6])*Saida_CanalizacaoQ
        dn_38_Reducao= float(df['Perda_Carga_Reducao'][6])*ReducaoQ

        equi_38 = {
            'Conexão':[dn_38_Cotovelo_90,	
                            dn_38_Cotovelo_45,	
                            dn_38_Cotovelo_Saida_Lateral,	
                            dn_38_Curva_90,	
                            dn_38_Curva_90_Femea,	
                            dn_38_Curva_90_Macho_Femea,	
                            dn_38_Curva_90_Macho,	
                            dn_38_Curva_45,		
                            dn_38_Transposicao,	
                            dn_38_TE_Direto,	
                            dn_38_T_Perpendicular,		
                            dn_38_T_Direto_45,	
                            dn_38_T_Perpendicular_45,	
                            dn_38_Cruzeta_Perpendicular,	
                            dn_38_T_Curva_Dupla_Saida,	
                            dn_38_T_Curva_Dupla_Entrada,	
                            dn_38_Luvas,	
                            dn_38_Uniao_Flange_Ovais,	
                            dn_38_Valvula_PE,	
                            dn_38_Valvula_Retencao_Horizontal,	
                            dn_38_Valvula_Retencao_Vertical,	
                            dn_38_RG_Esfera,	
                            dn_38_RG_Gaveta,	
                            dn_38_RG_Pressao,	
                            dn_38_RG_Angular,	
                            dn_38_Entrada_Normal,	
                            dn_38_Entrada_Borda,	
                            dn_38_Saida_Canalizacao,
                            dn_38_Reducao,
                    ]
                }

        df_38= pd.DataFrame(equi_38)
        SR_38 = pd.Series(df_38['Conexão'])
        EQ_38 = SR_38.sum()

        #dn_38_
        dn_50_Cotovelo_90 = float(df['Cotovelo_90'][7])*Cotovelo_90Q
        dn_50_Cotovelo_45= float(df['Cotovelo_45'][7])* Cotovelo_45Q
        dn_50_Cotovelo_Saida_Lateral= float(df['Cotovelo_Saida_Lateral'][7])*Cotovelo_Saida_LateralQ
        dn_50_Curva_90 = float(df['Curva_90'][7])*Curva_90Q	
        dn_50_Curva_90_Femea= float(df['Curva_90_Femea'][7])*	Curva_90_FemeaQ
        dn_50_Curva_90_Macho_Femea= float(df['Curva_90_Macho_Femea'][7])*	Curva_90_Macho_FemeaQ
        dn_50_Curva_90_Macho= float(df['Curva_90_Macho'][7])*	Curva_90_MachoQ
        dn_50_Curva_45= float(df['Curva_45'][7])*	Curva_45Q
        dn_50_Transposicao= float(df['Transposicao'][7])*	TransposicaoQ
        dn_50_TE_Direto= float(df['TE_Direto'][7])* TE_DiretoQ	
        dn_50_T_Perpendicular= float(df['T_Perpendicular'][7])* T_PerpendicularQ		
        dn_50_T_Direto_45= float(df['T_Direto_45'][7])*T_Direto_45Q 	
        dn_50_T_Perpendicular_45= float(df['T_Perpendicular_45'][7])*T_Perpendicular_45Q		
        dn_50_Cruzeta_Perpendicular= float(df['Cruzeta_Perpendicular'][7])*Cruzeta_PerpendicularQ	
        dn_50_T_Curva_Dupla_Saida= float(df['T_Curva_Dupla_Saida'][7])*T_Curva_Dupla_SaidaQ	
        dn_50_T_Curva_Dupla_Entrada= float(df['T_Curva_Dupla_Entrada'][7])*T_Curva_Dupla_EntradaQ	
        dn_50_Luvas= float(df['Luvas'][7])*LuvasQ		
        dn_50_Uniao_Flange_Ovais= float(df['Uniao_Flange_Ovais'][7])*Uniao_Flange_OvaisQ	
        dn_50_Valvula_PE= float(df['Valvula_PE'][7])*Valvula_PEQ	
        dn_50_Valvula_Retencao_Horizontal= float(df['Valvula_Retencao_Horizontal'][7])*Valvula_Retencao_HorizontalQ	
        dn_50_Valvula_Retencao_Vertical= float(df['Valvula_Retencao_Vertical'][7])*Valvula_Retencao_VerticalQ	
        dn_50_RG_Esfera= float(df['RG_Esfera'][7])*RG_EsferaQ	
        dn_50_RG_Gaveta= float(df['RG_Gaveta'][7])*RG_GavetaQ	
        dn_50_RG_Pressao= float(df['RG_Pressao'][7])*RG_PressaoQ	
        dn_50_RG_Angular= float(df['RG_Angular'][7])*RG_AngularQ		
        dn_50_Entrada_Normal= float(df['Entrada_Normal'][7])*Entrada_NormalQ	
        dn_50_Entrada_Borda= float(df['Entrada_Borda'][7])*Entrada_BordaQ	
        dn_50_Saida_Canalizacao= float(df['Saida_Canalizacao'][7])*Saida_CanalizacaoQ
        dn_50_Reducao= float(df['Perda_Carga_Reducao'][7])*ReducaoQ

        equi_50 = {
            'Conexão':[dn_50_Cotovelo_90,	
                            dn_50_Cotovelo_45,	
                            dn_50_Cotovelo_Saida_Lateral,	
                            dn_50_Curva_90,	
                            dn_50_Curva_90_Femea,	
                            dn_50_Curva_90_Macho_Femea,	
                            dn_50_Curva_90_Macho,	
                            dn_50_Curva_45,		
                            dn_50_Transposicao,	
                            dn_50_TE_Direto,	
                            dn_50_T_Perpendicular,		
                            dn_50_T_Direto_45,	
                            dn_50_T_Perpendicular_45,	
                            dn_50_Cruzeta_Perpendicular,	
                            dn_50_T_Curva_Dupla_Saida,	
                            dn_50_T_Curva_Dupla_Entrada,	
                            dn_50_Luvas,	
                            dn_50_Uniao_Flange_Ovais,	
                            dn_50_Valvula_PE,	
                            dn_50_Valvula_Retencao_Horizontal,	
                            dn_50_Valvula_Retencao_Vertical,	
                            dn_50_RG_Esfera,	
                            dn_50_RG_Gaveta,	
                            dn_50_RG_Pressao,	
                            dn_50_RG_Angular,	
                            dn_50_Entrada_Normal,	
                            dn_50_Entrada_Borda,	
                            dn_50_Saida_Canalizacao,
                            dn_50_Reducao,
                    ]
                }

        df_50= pd.DataFrame(equi_50)
        SR_50 = pd.Series(df_50['Conexão'])
        EQ_50 = SR_50.sum()

        #dn_63_
        dn_63_Cotovelo_90 = float(df['Cotovelo_90'][8])*Cotovelo_90Q
        dn_63_Cotovelo_45= float(df['Cotovelo_45'][8])* Cotovelo_45Q
        dn_63_Cotovelo_Saida_Lateral= float(df['Cotovelo_Saida_Lateral'][8])*Cotovelo_Saida_LateralQ
        dn_63_Curva_90 = float(df['Curva_90'][8])*Curva_90Q	
        dn_63_Curva_90_Femea= float(df['Curva_90_Femea'][8])*	Curva_90_FemeaQ
        dn_63_Curva_90_Macho_Femea= float(df['Curva_90_Macho_Femea'][8])*	Curva_90_Macho_FemeaQ
        dn_63_Curva_90_Macho= float(df['Curva_90_Macho'][8])*	Curva_90_MachoQ
        dn_63_Curva_45= float(df['Curva_45'][8])*	Curva_45Q
        dn_63_Transposicao= float(df['Transposicao'][8])*	TransposicaoQ
        dn_63_TE_Direto= float(df['TE_Direto'][8])* TE_DiretoQ	
        dn_63_T_Perpendicular= float(df['T_Perpendicular'][8])* T_PerpendicularQ		
        dn_63_T_Direto_45= float(df['T_Direto_45'][8])*T_Direto_45Q 	
        dn_63_T_Perpendicular_45= float(df['T_Perpendicular_45'][8])*T_Perpendicular_45Q		
        dn_63_Cruzeta_Perpendicular= float(df['Cruzeta_Perpendicular'][8])*Cruzeta_PerpendicularQ	
        dn_63_T_Curva_Dupla_Saida= float(df['T_Curva_Dupla_Saida'][8])*T_Curva_Dupla_SaidaQ	
        dn_63_T_Curva_Dupla_Entrada= float(df['T_Curva_Dupla_Entrada'][8])*T_Curva_Dupla_EntradaQ	
        dn_63_Luvas= float(df['Luvas'][8])*LuvasQ		
        dn_63_Uniao_Flange_Ovais= float(df['Uniao_Flange_Ovais'][8])*Uniao_Flange_OvaisQ	
        dn_63_Valvula_PE= float(df['Valvula_PE'][8])*Valvula_PEQ	
        dn_63_Valvula_Retencao_Horizontal= float(df['Valvula_Retencao_Horizontal'][8])*Valvula_Retencao_HorizontalQ	
        dn_63_Valvula_Retencao_Vertical= float(df['Valvula_Retencao_Vertical'][8])*Valvula_Retencao_VerticalQ	
        dn_63_RG_Esfera= float(df['RG_Esfera'][8])*RG_EsferaQ	
        dn_63_RG_Gaveta= float(df['RG_Gaveta'][8])*RG_GavetaQ	
        dn_63_RG_Pressao= float(df['RG_Pressao'][8])*RG_PressaoQ	
        dn_63_RG_Angular= float(df['RG_Angular'][8])*RG_AngularQ		
        dn_63_Entrada_Normal= float(df['Entrada_Normal'][8])*Entrada_NormalQ	
        dn_63_Entrada_Borda= float(df['Entrada_Borda'][8])*Entrada_BordaQ	
        dn_63_Saida_Canalizacao= float(df['Saida_Canalizacao'][8])*Saida_CanalizacaoQ
        dn_63_Reducao= float(df['Perda_Carga_Reducao'][8])*ReducaoQ

        equi_63 = {
            'Conexão':[dn_63_Cotovelo_90,	
                            dn_63_Cotovelo_45,	
                            dn_63_Cotovelo_Saida_Lateral,	
                            dn_63_Curva_90,	
                            dn_63_Curva_90_Femea,	
                            dn_63_Curva_90_Macho_Femea,	
                            dn_63_Curva_90_Macho,	
                            dn_63_Curva_45,		
                            dn_63_Transposicao,	
                            dn_63_TE_Direto,	
                            dn_63_T_Perpendicular,		
                            dn_63_T_Direto_45,	
                            dn_63_T_Perpendicular_45,	
                            dn_63_Cruzeta_Perpendicular,	
                            dn_63_T_Curva_Dupla_Saida,	
                            dn_63_T_Curva_Dupla_Entrada,	
                            dn_63_Luvas,	
                            dn_63_Uniao_Flange_Ovais,	
                            dn_63_Valvula_PE,	
                            dn_63_Valvula_Retencao_Horizontal,	
                            dn_63_Valvula_Retencao_Vertical,	
                            dn_63_RG_Esfera,	
                            dn_63_RG_Gaveta,	
                            dn_63_RG_Pressao,	
                            dn_63_RG_Angular,	
                            dn_63_Entrada_Normal,	
                            dn_63_Entrada_Borda,	
                            dn_63_Saida_Canalizacao,
                            dn_63_Reducao,
                    ]
                }

        df_63= pd.DataFrame(equi_63)
        SR_63 = pd.Series(df_63['Conexão'])
        EQ_63 = SR_63.sum()

        #dn_75_
        dn_75_Cotovelo_90 = float(df['Cotovelo_90'][9])*Cotovelo_90Q
        dn_75_Cotovelo_45= float(df['Cotovelo_45'][9])* Cotovelo_45Q
        dn_75_Cotovelo_Saida_Lateral= float(df['Cotovelo_Saida_Lateral'][9])*Cotovelo_Saida_LateralQ
        dn_75_Curva_90 = float(df['Curva_90'][9])*Curva_90Q	
        dn_75_Curva_90_Femea= float(df['Curva_90_Femea'][9])*	Curva_90_FemeaQ
        dn_75_Curva_90_Macho_Femea= float(df['Curva_90_Macho_Femea'][9])*	Curva_90_Macho_FemeaQ
        dn_75_Curva_90_Macho= float(df['Curva_90_Macho'][9])*	Curva_90_MachoQ
        dn_75_Curva_45= float(df['Curva_45'][9])*	Curva_45Q
        dn_75_Transposicao= float(df['Transposicao'][9])*	TransposicaoQ
        dn_75_TE_Direto= float(df['TE_Direto'][9])* TE_DiretoQ	
        dn_75_T_Perpendicular= float(df['T_Perpendicular'][9])* T_PerpendicularQ		
        dn_75_T_Direto_45= float(df['T_Direto_45'][9])*T_Direto_45Q 	
        dn_75_T_Perpendicular_45= float(df['T_Perpendicular_45'][9])*T_Perpendicular_45Q		
        dn_75_Cruzeta_Perpendicular= float(df['Cruzeta_Perpendicular'][9])*Cruzeta_PerpendicularQ	
        dn_75_T_Curva_Dupla_Saida= float(df['T_Curva_Dupla_Saida'][9])*T_Curva_Dupla_SaidaQ	
        dn_75_T_Curva_Dupla_Entrada= float(df['T_Curva_Dupla_Entrada'][9])*T_Curva_Dupla_EntradaQ	
        dn_75_Luvas= float(df['Luvas'][9])*LuvasQ		
        dn_75_Uniao_Flange_Ovais= float(df['Uniao_Flange_Ovais'][9])*Uniao_Flange_OvaisQ	
        dn_75_Valvula_PE= float(df['Valvula_PE'][9])*Valvula_PEQ	
        dn_75_Valvula_Retencao_Horizontal= float(df['Valvula_Retencao_Horizontal'][9])*Valvula_Retencao_HorizontalQ	
        dn_75_Valvula_Retencao_Vertical= float(df['Valvula_Retencao_Vertical'][9])*Valvula_Retencao_VerticalQ	
        dn_75_RG_Esfera= float(df['RG_Esfera'][9])*RG_EsferaQ	
        dn_75_RG_Gaveta= float(df['RG_Gaveta'][9])*RG_GavetaQ	
        dn_75_RG_Pressao= float(df['RG_Pressao'][9])*RG_PressaoQ	
        dn_75_RG_Angular= float(df['RG_Angular'][9])*RG_AngularQ		
        dn_75_Entrada_Normal= float(df['Entrada_Normal'][9])*Entrada_NormalQ	
        dn_75_Entrada_Borda= float(df['Entrada_Borda'][9])*Entrada_BordaQ	
        dn_75_Saida_Canalizacao= float(df['Saida_Canalizacao'][9])*Saida_CanalizacaoQ
        dn_75_Reducao= float(df['Perda_Carga_Reducao'][9])*ReducaoQ

        equi_75 = {
            'Conexão':[dn_75_Cotovelo_90,	
                            dn_75_Cotovelo_45,	
                            dn_75_Cotovelo_Saida_Lateral,	
                            dn_75_Curva_90,	
                            dn_75_Curva_90_Femea,	
                            dn_75_Curva_90_Macho_Femea,	
                            dn_75_Curva_90_Macho,	
                            dn_75_Curva_45,		
                            dn_75_Transposicao,	
                            dn_75_TE_Direto,	
                            dn_75_T_Perpendicular,		
                            dn_75_T_Direto_45,	
                            dn_75_T_Perpendicular_45,	
                            dn_75_Cruzeta_Perpendicular,	
                            dn_75_T_Curva_Dupla_Saida,	
                            dn_75_T_Curva_Dupla_Entrada,	
                            dn_75_Luvas,	
                            dn_75_Uniao_Flange_Ovais,	
                            dn_75_Valvula_PE,	
                            dn_75_Valvula_Retencao_Horizontal,	
                            dn_75_Valvula_Retencao_Vertical,	
                            dn_75_RG_Esfera,	
                            dn_75_RG_Gaveta,	
                            dn_75_RG_Pressao,	
                            dn_75_RG_Angular,	
                            dn_75_Entrada_Normal,	
                            dn_75_Entrada_Borda,	
                            dn_75_Saida_Canalizacao,
                            dn_75_Reducao,
                    ]
                }

        df_75= pd.DataFrame(equi_75)
        SR_75 = pd.Series(df_75['Conexão'])
        EQ_75 = SR_75.sum()


        #dn_100_
        dn_100_Cotovelo_90 = float(df['Cotovelo_90'][10])*Cotovelo_90Q
        dn_100_Cotovelo_45= float(df['Cotovelo_45'][10])* Cotovelo_45Q
        dn_100_Cotovelo_Saida_Lateral= float(df['Cotovelo_Saida_Lateral'][10])*Cotovelo_Saida_LateralQ
        dn_100_Curva_90 = float(df['Curva_90'][10])*Curva_90Q	
        dn_100_Curva_90_Femea= float(df['Curva_90_Femea'][10])* Curva_90_FemeaQ
        dn_100_Curva_90_Macho_Femea= float(df['Curva_90_Macho_Femea'][10])* Curva_90_Macho_FemeaQ
        dn_100_Curva_90_Macho= float(df['Curva_90_Macho'][10])*Curva_90_MachoQ
        dn_100_Curva_45= float(df['Curva_45'][10])*	Curva_45Q
        dn_100_Transposicao= float(df['Transposicao'][10])*TransposicaoQ
        dn_100_TE_Direto= float(df['TE_Direto'][10])* TE_DiretoQ	
        dn_100_T_Perpendicular= float(df['T_Perpendicular'][10])* T_PerpendicularQ		
        dn_100_T_Direto_45= float(df['T_Direto_45'][10])*T_Direto_45Q 	
        dn_100_T_Perpendicular_45= float(df['T_Perpendicular_45'][10])*T_Perpendicular_45Q		
        dn_100_Cruzeta_Perpendicular= float(df['Cruzeta_Perpendicular'][10])*Cruzeta_PerpendicularQ	
        dn_100_T_Curva_Dupla_Saida= float(df['T_Curva_Dupla_Saida'][10])*T_Curva_Dupla_SaidaQ	
        dn_100_T_Curva_Dupla_Entrada= float(df['T_Curva_Dupla_Entrada'][10])*T_Curva_Dupla_EntradaQ	
        dn_100_Luvas= float(df['Luvas'][10])*LuvasQ		
        dn_100_Uniao_Flange_Ovais= float(df['Uniao_Flange_Ovais'][10])*Uniao_Flange_OvaisQ	
        dn_100_Valvula_PE= float(df['Valvula_PE'][10])*Valvula_PEQ	
        dn_100_Valvula_Retencao_Horizontal= float(df['Valvula_Retencao_Horizontal'][10])*Valvula_Retencao_HorizontalQ	
        dn_100_Valvula_Retencao_Vertical= float(df['Valvula_Retencao_Vertical'][10])*Valvula_Retencao_VerticalQ	
        dn_100_RG_Esfera= float(df['RG_Esfera'][10])*RG_EsferaQ	
        dn_100_RG_Gaveta= float(df['RG_Gaveta'][10])*RG_GavetaQ	
        dn_100_RG_Pressao= float(df['RG_Pressao'][10])*RG_PressaoQ	
        dn_100_RG_Angular= float(df['RG_Angular'][10])*RG_AngularQ		
        dn_100_Entrada_Normal= float(df['Entrada_Normal'][10])*Entrada_NormalQ	
        dn_100_Entrada_Borda= float(df['Entrada_Borda'][10])*Entrada_BordaQ	
        dn_100_Saida_Canalizacao= float(df['Saida_Canalizacao'][10])*Saida_CanalizacaoQ
        dn_100_Reducao= float(df['Perda_Carga_Reducao'][10])*ReducaoQ

        equi_100 = {
            'Conexão':[dn_100_Cotovelo_90,	
                            dn_100_Cotovelo_45,	
                            dn_100_Cotovelo_Saida_Lateral,	
                            dn_100_Curva_90,	
                            dn_100_Curva_90_Femea,	
                            dn_100_Curva_90_Macho_Femea,	
                            dn_100_Curva_90_Macho,	
                            dn_100_Curva_45,		
                            dn_100_Transposicao,	
                            dn_100_TE_Direto,	
                            dn_100_T_Perpendicular,		
                            dn_100_T_Direto_45,	
                            dn_100_T_Perpendicular_45,	
                            dn_100_Cruzeta_Perpendicular,	
                            dn_100_T_Curva_Dupla_Saida,	
                            dn_100_T_Curva_Dupla_Entrada,	
                            dn_100_Luvas,	
                            dn_100_Uniao_Flange_Ovais,	
                            dn_100_Valvula_PE,	
                            dn_100_Valvula_Retencao_Horizontal,	
                            dn_100_Valvula_Retencao_Vertical,	
                            dn_100_RG_Esfera,	
                            dn_100_RG_Gaveta,	
                            dn_100_RG_Pressao,	
                            dn_100_RG_Angular,	
                            dn_100_Entrada_Normal,	
                            dn_100_Entrada_Borda,	
                            dn_100_Saida_Canalizacao,
                            dn_100_Reducao,
                    ]
                }

        df_100= pd.DataFrame(equi_100)
        SR_100 = pd.Series(df_100['Conexão'])
        EQ_100 = SR_100.sum()

        #dn_125_
        dn_125_Cotovelo_90 = float(df['Cotovelo_90'][11])*Cotovelo_90Q
        dn_125_Cotovelo_45= float(df['Cotovelo_45'][11])* Cotovelo_45Q
        dn_125_Cotovelo_Saida_Lateral= float(df['Cotovelo_Saida_Lateral'][11])*Cotovelo_Saida_LateralQ
        dn_125_Curva_90 = float(df['Curva_90'][11])*Curva_90Q	
        dn_125_Curva_90_Femea= float(df['Curva_90_Femea'][11])*Curva_90_FemeaQ
        dn_125_Curva_90_Macho_Femea= float(df['Curva_90_Macho_Femea'][11])*Curva_90_Macho_FemeaQ
        dn_125_Curva_90_Macho= float(df['Curva_90_Macho'][11])*Curva_90_MachoQ
        dn_125_Curva_45= float(df['Curva_45'][11])*Curva_45Q
        dn_125_Transposicao= float(df['Transposicao'][11])*TransposicaoQ
        dn_125_TE_Direto= float(df['TE_Direto'][11])* TE_DiretoQ	
        dn_125_T_Perpendicular= float(df['T_Perpendicular'][11])* T_PerpendicularQ		
        dn_125_T_Direto_45= float(df['T_Direto_45'][11])*T_Direto_45Q 	
        dn_125_T_Perpendicular_45= float(df['T_Perpendicular_45'][11])*T_Perpendicular_45Q		
        dn_125_Cruzeta_Perpendicular= float(df['Cruzeta_Perpendicular'][11])*Cruzeta_PerpendicularQ	
        dn_125_T_Curva_Dupla_Saida= float(df['T_Curva_Dupla_Saida'][11])*T_Curva_Dupla_SaidaQ	
        dn_125_T_Curva_Dupla_Entrada= float(df['T_Curva_Dupla_Entrada'][11])*T_Curva_Dupla_EntradaQ	
        dn_125_Luvas= float(df['Luvas'][11])*LuvasQ		
        dn_125_Uniao_Flange_Ovais= float(df['Uniao_Flange_Ovais'][11])*Uniao_Flange_OvaisQ	
        dn_125_Valvula_PE= float(df['Valvula_PE'][11])*Valvula_PEQ	
        dn_125_Valvula_Retencao_Horizontal= float(df['Valvula_Retencao_Horizontal'][11])*Valvula_Retencao_HorizontalQ	
        dn_125_Valvula_Retencao_Vertical= float(df['Valvula_Retencao_Vertical'][11])*Valvula_Retencao_VerticalQ	
        dn_125_RG_Esfera= float(df['RG_Esfera'][11])*RG_EsferaQ	
        dn_125_RG_Gaveta= float(df['RG_Gaveta'][11])*RG_GavetaQ	
        dn_125_RG_Pressao= float(df['RG_Pressao'][11])*RG_PressaoQ	
        dn_125_RG_Angular= float(df['RG_Angular'][11])*RG_AngularQ		
        dn_125_Entrada_Normal= float(df['Entrada_Normal'][11])*Entrada_NormalQ	
        dn_125_Entrada_Borda= float(df['Entrada_Borda'][11])*Entrada_BordaQ	
        dn_125_Saida_Canalizacao= float(df['Saida_Canalizacao'][11])*Saida_CanalizacaoQ
        dn_125_Reducao= float(df['Perda_Carga_Reducao'][11])*ReducaoQ

        equi_125 = {
            'Conexão':[dn_125_Cotovelo_90,	
                            dn_125_Cotovelo_45,	
                            dn_125_Cotovelo_Saida_Lateral,	
                            dn_125_Curva_90,	
                            dn_125_Curva_90_Femea,	
                            dn_125_Curva_90_Macho_Femea,	
                            dn_125_Curva_90_Macho,	
                            dn_125_Curva_45,		
                            dn_125_Transposicao,	
                            dn_125_TE_Direto,	
                            dn_125_T_Perpendicular,		
                            dn_125_T_Direto_45,	
                            dn_125_T_Perpendicular_45,	
                            dn_125_Cruzeta_Perpendicular,	
                            dn_125_T_Curva_Dupla_Saida,	
                            dn_125_T_Curva_Dupla_Entrada,	
                            dn_125_Luvas,	
                            dn_125_Uniao_Flange_Ovais,	
                            dn_125_Valvula_PE,	
                            dn_125_Valvula_Retencao_Horizontal,	
                            dn_125_Valvula_Retencao_Vertical,	
                            dn_125_RG_Esfera,	
                            dn_125_RG_Gaveta,	
                            dn_125_RG_Pressao,	
                            dn_125_RG_Angular,	
                            dn_125_Entrada_Normal,	
                            dn_125_Entrada_Borda,	
                            dn_125_Saida_Canalizacao,
                            dn_125_Reducao,
                    ]
                }

        df_125= pd.DataFrame(equi_125)
        SR_125 = pd.Series(df_125['Conexão'])
        EQ_125 = SR_125.sum()

        #dn_150_
        dn_150_Cotovelo_90 = float(df['Cotovelo_90'][12])*Cotovelo_90Q
        dn_150_Cotovelo_45= float(df['Cotovelo_45'][12])* Cotovelo_45Q
        dn_150_Cotovelo_Saida_Lateral= float(df['Cotovelo_Saida_Lateral'][12])*Cotovelo_Saida_LateralQ
        dn_150_Curva_90 = float(df['Curva_90'][12])*Curva_90Q	
        dn_150_Curva_90_Femea= float(df['Curva_90_Femea'][12])*Curva_90_FemeaQ
        dn_150_Curva_90_Macho_Femea= float(df['Curva_90_Macho_Femea'][12])*Curva_90_Macho_FemeaQ
        dn_150_Curva_90_Macho= float(df['Curva_90_Macho'][12])*Curva_90_MachoQ
        dn_150_Curva_45= float(df['Curva_45'][12])*Curva_45Q
        dn_150_Transposicao= float(df['Transposicao'][12])*TransposicaoQ
        dn_150_TE_Direto= float(df['TE_Direto'][12])* TE_DiretoQ	
        dn_150_T_Perpendicular= float(df['T_Perpendicular'][12])* T_PerpendicularQ		
        dn_150_T_Direto_45= float(df['T_Direto_45'][12])*T_Direto_45Q 	
        dn_150_T_Perpendicular_45= float(df['T_Perpendicular_45'][12])*T_Perpendicular_45Q		
        dn_150_Cruzeta_Perpendicular= float(df['Cruzeta_Perpendicular'][12])*Cruzeta_PerpendicularQ	
        dn_150_T_Curva_Dupla_Saida= float(df['T_Curva_Dupla_Saida'][12])*T_Curva_Dupla_SaidaQ	
        dn_150_T_Curva_Dupla_Entrada= float(df['T_Curva_Dupla_Entrada'][12])*T_Curva_Dupla_EntradaQ	
        dn_150_Luvas= float(df['Luvas'][12])*LuvasQ		
        dn_150_Uniao_Flange_Ovais= float(df['Uniao_Flange_Ovais'][12])*Uniao_Flange_OvaisQ	
        dn_150_Valvula_PE= float(df['Valvula_PE'][12])*Valvula_PEQ	
        dn_150_Valvula_Retencao_Horizontal= float(df['Valvula_Retencao_Horizontal'][12])*Valvula_Retencao_HorizontalQ	
        dn_150_Valvula_Retencao_Vertical= float(df['Valvula_Retencao_Vertical'][12])*Valvula_Retencao_VerticalQ	
        dn_150_RG_Esfera= float(df['RG_Esfera'][12])*RG_EsferaQ	
        dn_150_RG_Gaveta= float(df['RG_Gaveta'][12])*RG_GavetaQ	
        dn_150_RG_Pressao= float(df['RG_Pressao'][12])*RG_PressaoQ	
        dn_150_RG_Angular= float(df['RG_Angular'][12])*RG_AngularQ		
        dn_150_Entrada_Normal= float(df['Entrada_Normal'][12])*Entrada_NormalQ	
        dn_150_Entrada_Borda= float(df['Entrada_Borda'][12])*Entrada_BordaQ	
        dn_150_Saida_Canalizacao= float(df['Saida_Canalizacao'][12])*Saida_CanalizacaoQ
        dn_150_Reducao= float(df['Perda_Carga_Reducao'][12])*ReducaoQ

        equi_150 = {
            'Conexão':[dn_150_Cotovelo_90,	
                            dn_150_Cotovelo_45,	
                            dn_150_Cotovelo_Saida_Lateral,	
                            dn_150_Curva_90,	
                            dn_150_Curva_90_Femea,	
                            dn_150_Curva_90_Macho_Femea,	
                            dn_150_Curva_90_Macho,	
                            dn_150_Curva_45,		
                            dn_150_Transposicao,	
                            dn_150_TE_Direto,	
                            dn_150_T_Perpendicular,		
                            dn_150_T_Direto_45,	
                            dn_150_T_Perpendicular_45,	
                            dn_150_Cruzeta_Perpendicular,	
                            dn_150_T_Curva_Dupla_Saida,	
                            dn_150_T_Curva_Dupla_Entrada,	
                            dn_150_Luvas,	
                            dn_150_Uniao_Flange_Ovais,	
                            dn_150_Valvula_PE,	
                            dn_150_Valvula_Retencao_Horizontal,	
                            dn_150_Valvula_Retencao_Vertical,	
                            dn_150_RG_Esfera,	
                            dn_150_RG_Gaveta,	
                            dn_150_RG_Pressao,	
                            dn_150_RG_Angular,	
                            dn_150_Entrada_Normal,	
                            dn_150_Entrada_Borda,	
                            dn_150_Saida_Canalizacao,
                            dn_150_Reducao,
                    ]
                }

        df_150= pd.DataFrame(equi_150)
        SR_150 = pd.Series(df_150['Conexão'])
        EQ_150 = SR_150.sum()

    #######44444########## criar um dataframe com esses valores, de EQ_150 que possam ser buscados novamente quando fizer o load
        comp_eq_ferro_dn = [
                           EQ_13,
                           EQ_19,
                           EQ_25,
                           EQ_32,
                           EQ_38,
                           EQ_50,
                           EQ_63,
                           EQ_75,
                           EQ_100,
                           EQ_125,
                           EQ_150
                        ]
                        
        return(comp_eq_ferro_dn)

    def vazao_trecho(self, velocidade):
        
        # Pesos

        BA = self.TX_P_BA.value()
        BD = self.TX_P_BD.value()
        VSC = self.TX_P_VSC.value()
        VSVD = self.TX_P_VSVD.value()
        CH = self.TX_P_CH.value()
        LV = self.TX_P_LV.value()
        MIC = self.TX_P_MIC.value()
        DH = self.TX_P_DH.value()
        MICS = self.TX_P_MICS.value()
        MICC = self.TX_P_MICC.value()
        TQ = self.TX_P_TQ.value()
        LR = self.TX_P_LR.value()
        TL = self.TX_P_TL.value()
        PIA = self.TX_P_PIA_2.value()
        LP = self.TX_P_LP.value()
        PIAE = self.TX_P_PIAE.value()
        BE = self.TX_P_BE.value()

        # Qtda
        BAQ = self.TX_Q_BA.value()
        BDQ = self.TX_Q_BD.value()
        VSCQ = self.TX_Q_VS.value()
        VSVDQ = self.TX_Q_VSVD.value()
        CHQ = self.TX_Q_CH.value()
        LVQ = self.TX_Q_LV.value()
        MICQ = self.TX_Q_MIC.value()
        DHQ = self.TX_Q_DH.value()
        MICSQ = self.TX_Q_MICS.value()
        MICCQ = self.TX_Q_MICC.value()
        TQQ = self.TX_Q_TQ.value()
        LRQ = self.TX_Q_LR.value()
        TLQ = self.TX_Q_TL.value()
        PIAQ = self.TX_Q_PIA.value()
        LPQ = self.TX_Q_LP.value()
        PIAEQ = self.TX_Q_PIAE.value()
        BEQ = self.TX_Q_BE.value()

        Vazao_Pesos = { 'Pesos':[BA,BD,VSC,VSVD,CH,LV,MIC,DH,MICS,MICC,TQ,LR,TL,PIA,LP,PIAE,BE],
                          'Qtda': [BAQ,BDQ,VSCQ,VSVDQ,CHQ,LVQ,MICQ,DHQ,MICSQ,MICCQ,TQQ,LRQ,TLQ,PIAQ,LPQ,PIAEQ,BEQ]

                                    }
        

        df_Total_Pesos = pd.DataFrame(Vazao_Pesos)

        # Este processo cria série com os dados das colunas multiplica e depois incorpora no dataframe
        Pesos_SR = pd.Series(df_Total_Pesos['Pesos'])
        Qtda_SR = pd.Series(df_Total_Pesos['Qtda'])
        Total_Pesos = Pesos_SR * Qtda_SR
        df_Total_Pesos['Total'] = Total_Pesos
        Pesos_Soma = df_Total_Pesos['Total'].sum()

        Vazao_Pesos = 0.3*(Pesos_Soma)**0.5

        if self.CK_INSERIR_VAZAO.isChecked() == True:
            vazao_trecho = self.SP_Vazao_Trecho.value()
            print('usou vazao especifica')
        else:
            vazao_trecho = Vazao_Pesos
            print('usou vazao dos pesso')

        

        
        Diametro_Calculado = (((4*(vazao_trecho/1000))/(3.14*velocidade))**0.5)*1000
        print('D calculado no calc hid:',Diametro_Calculado)

        # Diametro calculado tem que sair em mm
        

        return(vazao_trecho, Diametro_Calculado)

# FUNÇÃO INSERIR TRECHO
    def add_linha(self):
        
        # interrompe o calculo se falhar a ativação
        if self.acesso_permitido == False:
            self.aviso_acesso_negado()
            return

        #avisos que interrompem a função inserir dados revisão de dados de entrada 
        aviso_continuidade_errada = self.aviso_continuidade_errada()
        interromper = self.verificacao_suficiencia_dados()
        if interromper == True or aviso_continuidade_errada == True:

            self.exibir_aviso()
            return


        # ENTRADA DE DADOS

        pressao_necessaria = self.SP_pressao_nec_trecho.value()
        Nome = self.tx_Nome.toPlainText()
        Nome = Nome.strip().upper() # converte para maiúsculas e remove espaços

        h_reservoir = 0
        self.SP_velocidade.setValue(2.5)
        Velocidade_Max = self.SP_velocidade.value() #V
        Origem = self.CB_Origem_2.currentText()
        Altura = self.SP_Altura_Trecho.value() # h
        Comprimento = self.SP_Comprimento.value()  # L
        Temperatura = self.Slider_Valor() # temp  

        
        vazao_trecho = self.vazao_trecho(Velocidade_Max)
        diametro_calculado = vazao_trecho[1]
        vazao = vazao_trecho[0]


        resultado_d_PVC = self.Diametro_interno_PVC(diametro_calculado)

        diametro_PVC= resultado_d_PVC[0]
        diametro_PVC_DN = resultado_d_PVC[2]
        print('DN PVC:', diametro_PVC_DN)

        if diametro_calculado > diametro_PVC:
            # função que calcula a velocidade procurar onde está
            velocidade_calculada = self.velocidade_calculada(vazao, diametro_PVC)
            velocidade_calculada = round(velocidade_calculada,2)
            self.SP_velocidade.setValue(velocidade_calculada)


        comprimento_eq_PVC = self.Comprimento_Equivalente(diametro_PVC)[0]
        #dataframe conexões
        df_conex_PVC = self.Comprimento_Equivalente(diametro_PVC)[1]


        resultado_d_ferro = self.Diametro_interno_FERRO(diametro_calculado)

        diametro_FERRO= resultado_d_ferro[0]
        diametro_FERRO_DN = resultado_d_ferro[2]
        print('DN ferro:', diametro_FERRO_DN)

        if diametro_calculado > diametro_FERRO:
            # função que calcula a velocidade procurar onde está
            velocidade_calculada = self.velocidade_calculada(vazao, diametro_FERRO)
            velocidade_calculada = round(velocidade_calculada,2)
            self.SP_velocidade.setValue(velocidade_calculada)


        comprimento_eq_FERRO = self.Comprimento_Equivalente_Fe(diametro_FERRO)[0]
        #daframe conexões
        df_conex_FERRO = self.Comprimento_Equivalente_Fe(diametro_FERRO)[1]

        Velocidade_Max = self.SP_velocidade.value()
        Material = self.CB_Material.currentText()

        if Material == "PVC" or Material == "Cobre" or Material == "Latão" or Material == "Vidro":
            comprimento_eq = comprimento_eq_PVC
            diametro = diametro_PVC
            diametro_DN = diametro_PVC_DN
            df_conex = df_conex_PVC
            
        else:
            comprimento_eq = comprimento_eq_FERRO
            diametro = diametro_FERRO
            diametro_DN = diametro_FERRO_DN 
            df_conex = df_conex_FERRO
        
        comprimento_total = Comprimento + comprimento_eq 
       
        perda_de_carga = self.Equacao_Universal( Velocidade_Max,Temperatura,comprimento_total, Material,diametro)

        trecho_continuo = Origem in self.df['Trecho'].values

    
        if trecho_continuo == True:

            indice_origem = self.df.loc[self.df['Trecho'] == Origem].index[0]
            Perda_acumulada = float(self.df['Dh[mca]'][indice_origem]) + perda_de_carga
            perda_de_carga = perda_de_carga + Perda_acumulada
        
        pressao_disp = h_reservoir - Altura - perda_de_carga
        pressao_resultante = round(pressao_disp - pressao_necessaria, 2)

        existe_valor = Nome in self.df['Trecho'].values
        
        if existe_valor == True:
            # PERGUNTA SE QUER SUBSTITUIR O TRECHO EXISTENTE
            interromperSub = self.exibir_confirmacao()
            if interromperSub == True:

                indice = self.df.loc[self.df['Trecho'] == Nome].index[0]

                trecho_novo = {'Trecho': Nome,
                        'Origem': Origem,
                        'Mat': Material,
                        'DN[mm]': diametro_DN,
                        'Di[mm]': diametro, 
                        'L[m]': Comprimento, 
                        'L eq[m]': round(comprimento_eq,2), 
                        'L tot[m]': round(comprimento_total,2), 
                        'h[m]':Altura, 
                        'V[m/s]': Velocidade_Max,
                        'Q[L/s]':round(vazao,2),
                        'Dh[mca]': round(perda_de_carga,3), 
                        'P disp[mca]': round(pressao_disp,2), 
                        'temp[°C]':Temperatura,
                        'P nec[mca]':pressao_necessaria,
                        'P res[mca]':pressao_resultante
                        }
                # tentativa de substituir linha usando a posição index existente
                self.df.loc[indice] = trecho_novo
                #-------------------------------------------------------------------------
                # isso adiciona o nome do trecho ao dataframe de equivalente 
       

                # isso acha o indice do datafram que tem o nome do trecho 
                indice_eq = self.df_comp_eq_pvc.loc[self.df_comp_eq_pvc[0] == Nome].index[0]
                print('indice do dataframe comp equivalente', indice_eq)
                indice_eq_fe = self.df_comp_eq_fe.loc[self.df_comp_eq_fe[0] == Nome].index[0]
                # isso captura a lista na def de comprimento 
                lista_eq_pvc = self.Comprimento_tabview_PVC(50)[1] # aqui coloca-se qualquer diâmetro pois isso não interfere no cálculo
                lista_eq_fe = self.Comprimento_tabview_Fe(50)[1] # aqui coloca-se qualquer diâmetro por isso não interefer no cálculo
                print('lista de comprimento equivalente', lista_eq_pvc)

                # isso substitui o dataframe existente pelo novo 

                self.df_comp_eq_pvc.loc[indice_eq + 1] = lista_eq_pvc
                self.df_comp_eq_fe.loc[indice_eq_fe + 1] = lista_eq_fe
                
            else:
                return
        else:
            self.tx_Nome.setStyleSheet('background-color: white;')

            if Nome:
                trecho = {'Trecho': Nome,
                    'Origem': Origem,
                    'Mat': Material,
                    'DN[mm]': diametro_DN,
                    'Di[mm]': diametro,  
                    'L[m]': Comprimento, 
                    'L eq[m]': round(comprimento_eq,2), 
                    'L tot[m]': round(comprimento_total,2), 
                    'h[m]':Altura, 
                    'V[m/s]': Velocidade_Max,
                    'Q[L/s]':round(vazao,2),
                    'Dh[mca]': round(perda_de_carga,3), 
                    'P disp[mca]': round(pressao_disp,2), 
                    'temp[°C]':Temperatura,
                    'P nec[mca]':pressao_necessaria,
                    'P res[mca]':pressao_resultante
                    }
                
                # chamar verificação dos campos aqui
            
                self.df = pd.concat([self.df, pd.DataFrame([trecho])], ignore_index=True)
                
                self.model = DataFrameModel(self.df) 
                self.tableview.setModel(self.model)


                self.combo_delegate = ComboBoxDelegate_origem(self)
                self.tableview.setItemDelegateForColumn(1, self.combo_delegate)
                self.combo_delegate = ComboBoxDelegate(self)
                self.tableview.setItemDelegateForColumn(3, self.combo_delegate)

                self.tableview.resizeColumnsToContents()

                self.model.layoutChanged.emit()
                self.sinal_atualizar_dataframe =  QtCore.Signal(DataFrameModel(self.df))
                #------------------- fim do dataframe principal que alimenta a tabela 
                #------- aqui começa o datarame de equivalentes 

                # isso adiciona o nome do trecho ao dataframe de equivalente 


                # isso captura a lista na def de comprimento 
                lista_eq_pvc = self.Comprimento_tabview_PVC()
                lista_eq_fe = self.Comprimento_tabview_Fe()  # diametro de 50 é genérico não influi no cálculo é apenas para ter uma variável 
                print('lista de comprimento equivalente', lista_eq_pvc)

                self.df_comp_eq_pvc = pd.concat([self.df_comp_eq_pvc, pd.DataFrame([Nome])], ignore_index=True)

                self.df_comp_eq_fe = pd.concat([self.df_comp_eq_fe, pd.DataFrame([Nome])], ignore_index=True)


                # isso substitui o dataframe existente pelo novo 
                self.df_comp_eq_pvc = pd.concat([self.df_comp_eq_pvc, pd.DataFrame([lista_eq_pvc])], ignore_index=True)

                self.df_comp_eq_fe = pd.concat([self.df_comp_eq_fe, pd.DataFrame([lista_eq_fe])], ignore_index=True)

                print(self.df_comp_eq_pvc)
             
        print(self.df)       
        self.aviso_confirm()
        self.limpar_campos()
        self.combobox_origem()
    
        return

    
    def combobox_dn(self, row_value):

        if row_value == "PVC" or row_value == 'Cobre' or row_value == 'Latão':

            df = self.df_PVC
            diametro_nominal = df['Diametro_Nominal'].astype(str).tolist()
            
        else:
         
            df = self.df_FERRO
            diametro_nominal = df['Diametro_Nominal'].astype(str).tolist()
            diametro_nominal = [valor for valor in diametro_nominal if valor != '0']
           
        return diametro_nominal
    
    def combobox_origem(self):

    
        reservoir = 'Reservatório'
        if self.df['Trecho'].isna().all():
            self.CB_Origem_2.addItems([reservoir])

        else:

            self.CB_Origem_2.clear()
            self.CB_Origem_2.addItems([reservoir])
            existe_reservoir = reservoir in self.df['Origem']

            if existe_reservoir == True:
                origem = self.df['Trecho'].tolist() # onverter a coluna do dataframe em lista 
                self.CB_Origem_2.addItems(origem) # atribui a lista ao combobox
            
            if existe_reservoir == False:
            
                origem = self.df['Trecho'].tolist() # onverter a coluna do dataframe em lista 
                self.CB_Origem_2.addItems(origem) # atribui a lista ao combobox
        return
    
    def combobox_tabview_origem_lista(self):
        origem = self.df['Trecho'].astype(str).tolist()
        return origem
        
    def combobox_material(self):
        self.CB_Material.addItems(["Selecione o material",
                                   "PVC",
                                   "Cobre",
                                   "Latão",
                                   "FoFo",
                                   "Aço_Galvanizado",
                                   "Aço_Inoxidável",
                                   ])
   
    def Equacao_Universal(self, Velocidade ,Temperatura_agua, Comprimento_tubo, Material_Tubo,Diametro_Tubo):

        df = pd.read_excel(r"T:\MEUS CODIGOS\venv\tabs\Tabela_Diametro_Equivalente.xlsx", sheet_name="TABELA_PROPRIEDADE_AGUA")

        if Temperatura_agua == 0: Linha_Temperatura = 0
        if Temperatura_agua == 5: Linha_Temperatura = 1
        if Temperatura_agua == 10: Linha_Temperatura = 2
        if Temperatura_agua == 15: Linha_Temperatura = 3
        if Temperatura_agua == 20: Linha_Temperatura = 4
        if Temperatura_agua == 25: Linha_Temperatura = 5
        if Temperatura_agua == 30: Linha_Temperatura = 6
        if Temperatura_agua == 40: Linha_Temperatura = 7
        if Temperatura_agua == 50: Linha_Temperatura = 8
        if Temperatura_agua == 60: Linha_Temperatura = 9
        if Temperatura_agua == 70: Linha_Temperatura = 10
        if Temperatura_agua == 80: Linha_Temperatura = 11
        if Temperatura_agua == 90: Linha_Temperatura = 12
        if Temperatura_agua == 100: Linha_Temperatura = 13

        if Material_Tubo == 'PVC': Linha_Rugosidade = 0
        if Material_Tubo == 'Vidro': Linha_Rugosidade = 1
        if Material_Tubo == 'Concreto': Linha_Rugosidade = 2
        if Material_Tubo == 'Madeira': Linha_Rugosidade = 3
        if Material_Tubo == 'Borracha_Alisada': Linha_Rugosidade = 4
        if Material_Tubo == 'Cobre': Linha_Rugosidade = 5
        if Material_Tubo == 'Latão': Linha_Rugosidade = 6
        if Material_Tubo == 'FoFo': Linha_Rugosidade = 7
        if Material_Tubo == 'Aço_Galvanizado': Linha_Rugosidade = 8
        if Material_Tubo == 'Ferro_Forjado': Linha_Rugosidade = 9
        if Material_Tubo == 'Aço_Inoxidável': Linha_Rugosidade = 10
        if Material_Tubo == 'Aço_Comercial': Linha_Rugosidade = 11

        Fator_Rugosidade = float(df['Fator_Rugosidade'][Linha_Rugosidade])
        Massa_Especifica = float(df['Massa_Especifica'][Linha_Temperatura])
        Viscosidade_Dinamica = float(df['Viscosidade_Dinamica'][Linha_Temperatura])

        #Viscosidade dinamica[kg/m.s] 1cp = 1/1000
        #massa especifica [kg/m³]
        # Diametro em [mm]
        # Vazão entra em [L/s] converte para [m³/s]
        # Velocidade em [m/s]
        # perda de carga em mca

        # ________________isso eu vou tirar de uma função pronta, dado de entrada

        #_______________encerra 
        #di interno tem que retornar em mm
    
        N_Reynold = ((Diametro_Tubo/1000) * Velocidade * Massa_Especifica / Viscosidade_Dinamica)
        print('diametro tubo N reynolds:', Diametro_Tubo)
        print('N Reynolds:', N_Reynold)

    #REGIME DE ESCOAMENTO
        print('fator rugosidade:', Fator_Rugosidade)
        fator_atrito_inicial = float(0.00001)
        precisao_calculo = 0.01
        fator_atrito_adicional_loop = float(0.00001) 

        Fator_Atrito_limite_14 = float((14.14/(N_Reynold*(Fator_Rugosidade/(Diametro_Tubo))))**0.5)
        Fator_Atrito_limite_198 = float((198/(N_Reynold*(Fator_Rugosidade/(Diametro_Tubo))))**0.5)

        # Regime Laminar
        Fator_Atrito_Laminar = 64 / N_Reynold

        # Regime Transitório

        Fator_Atrito_Transitorio = float((((64/N_Reynold) ** 8) + 9.5 * (math.log(Fator_Rugosidade/(3.7 * Diametro_Tubo) + 5.74 / (N_Reynold ** 0.9)) - (2500/ N_Reynold) ** 6) ** -16) ** 0.125)

        print('REGIME TRANSITÓRIO OK')

        # Regime turbulento liso

        Fator_Atrito_Turbulento_Liso = fator_atrito_inicial
        LDE_1 = float(1/(Fator_Atrito_Turbulento_Liso ** 0.5))
        LDD_1 = float((2*(math.log(N_Reynold*Fator_Atrito_Turbulento_Liso**0.5)))-0.8)

        while abs((LDD_1-LDE_1)/LDD_1)>=precisao_calculo:
            Fator_Atrito_Turbulento_Liso += fator_atrito_adicional_loop
            LDE_1 = float(1/(Fator_Atrito_Turbulento_Liso ** 0.5)) 
            LDD_1 = (2*(math.log(N_Reynold*Fator_Atrito_Turbulento_Liso**0.5)))-0.8

        print('REGIME TURBULENTO LISO OK')

        #Regime turbulento transitório
        Fator_Atrito_Turbulento_Transitorio = fator_atrito_inicial

        LDE_2 = float(1/(Fator_Atrito_Transitorio ** 0.5))
        LDD_2=  -2.0 * math.log((Fator_Rugosidade/(3.7 * (Diametro_Tubo))) + (2.51/((N_Reynold * Fator_Atrito_Turbulento_Transitorio ** 0.5))))

        while abs((LDD_2-LDE_2)/LDD_2)>=precisao_calculo:

            Fator_Atrito_Turbulento_Transitorio += fator_atrito_adicional_loop
            LDE_2 = float(1/(Fator_Atrito_Turbulento_Transitorio ** 0.5))
            LDD_2=  float(-2.0 * math.log((Fator_Rugosidade/(3.7 * (Diametro_Tubo))) + (2.51/((N_Reynold * Fator_Atrito_Turbulento_Transitorio ** 0.5)))))
            print(' :',Fator_Atrito_Turbulento_Transitorio,' LDD2: ',LDD_2,'LDE2: ', LDE_2)
        
        print('REGIME TURBULENTO TRANSITÓRIO OK')

        # Regime turnbulento rugoso

        Fator_Atrito_Turbulento_Rugoso = fator_atrito_inicial

        LDE_3= float(1/(Fator_Atrito_Turbulento_Rugoso ** 0.5))
        LDD_3= 1.74 -2 * math.log(2 * Fator_Rugosidade / (3.71 * Diametro_Tubo) + 2.51 / (N_Reynold * Fator_Atrito_Turbulento_Rugoso ** 0.5))

        while abs((LDD_3-LDE_3)/LDD_3)>=precisao_calculo:

            Fator_Atrito_Turbulento_Rugoso += fator_atrito_adicional_loop

            LDE_3 = float(1/(Fator_Atrito_Turbulento_Rugoso ** 0.5))
            LDD_3 = 1.74 -2 * math.log(2 * Fator_Rugosidade / (3.71 * Diametro_Tubo) + 2.51 / (N_Reynold * Fator_Atrito_Turbulento_Rugoso ** 0.5))
        
        print('REGIME TURBULENTO RUGOSO OK')

        print('Laminar: ', Fator_Atrito_Laminar)
        print('Transitório: ', Fator_Atrito_Transitorio)
        print('Turbulento liso: ', Fator_Atrito_Turbulento_Liso, 'LDE:',LDE_1,'LDD:',LDD_1)
        print('Turbulento transitório: ', Fator_Atrito_Turbulento_Transitorio, 'LDE:',LDE_2,'LDD:',LDD_2)
        print('Turbulento Rugoso: ', Fator_Atrito_Turbulento_Rugoso, 'LDE:',LDE_3,'LDD:',LDD_3)
    

        if N_Reynold < 2000:
            Fator_Atrito = Fator_Atrito_Laminar
        if N_Reynold >= 2000 and N_Reynold <= 4000:
            Fator_Atrito = Fator_Atrito_Transitorio
        if N_Reynold > 4000 and Fator_Atrito_Turbulento_Liso >= Fator_Atrito_limite_14 and Fator_Atrito_Turbulento_Liso <= Fator_Atrito_limite_198:
            Fator_Atrito = Fator_Atrito_Turbulento_Liso
        else:
            Fator_Atrito = Fator_Atrito_Turbulento_Rugoso

        print('Fator de Atrito: ', Fator_Atrito, 'Reynolds: ', N_Reynold, 'Fator limite 14.14: ',Fator_Atrito_limite_14,' Fator limite 198: ', Fator_Atrito_limite_198)

        print('Material Tubo eq universal:', Material_Tubo)

        # Calculo da equação universal
        # a gravidade na terra varia entre 9,76 e 9,83 m/s²
        Gravidade = 9.81 
        perda_de_carga = Fator_Atrito * (Comprimento_tubo/(Diametro_Tubo/1000)) * ((Velocidade ** 2) / (2 * Gravidade))
        

        return (perda_de_carga)
    
    def Diametro_interno_PVC(self, Diametro_Calculado):

        df = self.df_PVC        

        # isso tem que achar o dimametro max e se o calculado for maior usa o máximo
        diametro_maximo = np.max(df['Diametro_Interno'])
        print('diametro interno maximo:', diametro_maximo)
        if Diametro_Calculado > diametro_maximo:
            Diametro_Calculado = diametro_maximo

        df_di = df.loc[(df['Diametro_Interno']>= Diametro_Calculado)]
        diametro = np.min(df_di['Diametro_Interno'])

        linha_total = df[df.columns[0]].count()
        linha_subt = df_di[df_di.columns[0]].count()
        Linha_ref = linha_total - linha_subt

        diametro_nominal = df['Diametro_Nominal'][Linha_ref]

        print('LINHA SUBT:',linha_subt)
        print('LINHA REF:',Linha_ref)

        print('Di pvc:',diametro)
        # tem que sair o diametro interno em mm
        return diametro, Linha_ref,diametro_nominal
  
    def Diametro_interno_FERRO(self, Diametro_Calculado):
        
        df = self.df_FERRO
  
        diametro_maximo = np.max(df['Diametro_Interno'])
        print('diametro interno maximo:', diametro_maximo)
        if Diametro_Calculado > diametro_maximo:
            Diametro_Calculado = diametro_maximo

        df_di = df.loc[(df['Diametro_Interno']>= Diametro_Calculado)]
        diametro= np.min(df_di['Diametro_Interno'])

        linha_total = df[df.columns[0]].count()
        linha_subt = df_di[df_di.columns[0]].count()
        Linha_ref= linha_total - linha_subt

        diametro_nominal = df['Diametro_Nominal'][Linha_ref]


        return diametro, Linha_ref,diametro_nominal

    def limpar_campos(self):
        ########
        self.tx_Nome.clear()
        #self.CB_Origem_2.clear()
        self.SP_Altura_Trecho.clear()
        self.SP_Comprimento.clear()
        self.SP_pressao_nec_trecho.clear()

        # PVC CONEXÕES  
        self.SP_COT90.clear()	
        self.SP_COT45.clear()
        self.SP_CURV90.clear()
        self.SP_CURV45.clear()	
        self.SP_TDIR.clear()
        self.SP_TLAT.clear()	
        self.SP_VALV_PE.clear()	
        self.SP_VALV_H.clear()
        self.SP_VALV_V.clear()	
        self.spinBox_3.clear()	
        self.SP_RG_GAV.clear()	
        self.SP_RG_RP.clear()	
        self.SP_RG_ANG.clear()
        self.SP_ENTRADA_N.clear()	
        self.SP_ENTRADA_B.clear()
        self.SP_ENTRADA_SC.clear()

        # FERRO CONEXÕES 
        self.SP_COT90_F.clear()
        self.SP_COT45_F.clear()	
        self.SP_COT90_SLat_F.clear()	
        self.SP_CURV90_F.clear()	
        self.SP_CURV90_Fem_F.clear()
        self.SP_CURV90_MF_F.clear()	
        self.SP_CURV90_M_F.clear()
        self.SP_CURV45_F.clear()	
        self.SP_VALV_H_30.clear()	
        self.SP_TDIR_4.clear()
        self.SP_TLAT_4.clear()	
        self.SP_VALV_H_32.clear()	
        self.SP_VALV_H_33.clear()		
        self.SP_VALV_H_31.clear()	
        self.SP_VALV_H_34.clear()
        self.SP_VALV_H_35.clear()
        self.SP_VALV_H_36.clear()		
        self.SP_VALV_H_37.clear()	
        self.SP_VALV_PE_F.clear()
        self.SP_VALV_H_25.clear()	
        self.SP_VALV_V_4.clear()
        self.SP_RG_ESF_F.clear()	
        self.SP_RG_GAV_F.clear()	
        self.SP_RG_RP_F.clear()	
        self.SP_RG_ANG_F.clear()
        self.SP_ENTRADA_N_F.clear()	
        self.SP_ENTRADA_B_F.clear()	
        self.SP_ENTRADA_SC_F.clear()
        self.SP_TE_Red_12.clear()

        # VAZAO 
        self.TX_Q_BA.value()
        self.TX_Q_BD.value()
        self.TX_Q_VS.value()
        self.TX_Q_VSVD.value()
        self.TX_Q_CH.value()
        self.TX_Q_LV.value()
        self.TX_Q_MIC.value()
        self.TX_Q_DH.value()
        self.TX_Q_MICS.value()
        self.TX_Q_MICC.value()
        self.TX_Q_TQ.value()
        self.TX_Q_LR.value()
        self.TX_Q_TL.value()
        self.TX_Q_PIA.value()
        self.TX_Q_LP.value()
        self.TX_Q_PIAE.value()
        self.TX_Q_BE.value()

    def limpar_conexões(self):
                # PVC CONEXÕES  
        self.SP_COT90.clear()	
        self.SP_COT45.clear()
        self.SP_CURV90.clear()
        self.SP_CURV45.clear()	
        self.SP_TDIR.clear()
        self.SP_TLAT.clear()	
        self.SP_VALV_PE.clear()	
        self.SP_VALV_H.clear()
        self.SP_VALV_V.clear()	
        self.spinBox_3.clear()	
        self.SP_RG_GAV.clear()	
        self.SP_RG_RP.clear()	
        self.SP_RG_ANG.clear()
        self.SP_ENTRADA_N.clear()	
        self.SP_ENTRADA_B.clear()
        self.SP_ENTRADA_SC.clear()

        # FERRO CONEXÕES 
        self.SP_COT90_F.clear()
        self.SP_COT45_F.clear()	
        self.SP_COT90_SLat_F.clear()	
        self.SP_CURV90_F.clear()	
        self.SP_CURV90_Fem_F.clear()
        self.SP_CURV90_MF_F.clear()	
        self.SP_CURV90_M_F.clear()
        self.SP_CURV45_F.clear()	
        self.SP_VALV_H_30.clear()	
        self.SP_TDIR_4.clear()
        self.SP_TLAT_4.clear()	
        self.SP_VALV_H_32.clear()	
        self.SP_VALV_H_33.clear()		
        self.SP_VALV_H_31.clear()	
        self.SP_VALV_H_34.clear()
        self.SP_VALV_H_35.clear()
        self.SP_VALV_H_36.clear()		
        self.SP_VALV_H_37.clear()	
        self.SP_VALV_PE_F.clear()
        self.SP_VALV_H_25.clear()	
        self.SP_VALV_V_4.clear()
        self.SP_RG_ESF_F.clear()	
        self.SP_RG_GAV_F.clear()	
        self.SP_RG_RP_F.clear()	
        self.SP_RG_ANG_F.clear()
        self.SP_ENTRADA_N_F.clear()	
        self.SP_ENTRADA_B_F.clear()	
        self.SP_ENTRADA_SC_F.clear()
        self.SP_TE_Red_12.clear()



#AVISOS
    def verificacao_suficiencia_dados(self):

        nomev = self.tx_Nome.toPlainText()
        comprimentov = self.SP_Comprimento.value()
        velocidadev = self.SP_velocidade.value()
        vazaov = self.SP_Vazao_Trecho.value()

        BAv = self.TX_P_BA.value()
        BDv = self.TX_P_BD.value()
        VSCv = self.TX_P_VSC.value()
        VSVDv = self.TX_P_VSVD.value()
        CHv = self.TX_P_CH.value()
        LVv = self.TX_P_LV.value()
        MICv = self.TX_P_MIC.value()
        DHv = self.TX_P_DH.value()
        MICSv = self.TX_P_MICS.value()
        MICCv = self.TX_P_MICC.value()
        TQv = self.TX_P_TQ.value()
        LRv = self.TX_P_LR.value()
        TLv = self.TX_P_TL.value()
        PIAv = self.TX_P_PIA_2.value()
        LPv = self.TX_P_LP.value()
        PIAEv = self.TX_P_PIAE.value()
        BEv = self.TX_P_BE.value()

        # Qtda
        BAQv = self.TX_Q_BA.value()
        BDQv = self.TX_Q_BD.value()
        VSCQv = self.TX_Q_VS.value()
        VSVDQv = self.TX_Q_VSVD.value()
        CHQv = self.TX_Q_CH.value()
        LVQv = self.TX_Q_LV.value()
        MICQv = self.TX_Q_MIC.value()
        DHQv = self.TX_Q_DH.value()
        MICSQv = self.TX_Q_MICS.value()
        MICCQv = self.TX_Q_MICC.value()
        TQQv = self.TX_Q_TQ.value()
        LRQv = self.TX_Q_LR.value()
        TLQv = self.TX_Q_TL.value()
        PIAQv = self.TX_Q_PIA.value()
        LPQv = self.TX_Q_LP.value()
        PIAEQv = self.TX_Q_PIAE.value()
        BEQv = self.TX_Q_BE.value()


        verif_soma = BAQv + BDQv + VSCQv + VSVDQv + CHQv +LVQv +MICQv +DHQv +MICSQv + MICCQv + TQQv + LRQv + TLQv + PIAQv + LPQv + PIAEQv + BEQv   # a soma não está funcionando 

        print('verificação soma:', verif_soma)

        # verifica se tem algum elemento para calcular a vazao
        if verif_soma == 0 and self.CK_INSERIR_VAZAO.isChecked() == False  or nomev == "" or comprimentov == 0 or velocidadev == 0:
            # velocidade ok
            interromper = True

        else:

            if BAQv > 0 and BAv == 0 or BDQv > 0 and BDv == 0 or VSCQv > 0 and VSCv == 0 or VSVDQv > 0 and VSVDv == 0 or CHQv > 0 and CHv == 0 or LVQv > 0 and LVv == 0 or MICQv > 0 and MICv == 0 or DHQv > 0 and DHv == 0 or MICSQv > 0 and MICSv == 0 or MICCQv > 0 and MICCv == 0 or TQQv > 0 and TQv == 0 or LRQv > 0 and LRv == 0 or TLQv > 0 and TLv == 0 or PIAQv > 0 and PIAv == 0 or LPQv > 0 and LPv == 0 or PIAEQv > 0 and PIAEv == 0 or BEQv > 0 and BEv == 0 :    # Esse funciona

                interromper = True

            else:
                
                if self.CK_INSERIR_VAZAO.isChecked() == True and vazaov == 0: # Esse funcionou
                
                    interromper = True
                else:

                    interromper = False

        return interromper

    def exibir_aviso(self):
        # Cria uma instância de QMessageBox
        msgbox_verif_dados = "Há dados importantes faltantes, por favor verifique as informações inseridas"
        
        caixa_aviso = QMessageBox()
        caixa_aviso.setWindowTitle("Aviso")
        caixa_aviso.setText(msgbox_verif_dados)
        caixa_aviso.setIcon(QMessageBox.Information)

        # Exibe a caixa de aviso
        caixa_aviso.exec()

    def aviso_confirm(self):
        # Cria uma instância de QMessageBox
        msgbox_confirmacao = "Atividade realizada sucesso!"
        
        caixa_aviso = QMessageBox()
        caixa_aviso.setWindowTitle("Aviso")
        caixa_aviso.setText(msgbox_confirmacao)
        caixa_aviso.setIcon(QMessageBox.Information)

        # Exibe a caixa de aviso
        caixa_aviso.exec()
    
    def aviso_trecho_existente(self):
        # Cria uma instância de QMessageBox
        msgbox_confirmacao = "O trecho já existe deseja substituir?"
        
        cor_fundo = "background-color: white;"
        caixa_aviso = QMessageBox(self)
        caixa_aviso.setWindowTitle('Aviso')
        caixa_aviso.setText(msgbox_confirmacao)
        caixa_aviso.setStyleSheet(cor_fundo)
        caixa_aviso.question(self, QMessageBox.YesRole | QMessageBox.NoRole)
       
        caixa_aviso.exec()
    
        if caixa_aviso == QMessageBox.YesRole:
            print('Trecho será substituido!')
            interromperSub = True

        else:
            print('Trecho não será substituído!')
            interromperSub = False

        # Exibe a caixa de aviso
       
        return interromperSub

    def aviso_acesso_negado(self):
        # Cria uma instância de QMessageBox
        msgbox_confirmacao = " A licença não é válida, a ativação pode ser feita na aba INFO / Ativação. Insira uma chave válida, ou contate o vendedor"
        
        caixa_aviso = QMessageBox()
        caixa_aviso.setWindowTitle("Aviso")
        caixa_aviso.setText(msgbox_confirmacao)
        caixa_aviso.setIcon(QMessageBox.Warning)

        # Exibe a caixa de aviso
        caixa_aviso.exec()

    def exibir_confirmacao(self):
        mensagem = "O trecho já existe deseja substituir?"

        # Crie uma instância personalizada da caixa de diálogo com uma folha de estilo
        caixa_confirmacao = QMessageBox(self)
        caixa_confirmacao.setWindowTitle("Confirmação")
        caixa_confirmacao.setIcon(QMessageBox.Question)
        caixa_confirmacao.setText(mensagem)

        # Defina a cor do texto da caixa de diálogo
        estilo_texto = "background-color: white;"  # Define a cor do texto como vermelho
        caixa_confirmacao.setStyleSheet(estilo_texto)

        # Adicione botões personalizados (opcional)
        caixa_confirmacao.addButton("Sim", QMessageBox.YesRole)
        caixa_confirmacao.addButton("Não", QMessageBox.NoRole)

        # Exiba a caixa de diálogo
        opcao = caixa_confirmacao.exec()

        if opcao == 0:
            print("Operação continuada.")
            interromperSub = True
        else:
            print("Operação cancelada.")
            interromperSub = False

        print('intrromper',interromperSub)
        print('intrromper',opcao)

        return interromperSub

    def aviso_continuidade_errada(self):  #VERIFICAR SE ESSA DEF ESTÁ LINKADA

        Nome = self.tx_Nome.toPlainText()
        Nome = Nome.strip().upper() # converte para maiúsculas e remove espaços
        Origem = self.CB_Origem_2.currentText()

        if Nome == Origem:
            aviso_trecho = 'O trecho começa e termina no mesmo ponto, verifique a origem correta do trecho'
            interromper_continuidade = True
        else:
            interromper_continuidade = False

        return interromper_continuidade
#    


# OPERAÇÕES NA PLANILHA
    def calcular_dataframe(self):

        #self.recalcular_pressao()
        self.atualizar_qtableview() 
        df = self.df

        h_reservoir = 0
        maior_altura = df['h[m]'].max()
        maior_pressao = df['P disp[mca]'].max()
        print('maior pressao:', maior_pressao)

        menor_pressao = df['P res[mca]'].min()
        print('menor pressao:', menor_pressao)

        h_reservoir = round(abs(menor_pressao),2)
        
        maior_vazao = df['Q[L/s]'].max()
        maior_vazao = maior_vazao*3.6



        self.df_pressurizadora = pd.DataFrame(columns=['Vazão max[m³/h]', 'Pressão manométrica[mca]','h reservatório[m]'])
        
        pressao_manometrica = {'Vazão max[m³/h]': maior_vazao,
            'Pressão manométrica[mca]': h_reservoir,
            'h reservatório[m]': h_reservoir
            }
        
        # chamar verificação dos campos aqui
            
        self.df_pressurizadora = pd.concat([self.df_pressurizadora, pd.DataFrame([pressao_manometrica])], ignore_index=False)
        
        # Use a função concat para alinhar os DataFrames verticalmente
        #self.df_pressurizadora = pd.concat([self.df, self.df_pressurizadora],ignore_index=False)

        self.model = DataFrameModel(self.df_pressurizadora) 
        self.tableview.setModel(self.model)
        self.model.layoutChanged.emit()

        
        
        # PRECISO VERIFICAR ANTES SE A PRESSÃO ATENDE OU NÃO SE NÃO ATENDER PEGAR ADIFERENÇA
        # ADICIONAR A DIF DE PRESSÃO NA TABELA, PEGAR O MÍN DELA PARA CALCULAR A PRESSÃO NEC


        def calcular_valor_linha(row):

            resultado= round(h_reservoir + row['P res[mca]'])

            return resultado
            
        
        for index, row in df.iterrows():
            
            df.at[index, 'P result[mca]'] = calcular_valor_linha(row)

        
        self.SP_reservatorio.setValue(h_reservoir)
        self.SP_vazao_max.setValue(maior_vazao)


        #isso deve atualizar o dataframe
        self.model = DataFrameModel(self.df) 
        self.tableview.setModel(self.model)
        self.model.layoutChanged.emit()

        print(df)
        self.aviso_confirm()
        return(h_reservoir)
    
    def velocidade_calculada(self, vazao, diametro):
        velocidade_calc = 4 * (vazao/1000) / (3.14 * (diametro/1000)**2)
        print("velocidade calculada:", velocidade_calc)
        return velocidade_calc

    def remove_selected_rows(self):

        menssagem = "Será excluído a linha selecionada, talvez seja necessário verificar as origens e recalcular, deseja continuar?"

        # Crie uma instância personalizada da caixa de diálogo com uma folha de estilo
        caixa_confirmacao = QMessageBox(self)
        caixa_confirmacao.setWindowTitle("Confirmação")
        caixa_confirmacao.setIcon(QMessageBox.Question)
        caixa_confirmacao.setText(menssagem)

        # Defina a cor do texto da caixa de diálogo
        estilo_texto = "background-color: white;"  # Define a cor do texto como vermelho
        caixa_confirmacao.setStyleSheet(estilo_texto)

        # Adicione botões personalizados (opcional)
        caixa_confirmacao.addButton("Sim", QMessageBox.YesRole)
        caixa_confirmacao.addButton("Não", QMessageBox.NoRole)

        # Exiba a caixa de diálogo
        opcao = caixa_confirmacao.exec()

        if opcao == 0:
            print("Operação continuada.")

            selected_rows = set(index.row() for index in self.tableview.selectionModel().selectedIndexes())

            # Remover as linhas do DataFrame
            self.df = self.df.drop(selected_rows)

            # Atualizar o modelo da QTableView
            self.model = DataFrameModel(self.df)
            self.tableview.setModel(self.model)
            self.combobox_origem()


    def printar_dataframe(self):
        print(self.df)

    def save_dataframe(self):

        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Exportar tabela", "", "Excel Files (*.xlsx);;All Files (*)", options=options)

        if file_name:
            if file_name.endswith('.xlsx'):
                # Criar um escritor Excel (ExcelWriter)
                writer_file = pd.ExcelWriter(file_name, engine='xlsxwriter')

                # Salvar os DataFrames nas planilhas
                self.df.to_excel(writer_file, sheet_name='Planilha', index=False)
                self.df_comp_eq_pvc.to_excel(writer_file, sheet_name='L_eq_PVC', index=False)
                self.df_comp_eq_fe.to_excel(writer_file, sheet_name='L_eq_FE', index=False)
                self.df_pressurizadora.to_excel(writer_file, sheet_name='Pressão', index=False)

                # Salvar o arquivo Excel
                writer_file._save()

    def save_to_excel(self):

        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Exportar tabela", "", "Excel Files (*.xlsx);;All Files (*)", options=options)

        if file_name:
            if file_name.endswith('.xlsx'):
                # Criar um escritor Excel (ExcelWriter)
                writer_file = pd.ExcelWriter(file_name, engine='xlsxwriter')

                # Salvar os DataFrames nas planilhas
                self.df.to_excel(writer_file, sheet_name='Planilha', index=False)
                self.df_comp_eq_pvc.to_excel(writer_file, sheet_name='L_eq_PVC', index=False)
                self.df_comp_eq_fe.to_excel(writer_file, sheet_name='L_eq_FE', index=False)
                self.df_pressurizadora.to_excel(writer_file, sheet_name='Pressão', index=False)

                # Salvar o arquivo Excel
                writer_file._save()
           # self.status_label.setText(f"DataFrame salvo em: {file_name}")

    def load_dataframe(self):

        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Carregar arquivo Excel", "", "Excel Files (*.xlsx);;All Files (*)", options=options)

        if file_name:
            if file_name.endswith('.xlsx'):
                # Carregar o arquivo Excel em DataFrames
                xls = pd.ExcelFile(file_name)
                self.df = pd.read_excel(xls, sheet_name='Planilha')
                self.df_comp_eq_pvc = pd.read_excel(xls, sheet_name='L_eq_PVC')
                self.df_comp_eq_fe = pd.read_excel(xls, sheet_name='L_eq_FE')
                self.df_pressurizadora = pd.read_excel(xls, sheet_name='Pressão')

                self.model = DataFrameModel(self.df) 
                self.tableview.setModel(self.model)



                self.combo_delegate = ComboBoxDelegate_origem(self)
                self.tableview.setItemDelegateForColumn(1, self.combo_delegate)

                self.combo_delegate = ComboBoxDelegate(self)
                self.tableview.setItemDelegateForColumn(3, self.combo_delegate)


            
            #delegate = LineEditDelegate(self)
            #self.tableview.setItemDelegate(delegate)
            self.reexibir_tabela(self.df_pressurizadora)
            self.model.layoutChanged.emit()

        self.combobox_origem()



            #self.status_label.setText(f"DataFrame carregado de: {file_name}")   
               
    def reexibir_tabela(self, dataframe):
        
        self.model = DataFrameModel(dataframe) 

        self.model.data_changed.connect(self.LB_aviso_plan.setVisible(True))


        layout = QVBoxLayout(self.FR_container_planilha)
        self.tableview = QTableView(self)

        self.tableview.setGeometry(50,50,900,400) 
        self.tableview.setModel(self.model)

        # VERIFICAR SE ISSO É NECESSÁRIO
         
        self.combo_delegate = ComboBoxDelegate_origem(self)
        self.tableview.setItemDelegateForColumn(1, self.combo_delegate)

        self.combo_delegate = ComboBoxDelegate(self)
        self.tableview.setItemDelegateForColumn(3, self.combo_delegate)

        layout.addWidget(self.tableview)
        self.setLayout(layout)

        #CRIA EDIÇÃO NA TABELA 
        #delegate = LineEditDelegate(self)
        #self.tableview.setItemDelegate(delegate)


      
        self.model.layoutChanged.emit()

    def atualizar_qtableview(self):
               
        df = self.df
        h_reservoir = abs(df['P res[mca]'].min())

        def atualizar_valor_linha(row):
            Nome = row['Trecho']
            #COMPRIMENTO EQUIVALENTE TOTAL  'L eq[m]'
            vazao = row['Q[L/s]']
            velocidade = row['V[m/s]']
            temperatura = row['temp[°C]']
            #comprimento = row['L[m]'] + row['L eq[m]']
            material = row['Mat']
            diametro_DN = row['DN[mm]']
            print('DN', diametro_DN)

            #diametro = row['Di[mm]']
            # isso deve atualizar o dataframe



            if material == "PVC" or material == "Cobre" or material == "Latão":
                df2 = self.df_PVC
                diametro = self.dn_di(int(diametro_DN),df2)
                comprimento_equivalente = self.equivalente_total_pvc(int(diametro_DN), Nome)
            else:
                df3 = self.df_FERRO
                diametro = self.dn_di(int(diametro_DN),df3)
                comprimento_equivalente = self.equivalente_total_fe(int(diametro_DN), Nome)

            comprimento = row['L[m]'] + comprimento_equivalente
            
            print('comprimento equivalente', comprimento_equivalente)
            print('diametro interno e: ', diametro)

            velocidade = round(self.velocidade_calculada(vazao, diametro), 2)
            perda_de_carga = self.Equacao_Universal(velocidade, temperatura, comprimento, material, diametro)
            perda_de_carga = round(perda_de_carga,3)

            # Continuidade perda de carga 
            trecho_continuo = row['Origem'] in df['Trecho'].values

            if trecho_continuo == True:

                indice_origem = df.loc[df['Trecho'] == row['Origem']].index[0]
                Perda_acumulada = float(df['Dh[mca]'][indice_origem]) + perda_de_carga
                perda_de_carga = round(perda_de_carga + Perda_acumulada,3)    
            

            # atualiza a nova altura 
            nova_altura = row['h[m]']
            nova_pressao_residual = row['P disp[mca]'] - row['P nec[mca]']
            nova_pressao_resultante = nova_pressao_residual + h_reservoir


            return comprimento, perda_de_carga, nova_altura, nova_pressao_residual, nova_pressao_resultante, diametro, comprimento_equivalente, velocidade
            

        for index, row in df.iterrows():

            # atualizar com os dados editados n tabela ['V[m/s]']

            df.at[index, 'Di[mm]'] = atualizar_valor_linha(row)[5]
            df.at[index, 'V[m/s]'] = atualizar_valor_linha(row)[7]
            df.at[index, 'L eq[m]'] = round(atualizar_valor_linha(row)[6], 2)
            df.at[index, 'L tot[m]'] = round(atualizar_valor_linha(row)[0], 2)
            df.at[index, 'Dh[mca]'] = atualizar_valor_linha(row)[1]
            df.at[index, 'h[m]'] = atualizar_valor_linha(row)[2]
            disp = round((atualizar_valor_linha(row)[1] + atualizar_valor_linha(row)[2])*(-1),3)
            df.at[index, 'P disp[mca]'] = disp
            df.at[index, 'P res[mca]'] = round(atualizar_valor_linha(row)[3],3)
            df.at[index, 'P result[mca]'] = atualizar_valor_linha(row)[4]
        print(df)
       
    
    def dn_di(self, valor_dn, df2):
        d_interno = df2.loc[df2['Diametro_Nominal'] == valor_dn, 'Diametro_Interno'].values
        if len(d_interno) > 0:
            return d_interno[0]
        else:
            return None

    def equivalente_total_pvc(self,diametro, Nome):

        diametro = int(diametro)
        print('diametro trocado equivalente:', diametro)

        df = self.df_comp_eq_pvc
        indice = df.loc[df[0] == Nome].index[0]
        if diametro == 15:
            EQ_calc = int(df.iloc[indice + 1, 0])

        if diametro == 20:
            EQ_calc = int(df.iloc[indice + 1, 1])
            
        if diametro == 25:
            EQ_calc = int(df.iloc[indice + 1, 2])
            
        if diametro == 32:
            EQ_calc = int(df.iloc[indice + 1, 3])
            
        if diametro == 40:
            EQ_calc = int(df.iloc[indice + 1, 4])
            
        if diametro == 50:
            EQ_calc = int(df.iloc[indice + 1, 5])
            
        if diametro == 65:
            EQ_calc = int(df.iloc[indice + 1, 6])
            
        if diametro == 80:
            EQ_calc = int(df.iloc[indice + 1, 7])
            
        if diametro == 110:
            EQ_calc = int(df.iloc[indice + 1, 8])

        return EQ_calc            

    def equivalente_total_fe(self,diametro, Nome):
 
        
        df_fe = self.df_comp_eq_fe
        
        indice_fe = df_fe.loc[df_fe[0] == Nome].index[0]

        # ferro
        if diametro == 13:
            EQ_calc = int(df_fe.iloc[indice_fe + 1, 0])

        if diametro == 19:
            EQ_calc = int(df_fe.iloc[indice_fe + 1, 1])
            
        if diametro == 25:
            EQ_calc = int(df_fe.iloc[indice_fe + 1, 2])
            
        if diametro == 32:
            EQ_calc = int(df_fe.iloc[indice_fe + 1, 3])
            
        if diametro == 38:
            EQ_calc = int(df_fe.iloc[indice_fe + 1, 4])
            
        if diametro == 50:
            EQ_calc = int(df_fe.iloc[indice_fe + 1, 5])
            
        if diametro == 63:
            EQ_calc = int(df_fe.iloc[indice_fe + 1, 6])
            
        if diametro == 75:
            EQ_calc = int(df_fe.iloc[indice_fe + 1, 7])
            
        if diametro == 100:
            EQ_calc = int(df_fe.iloc[indice_fe + 1, 8])

        if diametro == 125:
            EQ_calc = int(df_fe.iloc[indice_fe + 1, 9])

        if diametro == 150:
            EQ_calc = int(df_fe.iloc[indice_fe + 1, 10])



        return EQ_calc            

        
# ANIMAÇÃO INTERFACE GRÁFICA
    def LeftMenu(self):
        width = self.Menu_Esquerdo.width()
      
        if width == 1:
            newWidth = 250
            
        else:
            newWidth = 1
        self.animation = QtCore.QPropertyAnimation(self.Menu_Esquerdo, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


# VERFIICAÇÃO DE SEGURANÇA

    def salva_chave_txt(self, chave_digitada):
        # Defina a chave de 8 dígitos
        if chave_digitada == None:
            return
        else:

            chave = chave_digitada
            #print('chave digitada salva:', chave)
            chave = self.criptografia_data(chave)
            #print('chave criptografada:', chave)

        

            # Caminho para o diretório de destino
            #caminho_destino = r'T:\MEUS CODIGOS\venv'
            caminho_destino = r'C:\ProgramData\Athenadevs'

            try:
                # Verifica se o diretório de destino existe, senão cria
                if not os.path.exists(caminho_destino):
                    os.makedirs(caminho_destino)

                # Caminho completo para o arquivo de saída
                arquivo_saida = os.path.join(caminho_destino, 'sysathena.txt')

                # Escreve a chave no arquivo de texto
                with open(arquivo_saida, 'w') as arquivo:
                    arquivo.write(chave)

                #print(f'Chave salva em: {arquivo_saida}')
            except Exception as e:
                print(f"Ocorreu um erro ao salvar o arquivo: {str(e)}")

    def carrega_chave_txt(self):
        # Caminho completo para o arquivo de entrada
        caminho_destino = r'C:\ProgramData\Athenadevs'
        arquivo_entrada = os.path.join(caminho_destino, 'sysathena.txt')

        # Verifica se o arquivo existe
        if os.path.exists(arquivo_entrada):
            # Lê o conteúdo do arquivo e salva em uma variável
            with open(arquivo_entrada, 'r') as arquivo:
                chave = arquivo.read()
                chave = self.descriptografar(chave)
            #print(f'Chave lida do arquivo: {chave}')
            return chave
        else:
            print(f'O arquivo {arquivo_entrada} não existe.')
        
    def adiciona_lista_negra(self, chave_digitada):

        chave_digitada = pd.Series([chave_digitada])
        self.df_restrito = pd.concat([self.df_restrito, chave_digitada], ignore_index=True)
        self.df_restrito = self.df_restrito.apply(self.criptografia_data)
        
        # Salvar o DataFrame resultante em um arquivo CSV  verificar sem .csv
        
        self.df_restrito.to_csv('sis_init', index=False)
        
        #print('chave lida restrição', chave_digitada)
        #print('adicionado chave a rstrição',self.df_restrito)

    def criptografia_data(self, s):

        if len(s) < 8:
            return s
        tres_primeiras_letras = s[:3]
        resto_da_string = s[3:]
        nova_string = resto_da_string + tres_primeiras_letras
        return nova_string

    def descriptografar(self, s):
        if len(s) < 8:
            return s
        
        # Obter as três últimas letras
        tres_ultimas_letras = s[-3:]
        
        # Obter o restante da string
        resto_da_string = s[:-3]
        
        # Reorganizar as letras
        string_original = tres_ultimas_letras + resto_da_string
        
        return string_original

    def gate_acesso(self):
        
        self.TX_ativacao.setStyleSheet("background-color: grey21;")
        # le o dataframe do banco de dados
        self.data_chave = pd.read_csv("sis_eng")
        
        #print(self.data_chave)
                                        
        # recebe o valor da QlindeEdit        
        self.chave_digitada = self.TX_ativacao.text()
        self.chave_digitada = self.chave_digitada.strip() #OK

        # carrega o valor da chave no arquivo txt se houver
    
        self.arquivo_chave_txt = self.carrega_chave_txt()
        #self.arquivo_chave_txt = self.descriptografar(self.carrega_chave_txt)

        #print('arquivo chave descripto',self.arquivo_chave_txt)

        self.data_chave['Chave'] = self.data_chave['Chave'].apply(self.descriptografar)
        verifica_txt = self.arquivo_chave_txt in self.data_chave['Chave'].values       
        print('verifica txt:', verifica_txt)
       


        self.verifica_banco_de_dados = self.chave_digitada in self.data_chave['Chave'].values       
        print('verifica banco de dados:', self.verifica_banco_de_dados)

        self.df_restrito = self.df_restrito.apply(self.descriptografar)
        #print('lista negra descripto:', self.df_restrito)
        self.verifica_lista_restricao = self.chave_digitada in self.df_restrito.values
        #print('lista de restrição:', self.verifica_lista_restricao)


        if verifica_txt == True:
            print('LICENÇA VÁLIDA etapa 01')
            self.salva_chave_txt(self.chave_digitada)
            self.acesso_permitido = True
            print('etapa 01 ',self.acesso_permitido)
            self.TX_ativacao.setStyleSheet("background-color: springgreen;")
            self.TX_ativacao.setText(self.carrega_chave_txt())
            self.TX_ativacao.setReadOnly(True)
            self.LB_ativacao.setText('Insira a Chave de Ativação: ATIVADO')
            return self.acesso_permitido
        

        else:
            
            if self.verifica_banco_de_dados == True and self.verifica_lista_restricao == False:
                
                self.salva_chave_txt(self.chave_digitada)
                print('chave txt:',self.arquivo_chave_txt)
                self.adiciona_lista_negra(self.chave_digitada)
                self.acesso_permitido = True
                self.TX_ativacao.setStyleSheet("background-color: springgreen;")
                
                self.LB_ativacao.setText('Insira a Chave de Ativação: ATIVADO')
                print('LICENÇA VÁLIDA etapa 2', self.acesso_permitido)
                return self.acesso_permitido

            else:

                print('LICENÇA INVALIDA')
                self.acesso_permitido = False
                self.TX_ativacao.setStyleSheet("background-color: tomato;")
                self.LB_ativacao.setText('Insira a Chave de Ativação:')
                return self.acesso_permitido
            

if __name__=="__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    