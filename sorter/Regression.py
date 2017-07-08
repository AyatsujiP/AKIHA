#-*- encoding: utf-8 -*-

#Module for Regression Analysis.

import logging
import numpy as np
from sorter.models import SortedIdols, SuggestedIdols, MergeSortChoices

class RegressionClass():
	"""
	回帰分析を行うためのクラス。
	"""
	def __init__(self):
		self.num = 0
		self.BArray = []
		self.WArray = []
		self.HArray = []
		self.ageArray = []
		self.heightArray = []
		self.weightArray = []
		self.cuArray = []
		self.coArray = []
		self.paArray = []
		self.nc = None
		self.coef = []
	def appendB(self,B):
		self.BArray.append(B)
	def appendW(self,W):
		self.WArray.append(W)
	def appendH(self,H):
		self.HArray.append(H)
	def appendAge(self,Age):
		self.ageArray.append(Age)
	def appendHeight(self,Height):
		self.heightArray.append(Height)
	def appendWeight(self,Weight):
		self.weightArray.append(Weight)	
	def appendCu(self,Cu):
		self.cuArray.append(Cu)
	def appendCo(self,Co):
		self.coArray.append(Co)
	def appendPa(self,Pa):
		self.paArray.append(Pa)
		
	def normalizeAll(self):
		"""
		それぞれの配列を正規化する。
		"""
		self.BArray = normalize(self.BArray)
		self.WArray = normalize(self.WArray)
		self.HArray = normalize(self.HArray)
		self.ageArray = normalize(self.ageArray)
		self.heightArray = normalize(self.heightArray)
		self.weightArray = normalize(self.weightArray)
		self.cuArray = normalize(self.cuArray)
		self.coArray = normalize(self.coArray)
		self.paArray = normalize(self.paArray)
		
	def returnAll(self):
		"""
		2次元配列として返却
		"""
		return np.array([self.BArray,self.WArray,self.HArray,self.ageArray,self.heightArray,self.weightArray,
						self.cuArray,self.coArray,self.paArray])
	
	def normalize_coef(self):
		"""
		正規化するための、平均と標準偏差を返却。
		"""
		self.nc =  np.array([[np.mean(self.BArray),np.std(self.BArray)],
							[np.mean(self.WArray),np.std(self.WArray)],
							[np.mean(self.HArray),np.std(self.HArray)],
							[np.mean(self.ageArray),np.std(self.ageArray)],
							[np.mean(self.heightArray),np.std(self.heightArray)],
							[np.mean(self.weightArray),np.std(self.weightArray)],
							[np.mean(self.cuArray),np.std(self.cuArray)],
							[np.mean(self.coArray),np.std(self.coArray)],
							[np.mean(self.paArray),np.std(self.paArray)]]
							)

	
	def regression(self):
		"""
		回帰分析を実行する。
		"""
		#目的変数(大きいほうがより好まれているということを示すため、順位をひっくり返してその後標準化)
		pref = normalize([self.num - i for i in range(0,self.num)])

		#独立変数を正規化
		self.normalizeAll()
		#配列として返却
		expl = self.returnAll()
		#重回帰分析の実行
		self.coef = stat(pref,expl)
		
		self.mean_to_zero_coef_cucopa()
		self.mean_to_zero_coef_cucopa()

		return self.coef
	
	def return_predict_with_database(self,mergesort_id):
		ans = []
		names = []
		pictures = []
		q = SuggestedIdols.objects.all().order_by("id")
		for idol in q:
			ret = 0.0
			ret = ret + ((idol.bust - self.nc[0][0])/self.nc[0][1])* self.coef[1]
			ret = ret + ((idol.waist - self.nc[1][0])/self.nc[1][1])* self.coef[2]
			ret = ret + ((idol.hip - self.nc[2][0])/self.nc[2][1])* self.coef[3]
			ret = ret + ((idol.age - self.nc[3][0])/self.nc[3][1])* self.coef[4]
			ret = ret + ((idol.height - self.nc[4][0])/self.nc[4][1])* self.coef[5]
			ret = ret + ((idol.weight - self.nc[5][0])/self.nc[5][1])* self.coef[6]
			ret = ret + ((idol.cute - self.nc[6][0])/self.nc[6][1])* self.coef[7]
			ret = ret + ((idol.cool - self.nc[7][0])/self.nc[7][1])* self.coef[8]
			ret = ret + ((idol.passion - self.nc[8][0])/self.nc[8][1])	* self.coef[9]
			ans.append(ret)
			names.append(idol.name)
			pictures.append(idol.pictures)
		
		ms = MergeSortChoices.objects.all().filter(id=mergesort_id)[0]
		ms.suggest_score = ans
		most_preferred = np.argmax(ans)
		ms.most_preferred_name = names[most_preferred]
		ms.most_preferred_picture = pictures[most_preferred]
		ms.save()


	def mean_to_zero_coef_cucopa(self):
		#多重共線性の補正(Cute, Cool, Passionの合計を0になるように補正)
		cucopamean = (self.coef[7] + self.coef[8] + self.coef[9]) / 3
		for i in range(7,10):
			self.coef[i] = self.coef[i] - cucopamean
			
			
	def register_with_database(self,id_array):
		self.num = 0
		for ia in id_array:

			concerned_idol = SortedIdols.objects.all().filter(id=ia)[0]
			self.appendB(concerned_idol.bust)
			self.appendW(concerned_idol.waist)
			self.appendH(concerned_idol.hip)
			self.appendAge(concerned_idol.age)
			self.appendHeight(concerned_idol.height)
			self.appendWeight(concerned_idol.weight)
			self.appendCu(concerned_idol.cute)
			self.appendCo(concerned_idol.cool)
			self.appendPa(concerned_idol.passion)
			self.num = self.num + 1
			
	def return_coef_dict(self,mergesort_id):
		ret_dict = {"bust": "%1.5f" % self.coef[1],
			"waist":"%1.5f" % self.coef[2],
			"hip":"%1.5f" % self.coef[3],
			"age":"%1.5f" % self.coef[4],
			"height":"%1.5f" % self.coef[5],
			"weight":"%1.5f" % self.coef[6],
			"cute":"%1.5f" % self.coef[7],
			"cool":"%1.5f" % self.coef[8],
			"passion":"%1.5f" % self.coef[9]
			}
		b = MergeSortChoices.objects.all().filter(id=mergesort_id)[0]
		b.pref_coefficient = ["%1.5f" % self.coef[i] for i in range(1,10)]
		b.save()
		return ret_dict

def normalize(array):
	"""
	配列を正規化する。
	"""
	sumArray = sum(array)/float(len(array))
	ans = [array[i] - float(sumArray) for i in range(0,len(array))]

	stdArray = np.std(ans)
	ans = [ans[i] / float(stdArray) for i in range(0,len(array))]
	return ans

def stat(obj, exp):
	"""
	重回帰分析の実行
	"""
	
	n = exp.shape[1]
	exp = np.vstack([np.ones(n), exp])
	coef = np.linalg.lstsq(exp.T, obj)[0]
	return coef







	