# MiniAODext-reprocessing
This repository provides the recipes to process AOD datasets to obtain an enriched version of official miniAOD format containing displaced muon collections. It contains the reprocessing routines that correspond to the analysis of Run2 data.


## 2016

(To be filled)

## 2017

(To be filled)

## 2018

Both Monte Carlo and Data are processed with CMSSW_10_2_5 release that is installed with following command sequence:

```
scram p CMSSW CMSSW_10_2_5
cd CMSSW_10_2_5/src
eval scram runtime -sh
scram b
```

### Monte Carlo

Monte Carlo simulated samples follow the processing requirements of the original RunIIAutumn18MiniAOD campaign. To avoid inconsistencies, the original global tag for each dataset is used: 102X_upgrade2018_realistic_v15. 

To create the config file just type the following cmsDriver.py command:

```
cmsDriver.py  --python_filename RunIIAutumn18MiniAOD-cfg.py --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --fileout file:RunIIAutumn18MiniAOD.root --conditions 102X_upgrade2018_realistic_v15 --step PAT --geometry DB:Extended --filein "dbs:/WZ_TuneCP5_13TeV-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v3/AODSIM" --era Run2_2018 --runUnscheduled --no_exec --mc -n 10 || exit $? ;

```

(Note: The command above can be adapted to run in any published dataset, NLO WZ is taken as an example.)

To include the displaced collections the following lines must be added just before the output routine is defined i.e. L263:

```
process.MINIAODSIMEventContent.outputCommands.extend(cms.untracked.vstring(
    'keep *_displacedGlobalMuons_*_RECO',
    'keep *_displacedStandAloneMuons_*_RECO'
))

```


