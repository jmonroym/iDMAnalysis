import os, sys
import subprocess


test = True
if test:
	mchis=['6p0']#['60p0']
	dmchis=['2p0']#['20p0']
	lifelist=[1]
	masslist = ["Mchi-%s_dMchi-%s"%(mchi,dmchi) for mchi,dmchi in zip(mchis,dmchis)]

else:
	lifelist = [1,10,100,1000]
	#mchis=['52p5']
	#dmchis=['5p0']
	#mchis=['5p25']
	#dmchis=['0p5']
	#mchis=['6p0']
	#dmchis=['2p0']
	mchis=['60p0']
	dmchis=['20p0']
	#mchis=['6p0','60p0','5p25','52p5']
	#dmchis=['2p0','20p0','0p5','5p0']
	masslist = ["Mchi-%s_dMchi-%s"%(mchi,dmchi) for mchi,dmchi in zip(mchis,dmchis)]

print masslist

makedir = subprocess.Popen("mkdir /uscmst1b_scratch/lpc1/3DayLifetime/mireid",shell=True,stdout=subprocess.PIPE)
makedir.wait()
analyzer ='MetTrigSelfEffiForMuTrack_cfg.py'
#analyzer ='iDMAnalyzer_cfg.py'
#analyzer='MuRecoEffi_cfg.py'
for mass in masslist:
	for life in lifelist:	
		odir = "/uscmst1b_scratch/lpc1/3DayLifetime/mireid"
		ofile= "iDMAnalysis_{0}_ctau-{1}.root".format(mass,life)
		if test:
			cmdxx = "cmsRun python/{1} year=2018 inputFiles_load=data/iDM/2018/signal/test.list outputFile=test_{0}".format(ofile,analyzer)#,mass,life)
		
			print(cmdxx)
			process1 = subprocess.Popen(cmdxx,shell=True, stdout=subprocess.PIPE)
			for line1 in iter(process1.stdout.readline,b''):
				print(line1)
			process1.stdout.close()
			process1.wait()
		else:
			cmdxx = "cmsRun python/{4} year=2018 inputFiles_load=data/iDM/2018/signal/{2}_ctau-{3}.list outputFile={0}/{1}".format(odir,ofile,mass,life,analyzer)
		
			print(cmdxx)
			process1 = subprocess.Popen(cmdxx,shell=True, stdout=subprocess.PIPE)
			for line1 in iter(process1.stdout.readline,b''):
				print(line1)
			process1.stdout.close()
			process1.wait()

			#transfer = "xrdcp {0}/{1} root://cmseos.fnal.gov//store/group/lpcmetx/iDM/Ntuples/2018/signal/reco_effi/{2}_ctau-{3}/{1}".format(odir,ofile,mass,life)
			transfer = "xrdcp {0}/{1} root://cmseos.fnal.gov//store/group/lpcmetx/iDM/Ntuples/2018/signal/iDMAnalysis/{2}_ctau-{3}/{1}".format(odir,ofile,mass,life)
			print(transfer)
                	process2 = subprocess.Popen(transfer,shell=True, stdout=subprocess.PIPE)
                	for line2 in iter(process2.stdout.readline,b''):
                        	print(line2)
                	process2.stdout.close()
                	process2.wait()
