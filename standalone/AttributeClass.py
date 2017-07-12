#! C:/Python35
# -*- encoding: utf-8 -*-
#Module for Class Definition.

import logging
import random

class IdolsContainer():
	"""
	IdolsAttributeを格納するためのコンテナ。
	"""
	def __init__(self):
		self.container = []
	
	
	def appendIdol(self,idol):
		"""
		コンテナにアイドルを追加するラッパー。
		"""
		self.container.append(idol)
	
	def returnIdolByName(self,findName):
		"""
		アイドル名を用いて、アイドルの属性を返却する関数。
		"""
		for i in self.container:
			if i.name == findName:
				return i
		return "No %s Found." % findName
		
	def returnContainer(self):
		"""
		コンテナそのものを返却する。
		"""
		return self.container
		
	def returnNameArray(self):
		"""
		名前の一覧を返却する。
		"""
		ans = []
		for item in self.container:
			ans.append(item.getName())
		return ans

	def shuffle(self):
		"""
		順番をシャッフルする。
		"""
		ary = [i for i in range(0,len(self.container))]
		random.shuffle(ary)
		for i in range(0,len(self.container)):
			tmp = self.container[i]
			self.container[i] = self.container[ary[i]]
			self.container[ary[i]] = tmp
		

class IdolsAttribute():
	"""
	各アイドルの属性。
	"""
	
	def __init__(self):
		self.name = u"Tsukasa Ayatsuji" 
		self.B = 72 
		self.W = 72
		self.H = 72
		self.age = 18 
		self.height = 156
		self.weight = 52 
		self.cu = 0
		self.co = 0
		self.pa = 0
		self.pictureName = u""
		
	def setAll(self,name=u"Tsukasa Ayatsuji",Bu=72,Wa=72,Hi=72,Ag=18,He=156,We=52,Cu=1,Co=0,Pa=0,Pi=u""):
		self.name = name
		self.B = float(Bu)
		self.W = float(Wa)
		self.H = float(Hi)
		self.age = float(Ag)
		self.height = float(He)
		self.weight = float(We)
		self.cu = float(Cu)
		self.co = float(Co)
		self.pa = float(Pa)
		self.pictureName = Pi
	def getName(self):
		return self.name
	def getB(self):
		return self.B
	def getW(self):
		return self.W
	def getH(self):
		return self.H
	def getAge(self):
		return self.age
	def getHeight(self):
		return self.height
	def getWeight(self):
		return self.weight
	def getCu(self):
		return self.cu
	def getCo(self):
		return self.co
	def getPa(self):
		return self.pa
	def getPictureName(self):
		return self.pictureName
	def returnAll(self):
		return []