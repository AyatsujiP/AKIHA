#! C:/Python27
#-*- encoding: utf-8 -*-

#GUI definition
#Copyright (c) 2017 AyatsujiP All Rights Reserved.


import MergeSort
import AttributeClass as ac
import Regression
import time
import sys
import Dialog
import Tkinter
import tkMessageBox
from PIL import Image,ImageTk

class MyApp(Tkinter.Frame):
	"""
	Tkinterでループを回すクラス。
	"""
	def __init__(self,master=None,filename="MobaMas.txt",sugfile = "Suggest.txt"):
		self.ver = master.ver
		self.myFont = "Gputeks"
		Tkinter.Frame.__init__(self,master)
		self.picDir = "Pictures"
		self.ans = Tkinter.BooleanVar()
		self.ans.set(True)
		self.ansDialog = False
		self.array = []
		self.ansArray = []
		self.nextText = []
		self.pack()
		self.makeWidget()
		self.alignWidget()
		self.ansText = u"Ranking:\n"
		self.seihekiText = u""
		self.idolsContainer = ac.IdolsContainer()
		self.tmpCont = MergeSort.readTable(filename)
		self.tmpCont.shuffle()
		self.sugCont = MergeSort.readTable(sugfile)
		self.nameArray = self.tmpCont.returnNameArray()
		self.setNameArray(self.nameArray)
		self.reg = Regression.RegressionClass()
		self.sugRet = False
		
	
	def imageConfig(self):
		"""
		画像ファイルの表示のための関数。
		"""
		try:
			self.leftImage = Image.open(self.picDir + "/" + self.tmpCont.returnIdolByName(self.nextText[0]).getPictureName())
			self.leftImage = self.leftImage.resize(resizeImage(self.leftImage.size),Image.NEAREST)
			self.leftImText = ImageTk.PhotoImage(self.leftImage)
			self.leftPic.configure(image=self.leftImText)
			self.rightImage = Image.open(self.picDir + "/" + self.tmpCont.returnIdolByName(self.nextText[1]).getPictureName())
			self.rightImage = self.rightImage.resize(resizeImage(self.rightImage.size),Image.NEAREST)
			self.rightImText = ImageTk.PhotoImage(self.rightImage)
			self.rightPic.configure(image=self.rightImText)
		except:
			self.leftImText.configure(file="")
			self.rightImText.configure(file="")
		self.leftText.configure(text=self.nextText[0])
		self.rightText.configure(text=self.nextText[1])

	def setNameArray(self,inArray):
		"""
		マージソートを行う際の次の名前を出すための関数。
		"""
		self.array = inArray
		self.nextText = MergeSort.mergeWithoutRecWithAns(self.nameArray,self.ansArray)
		if len(self.nextText) == 2:
			self.imageConfig()

	def messageWindow(self):
		self.ansDialog = tkMessageBox.askokcancel(u'結果発表',self.ansText)

	def nextCommand(self):
		"""
		GUIの状態を変えるための関数。
		"""
		self.ansArray.append(self.ans.get())
		self.nextText = MergeSort.mergeWithoutRecWithAns(self.array,self.ansArray)
		if len(self.nextText) == 2:
			self.imageConfig()
		else:
			for i in range(0,len(self.nextText)):
				self.ansText = self.ansText + u"\tNo. %d:\t%s\n" % (i+1,self.nextText[i])
			for a in self.nextText:
				self.idolsContainer.appendIdol(self.tmpCont.returnIdolByName(a))
			self.nextButton.configure(state=Tkinter.DISABLED)
			self.reg.register(self.idolsContainer.returnContainer())
			self.reg.normalizeCoef()
			regAns = self.reg.regression()
			self.seihekiText = Regression.seihekiChecker(regAns)
			self.sugText = self.reg.returnPredict(self.sugCont.returnContainer())
			self.messageWindow()
			
			if self.ansDialog == True:
				self.sugWindow = SugWindow(master=self,picDir=self.picDir,sugCont=self.sugCont,
										sugText=self.sugText,myFont=self.myFont,addText=self.addText,seihekiText=self.seihekiText)
				self.sugWindow.mainloop()
				
	def showHelp(self):
		"""
		ヘルプボタンを押したときの挙動。
		"""
		tkMessageBox.showinfo(u"使い方", 
							u"左か右の画像で気に行った方を下のラジオボタンから選択して、「次へ」を押してください。\n" + 
							u"画像すべてに対しての順位付けと、好みの由来が明らかになります。\n")
			
		
	def makeWidget(self):
		"""
		Tkinterのウィジェットをインスタンス変数として作成。
		"""
		self.screenTitle = Tkinter.Label(self,text = "AKIHA Ver %s" % self.ver,font = (self.myFont,30))
		self.leftImage = None
		self.rightImage = None
		self.leftImText = Tkinter.PhotoImage(file=u"")
		self.rightImText = Tkinter.PhotoImage(file=u"")
		self.leftPic = Tkinter.Label(self,image=self.leftImText)
		self.rightPic = Tkinter.Label(self,image=self.rightImText)
		self.leftText =  Tkinter.Label(self)
		self.rightText =  Tkinter.Label(self)
		self.leftRadioButton = Tkinter.Radiobutton(self,text = u'左', variable = self.ans, value = True)
		self.rightRadioButton = Tkinter.Radiobutton(self,text = u'右', variable = self.ans, value = False)
		self.frame0 = Tkinter.LabelFrame(self,text=u"")
		self.nextButton = Tkinter.Button(self.frame0,text=u"次へ",command=lambda: self.nextCommand())
		self.exitButton = Tkinter.Button(self.frame0,text=u"終了",command=sys.exit)
		self.helpButton = Tkinter.Button(self.frame0,text=u"ヘルプ", command = self.showHelp)
		self.addText = "=====================================================\n"+"A Knowledge-based Items' Hierarchical Algorithm (AKIHA) Ver %s\n" % self.ver+"Created by AyatsujiP, 2016-08-12\n" + "====================================================="
		self.additionalInformation = Tkinter.Label(self,text = self.addText,font=(self.myFont,11))
	
	def alignWidget(self):
		"""
		ウィジェットの位置調整。
		"""
		self.screenTitle.grid(row=0,column=0,columnspan=2)
		self.leftPic.grid(row=1,column=0)
		self.rightPic.grid(row=1,column=1)
		self.leftText.grid(row=2,column=0)
		self.rightText.grid(row=2,column=1)
		self.leftRadioButton.grid(row=3,column=0)
		self.rightRadioButton.grid(row=3,column=1)
		self.nextButton.grid(row=4,column=0,pady = 20,padx = 10)
		self.exitButton.grid(row=4,column=1,pady = 20,padx = 10)
		self.helpButton.grid(row=4,column=2,pady = 20,padx = 10)
		self.additionalInformation.grid(row=4,column=0)
		self.frame0.grid(row=4,column=1)

