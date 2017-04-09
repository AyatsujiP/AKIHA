#! C:/python27
#-*- encoding: utf-8 -*-

#A Knowledge-based Items' Hierarchical Algorithm (AKIHA) Ver 0.7.1 Main Module
#Copyright (c) 2017 AyatsujiP All Rights Reserved.

import logging
import GUI

if __name__=="__main__":
	#メインループ
	logging.basicConfig(filename="logs/AKIHA.log",level=logging.INFO,format='%(asctime)s %(message)s')
	logging.info("AKIHA started.")
	root = GUI.MyTk()
	app = GUI.MyApp(master=root,filename="MobaMas.txt",sugfile = "Suggest.txt")
	root.mainloop()