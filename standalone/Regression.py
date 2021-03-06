#! C:/python35
#-*- encoding: utf-8 -*-


import logging
import numpy as np
import AttributeClass

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
	
	def normalizeCoef(self):
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
	
	def register(self,preferredArray):
		"""
		アイドルのマージソート結果の配列を、インスタンス変数のそれぞれの属性ごとの配列に変換する。
		"""
		self.num = 0
		for p in preferredArray:
			self.appendB(p.getB())
			self.appendW(p.getW())
			self.appendH(p.getH())
			self.appendAge(p.getAge())
			self.appendHeight(p.getHeight())
			self.appendWeight(p.getWeight())
			self.appendCu(p.getCu())
			self.appendCo(p.getCo())
			self.appendPa(p.getPa())
			self.num = self.num + 1
	
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
	
	def returnPredict(self,arrayToPredict):
		"""
		予測結果の返却。
		"""
		ans = []
		pred = []
		for a in arrayToPredict:
			#coefとarrayToPredictの内積を取ってpredに投入する。
			ret = 0.0
			ret = ret + ((a.getB() - self.nc[0][0])/self.nc[0][1])* self.coef[1]
			ret = ret + ((a.getW() - self.nc[1][0])/self.nc[1][1])* self.coef[2]
			ret = ret + ((a.getH() - self.nc[2][0])/self.nc[2][1])* self.coef[3]
			ret = ret + ((a.getAge() - self.nc[3][0])/self.nc[3][1])* self.coef[4]
			ret = ret + ((a.getHeight() - self.nc[4][0])/self.nc[4][1])* self.coef[5]
			ret = ret + ((a.getWeight() - self.nc[5][0])/self.nc[5][1])* self.coef[6]
			ret = ret + ((a.getCu() - self.nc[6][0])/self.nc[6][1])* self.coef[7]
			ret = ret + ((a.getCo() - self.nc[7][0])/self.nc[7][1])* self.coef[8]
			ret = ret + ((a.getPa() - self.nc[8][0])/self.nc[8][1])	* self.coef[9]
			ans.append((a.getName(),ret))
			pred.append(ret)
		
		logging_string = u""
		#タプルの中身をログ出力
		for tup in ans:
			logging_string = logging_string + "%s:\t%2.3f\n" % (tup[0], tup[1])
		logging.info("Preferred value:\n" + logging_string)
		
		#predが最も大きくなるようなa.getName()の値を求めて返却する。
		max = ans[np.argmax(pred)]
		str = u"%s" % (max[0])
		return str

	def mean_to_zero_coef_cucopa(self):
		#多重共線性の補正(Cute, Cool, Passionの合計を0になるように補正)
		cucopamean = (self.coef[7] + self.coef[8] + self.coef[9]) / 3
		for i in range(7,10):
			self.coef[i] = self.coef[i] - cucopamean

def normalize(array):
	"""
	配列を正規化する。
	"""
	sumArray = sum(array)/float(len(array))
	ans = [array[i] - float(sumArray) for i in range(0,len(array))] # mean = 0
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

def returnRank(array):
	ct = 0
	print ("Ranking:")
	for item in array:
		ct = ct + 1
		print ("No.%d:\t\t%s" % (ct,item))

def seihekiChecker(regAns):
	"""
	どの属性にどの程度重みがついているかを表示する。
	"""
	returnText = "Coefficients:\n   Bust: %0.5f\n   Waist: %0.5f\n   Hip: %0.5f\n   Age: %0.5f\n   Height: %0.5f\n   Weight: %0.5f\n   Cute: %0.5f\n   Cool: %0.5f\n   Passion: %0.5f" % (regAns[1],regAns[2],regAns[3],regAns[4],regAns[5],regAns[6],regAns[7],regAns[8],regAns[9])
	absAns = abs(regAns)[1:10]
	maxArg = np.argmax(absAns)
	return returnText