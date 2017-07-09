#! C:/Python35
#-*- encoding: utf-8 -*-

#A Knowledge-based Items' Hierarchical Algorithm (AKIHA) Ver 0.7.1 Main Module
#Copyright (c) 2017 AyatsujiP All Rights Reserved.


import settings
import logging
import GUI
import time
import traceback


if __name__=="__main__":
	#メインループ
	#ログ用ファイルの作成
	logging.basicConfig(filename=settings.LOG_FILE_NAME,level=settings.LOGLEVEL,format='%(asctime)s %(message)s')
	logging.info("AKIHA started.")
	#メインループ
	root = GUI.MyTk()
	app = GUI.MyApp(master=root)
	root.mainloop()
