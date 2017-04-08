#! C:/Python27
# -*- encoding: utf-8 -*-

#Module for Merge Sorting and others.
##Copyright (c) 2017 AyatsujiP All Rights Reserved.

import AttributeClass as ac 

def printChoice(leftItem,rightItem):
	#deprecated(for CLI)
	print "\n\n\nWhich is more preferred, Left or Right?"
	print "===%s ===              ===%s ===" % (leftItem,rightItem)
	print "If left, press 'L'; If right, press 'R'"




def readTable(FILENAME):
	"""
	Mobamas.txt, Suggest.txtを読み込んでコンテナに格納する
	"""
	f = open(FILENAME,"r")
	cont = ac.IdolsContainer()
	next(f)
	for l in f:
		try:
			trg = l.rstrip("\n").split(",")
			#print trg
			tmp = ac.IdolsAttribute()
			tmp.setAll(trg[0].decode("utf-8"),trg[1],trg[2],trg[3],trg[4],trg[5],trg[6],trg[7],trg[8],trg[9],trg[10])
			cont.appendIdol(tmp)
		except:
			pass
	return cont
	
def mergeWithoutRecWithAns(array,ansArray):
	"""
	マージソートを行うための関数。マージソートの、1回ごとの比較をユーザに行わせるために、それまでのマージソートの結果とともに比較すべき対象を返却する。
	リファクタリングの際は手を入れないほうが無難。
	"""
	arraycp = [i for i in array]
		
	ansLen = len(ansArray)
	ct = 0
	arrayLen = len(arraycp)
	powArray = []
	tmp = [0 for i in range(0,arrayLen)]
	k = 1
	while(True):
		powArray.append(k)
		if k*2 < arrayLen:
			k = k * 2
		else:
			break
	for div in powArray:
		segArray = []
		l = 0
		while(True):
			segArray.append(l)
			if l+div*2 < arrayLen:
				l = l+div*2
			else:
				break
		for seg in segArray:
			fb = n = seg
			sb = fe = min(fb + div, arrayLen)
			se = min(sb + div, arrayLen)
			i = fb
			j = sb
			while (i < fe and j < se):
				if ct >= ansLen:
					return [arraycp[i],arraycp[j]]
				if ansArray[ct] == 1:
					tmp[n] = arraycp[i]
					n = n + 1
					i = i + 1
				else:
					tmp[n] = arraycp[j]
					n = n + 1
					j = j + 1
				ct = ct + 1

			while ( i < fe ):
				tmp[n] = arraycp[i]
				n = n + 1
				i = i + 1
			while ( j < se ):
				tmp[n] = arraycp[j]
				n = n + 1
				j = j + 1
			for p in range(seg,n):
				arraycp[p] = tmp[p]
	return arraycp