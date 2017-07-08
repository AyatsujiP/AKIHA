# A Knowledge-based Items' Hierarchical Algorithm (AKIHA) Ver2.1.1 ������

## 1�D �T�v
�{�v���O�����́A�D���ȃA�C�h����2���őI��ł����ƁA�������g�̍D���ȃA�C�h���̏��ʂ���т������߃A�C�h����\�����Ă����v���O�����ł���B
���I�Ȃ��Ƃ������ƃ\�[�e�B���O���ʂɊ�Â��d��A�Ɨ\�������s����v���O�����ł���B

���O�̗R���͏�L����(�m���x�[�X�ɂ��A�C�e���K�w���A���S���Y��)�����A14�΂̓V�˃��{�����Ƃ��A�l�̖ڂ����������ŐS���ǂ߂�l�R�~�~���C�h�Ƃ��A
Web�ɐ������郉���v�̖��l�Ȃ񂩂ɂ��֌W�����邩������Ȃ��B�֌W���Ȃ���������Ȃ��B

�T���v���Ƃ��ėp�ӂ��Ă���̂�Idolm@ster �V���f�����K�[���Y�ɓo�ꂷ��A�C�h���ł��邪�A���ۂɂ̓X���[�T�C�Y�A�N��A�g���A�̏d�A���i(Cute��Cool��Passion����3��)���킩���
2�������낤��3�������낤��9�����f�[�^�ɗ��Ƃ����߂�̂ŁA�{�v���O�����Ń\�[�g�E�T�W�F�X�g�\�ł���B


## 2. �T�[�o�̃Z�b�g�A�b�v

### 2-1. DB(Postgresql)
 - Postgresql(9.6����)���_�E�����[�h���Ă����Bapt-get�œ�����̂ł悢�B
 - ���[�U�[�Ƃ��āAakiha������Ă����B�p�X���[�h���K���Ɍ��߂�B
 
### 2-2. Django, numpy, PIL(Python�p�b�P�[�W)
 - Django 1.11���_�E�����[�h���Ă����B
 - numpy��PIL�ɂ��Ă��_�E�����[�h���Ă����B
 - pip3 install django numpy pillow�ŃC���X�g�[���\�B

### 2-3. �\�[�X�R�[�h�̃f�v���C
 - Git�����擾����B�ȉ��A/var/www/AKIHA�ȉ��Ƀ_�E�����[�h�������Ƃ�O��ɋL�ڂ���B
 - �ʂ̏ꏊ�Ƀf�v���C�����ꍇ�͓K�X�ǂݑւ��邱�ƁB
 - AKIHA_for_web/�z���ɁAsecrets.py�t�@�C�����쐬����B
 - �t�@�C���̓��e�Ƃ��āA�ȉ����L�ڂ���B
 
    #-*- coding: utf-8 -*-
    DB_PASSWORD = '<2-1�Ō��߂��p�X���[�h>'
    SECRET_KEY = '<�K���ȕ�����B���ł��悢�B>'

### 2-4. DB�̐ݒ�
 - postgresql�ɁA���[�U��akiha�ADB��akiha\_for\_web�Ƃ���DB������Ă����B�����R�[�h��UTF-8�ɂ��Ă������ƁB
 
### 2-5. �}�C�O���[�V����
 - /var/www/AKIHA�ŁApython3 manage.py migrate��DB�Ƀe�[�u�����쐬�B
 - /var/www/AKIHA�ŁApython3 sorter/insert\_initial\_idols.py�����s���ď����f�[�^�𓊓��B
 
### 2-6. �������[������
 - python3 manage.py createsuperuser�ŃX�[�p�[���[�U�쐬�BDjango�̊Ǘ����[�U���쐬�����B
 
# 3. ���s
 - 2�͂�2-1����2-6�܂ł����s������A/var/www/AKIHA��python3 manage.py runserver������΁A127.0.0.1:8000�ŗ����オ��B
 - Apache��œ����������Ƃ����v�����Ȃ���΁A����ł悢�B
 - Apache�Ńz�X�e�B���O�������ꍇ�́A�����g�Œ��ׂĂ��������Bmod-wsgi���g�����ƂɂȂ�܂��B
 
# 4. ���l
 - ���͐_�J�ޏ�P�ł��B
 
# 5. �����[�X�m�[�g
* 2016.8.12 Ver 0.7.0 �o�O�t�B�b�N�X���{�A�����[�X��
* 2017.3.5 Windows10�ł����삷�邱�Ƃ��m�F
* 2017.4.9 Ver 0.7.1 �����[�X(�\�[�X�Ǘ���Github�Ɉڍs)
* 2017.7.8 Ver 0.8.0 �����[�X(�~���V�^�̃����[�X���L�O���āA�~���V�^�̏����A�C�h��3�l�̂�������1�l���T�W�F�X�g�����悤�ɏC��)
* 2017.7.8 Ver 2.1.1 �����[�X()