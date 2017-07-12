#! C:/python35
# -*- coding: utf-8 -*-

#settings.py
#共通で用いる変数はここに格納する。

import logging

VERSION = u"1.0.0"


LOG_FILE_NAME="logs/AKIHA.log"

SORT_FILE_NAME = "MobaMas.txt"

SUGGEST_FILE_NAME = "Suggest.txt"

PICTURE_DIR = "Pictures"

FONT = "Gputeks"

LOGLEVEL = logging.INFO

DB_NAME = "akiha"

DB_PASSWORD = "dbfp"

IDOLS_COLUMNS = ["Name", "Bust", "Waist", "Hip", "Age", "Height", "Weight", "Cute", "Cool", "Passion", "Pictures"]

SORT_DATABASE_NAME = "sorted_idols"

SUGGEST_DATABASE_NAME = "suggested_idols"

CREATE_DATE = "2017-04-16"