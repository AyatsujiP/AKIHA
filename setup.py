#! C:/Python27
# -*- coding:utf-8 -*-

from distutils.core import setup
import py2exe

if __name__=="__main__":
	option = {"compressed":1,"optimize":2,"bundle_files":3}
	setup(options = {"py2exe":option}, windows = [{"script":"main.pyw"}],zipfile = None)