class SugWindow(Tkinter.Toplevel):
	"""
	サジェスト用の画面を出すためのクラス。
	"""
	def __init__(self,master=None,picDir=u"",sugCont=None,sugText=u"",myFont=u"",addText=u"",seihekiText=u""):
		Tkinter.Toplevel.__init__(self,master)
		self.ImageFlag = True
		self.picDir = picDir
		self.sugCont = sugCont
		self.sugText = sugText
		self.myFont = myFont
		self.addText = addText
		self.seihekiText = seihekiText
		
		
		self.makeWidget()
		self.alignWidget()
		
	def makeWidget(self):
		"""
		ウィジェットをインスタンス変数として作成
		"""
		self.sugFrame = Tkinter.Frame(self)
		self.geometry("780x660")
		try:
			self.sugImage = Image.open(self.picDir + "/" + self.sugCont.returnIdolByName(self.sugText).getPictureName())
			self.sugImage = self.sugImage.resize(resizeImage(self.sugImage.size),Image.NEAREST)
			self.sugImText = ImageTk.PhotoImage(self.sugImage)
		except:
			self.ImageFlag = False
			self.sugImText = Tkinter.PhotoImage(file="")
		
		self.sugPic = Tkinter.Label(self.sugFrame,image=self.sugImText)
		self.sugLetter = Tkinter.Label(self.sugFrame,text="Maybe you like...",font = (self.myFont,24))
		self.sugName = Tkinter.Label(self.sugFrame,text=self.sugText)
		self.sugInf = Tkinter.Label(self.sugFrame,text = self.addText,font=(self.myFont,9))
		self.coefs = Tkinter.Label(self.sugFrame,text = self.seihekiText,font=(self.myFont,14),justify=Tkinter.LEFT)
		self.dstr = Tkinter.Button(self.sugFrame,text=u"閉じる",command=self.myDestroy)

		
	def myDestroy(self):
		self.destroy()
		
	def alignWidget(self):
		"""
		ウィジェット配置
		"""
		self.sugLetter.grid(row=0,column=0,pady = 10)
		if self.ImageFlag == True:
			self.sugPic.grid(row=1,column=0,pady = 10)
		else:
			self.geometry("780x500")
			self.sugPic.grid(row=1,column=0,pady = 150)
		self.sugName.grid(row=2,column=0)
		self.sugInf.grid(row=3,column=0,pady=10)
		self.coefs.grid(row=0,column=1,rowspan=4)
		self.dstr.grid(row=3,column=1)

		self.sugFrame.pack()
		
		
	
class MyTk(Tkinter.Tk):
	"""
	GUIのクラスを継承する
	"""
	def __init__(self,master=None):
		self.ver = u"0.7.1"
		Tkinter.Tk.__init__(self,master)
		self.geometry("960x640")
		self.title("AKIHA Ver %s" % self.ver)
		
		
def resizeImage(tup,maxSize=400):
	"""
	画像のサイズを、画面に表示できるように変更する
	"""
	coef = 0.0
	tmp = [0.0,0.0]
	if tup[0] < maxSize and tup[1] < maxSize:
		return tup
	elif tup[0] >= tup[1]:
		tmp[0] = float(maxSize)
		tmp[1] = float(tup[1])/tup[0] * maxSize
	elif tup[0] < tup[1]:
		tmp[1] = float(maxSize)
		tmp[0] = float(tup[0])/tup[1] * maxSize
	return (int(tmp[0]),int(tmp[1]))
	

