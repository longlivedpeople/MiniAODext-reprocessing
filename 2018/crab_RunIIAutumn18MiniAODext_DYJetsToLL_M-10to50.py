import CRABClient
from CRABClient.UserUtilities import config

config = config()

# All output/log files go in directory workArea/requestName/
config.General.workArea = 'crab_projects'

config.General.requestName = 'DYJetsToLL_M-10to50_miniAODext'

config.General.transferOutputs = True
config.General.transferLogs = True
config.General.instance = 'prod'

# Set pluginName = Analysis if you are reading a dataset, or to PrivateMC if not (so you are generating events)
config.JobType.pluginName = 'Analysis'
# CMSSW cfg file you wish to run
config.JobType.psetName = 'RunIIAutumn18MiniAODext-cfg.py'
# Increase virtual memory limit (sum needed by all threads) from default of 2000 MB.
config.JobType.maxMemoryMB = 2500
# Number of threads to use.
#config.JobType.numCores = 2
# To allow use of SL7 CMSSW versions that were SL6 at time of original DATA/MC production.
config.JobType.allowUndistributedCMSSW = True

# Input dataset (small)
config.Data.inputDataset = '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v2/AODSIM'
config.Data.inputDBS = 'global'

# Units of "totalUnits" and "unitsPerJob" (e.g. files, events, lumi sections)
config.Data.splitting = 'FileBased'
# Total number of these units to be processed.
#config.Data.totalUnits = 999
# Requested number in each subjob.
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/fernance/'
config.Data.publication = True

# Output dataset stored in my dcache area in AAA/tomalin-outputDatasetTag-encodedDataAndTime/USER 
# where "AAA" is name between first pair of slashes in input dataset.
config.Data.outputDatasetTag = 'RunIIAutumn18MiniAODext'

config.Site.storageSite = 'T2_ES_IFCA'
