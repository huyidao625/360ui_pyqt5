#!/usr/bin/python  
#-*-coding:utf-8-*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.Qt import *

class ToolButton(QToolButton):
	def __init__(self,pic_name,parent = None):
		super(ToolButton,self).__init__(parent)
		
		#����ͼ��
		self.pixmap= QPixmap(pic_name) 
		self.setIcon(QIcon(self.pixmap))
		self.setIconSize(self.pixmap.size())
		#���ô�С
		self.setFixedSize(self.pixmap.width()+25, self.pixmap.height()+27)
		self.setAutoRaise(True)
		
		#�����ı���ɫ
		self.text_palette = QPalette()#palette() QPalette
		self.text_palette.setColor(self.text_palette.ButtonText, QColor(230, 230, 230))
		self.setPalette(self.text_palette)

		#�����ı�����
		self.text_font = QFont() #QFont & const_cast<QFont &>(font())
		self.text_font.setWeight(QFont.Bold)
		
		#��������������
		self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

		self.setStyleSheet("background:transparent")
		
		self.mouse_over  = False#����Ƿ��ƹ�
		self.mouse_press = False#����Ƿ���
		
	def enterEvent(self,event):
		self.mouse_over = True
		self.update()
		
	
	def leaveEvent(self,event):
		self.mouse_over = False
		self.update()
		
	def mousePressEvent(self,event):
		if(event.button() == Qt.LeftButton):		
			self.clicked.emit(True)
			
	def setMousePress(self, mouse_press):
		self.mouse_press = mouse_press
		self.update()
		
	def paintEvent(self,event):
		if(self.mouse_over):
			#��������Ƶ���ť�ϵİ�ťЧ��
			self.painterInfo(0, 100, 150)
		else:
			if(self.mouse_press):
				self.painterInfo(0, 100, 150)
		QToolButton.paintEvent(self,event)
		
	def painterInfo(self,top_color,middle_color,bottom_color):
		self.painter = QPainter()
		self.painter.begin(self)
		#self.pen = QPen()
		#self.pen.setWidth(0)
		self.painter.setPen(Qt.NoPen)
		
		self.linear = QLinearGradient(self.rect().topLeft(),self.rect().bottomLeft())
		#self.linear.start()
		self.linear.setColorAt(0, QColor(230, 230, 230, top_color))
		self.linear.setColorAt(0.5, QColor(230, 230, 230, middle_color))
		self.linear.setColorAt(1, QColor(230, 230, 230, bottom_color))
		#self.linear.finalStop()
		
		self.painter.setBrush(self.linear)
		#self.painter.fillRect(self.rect(),Qt.LinearGradientPattern)
		self.painter.drawRect(self.rect()) #
		self.painter.end()

		
	
if __name__ == '__main__':
	
	
	import sys
	app = QApplication(sys.argv)
	tool = ToolButton("./img/toolWidget/gongNeng.png")
	#tool.setMousePress(True)
	tool.show()
	sys.exit(app.exec_())	


