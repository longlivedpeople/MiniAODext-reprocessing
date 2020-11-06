# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename RunIIAutumn18MiniAOD-cfg.py --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --fileout file:RunIIAutumn18MiniAOD.root --conditions 102X_upgrade2018_realistic_v15 --step PAT --geometry DB:Extended --filein dbs:/WZ_TuneCP5_13TeV-pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v3/AODSIM --era Run2_2018 --runUnscheduled --no_exec --mc -n 10
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('PAT',eras.Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.PatAlgos.slimming.metFilterPaths_cff')
process.load('Configuration.StandardSequences.PATMC_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/C869BB5C-3031-B743-8D21-CAD8A5DB9F2C.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/EA7B5E4A-9235-4445-981E-1DECA8034AE6.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/E87FAB42-0B6C-5646-88C8-23080A8DCA65.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/EDB42757-0FEB-FF4C-8438-EAB2730BAF7A.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/37AD7E81-4EB4-904F-BB27-82385A5CEA87.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/79C4DD34-F776-9A42-90C3-F8200708F739.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/653289C0-7335-4147-AB9E-3CBFB13F5706.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/3FE391F4-44D9-5546-BBD0-19AAD9F996B0.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/51513B26-333C-B645-B6F6-196D74128E9E.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/EC4EAE67-E6B7-CF4E-9128-F2A78764384B.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/13CE3CA4-CBF2-2643-B17F-6DCBB73C7E9D.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/125A457F-D248-C24F-A54F-FEBD5160B21B.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/E4C1E875-396E-5B41-830B-7B5F0C272EBC.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/E57B68D8-730D-AB49-9FE9-E0B7BA9FEE07.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/5F812913-1F17-8640-8256-E982A8065591.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/7C183688-9674-744A-86E0-44594905E347.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/99EACD13-2141-0746-A1E1-A88C3F436662.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/E775B044-9E6C-2141-AB4A-12DCC5CCD60D.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/D23F95D9-4F83-3847-9EFB-2E04DB96E6B8.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/ECFFA26B-08A8-5045-B253-014B64BB7144.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/AED0E7C6-277D-D740-AC95-B4D9DEDAC245.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/2A2DAEBE-D008-F242-8C5A-85C06CE28C76.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/21E7B394-3F69-2148-BE48-48E644FDEE4F.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/E5FFAE9B-FD3D-9C4F-91A3-939B8B2952B9.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/02CF0B32-3827-814C-B8DC-3A3646F2A2B4.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/9EF9A60A-20CF-9940-9799-A9BB306D3F0E.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/3BE66190-46CE-BC47-9724-723C62EE2621.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/9479FD5C-6835-F64E-874A-15CEDBE0D7AF.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/85488242-1727-C743-A8B4-B1E82DDEE867.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/976B8265-3677-3249-A387-2981C8B6CC9A.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/31C1571C-FE14-3E49-B2A5-5205C2A789F9.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/BC68158A-EAF9-0B45-86D1-445DEE98EEBB.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/C47AF712-BB9C-E749-9D40-8920CAD79822.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/DF30DF4F-DA5A-4C4E-BC40-2AE9B62E3804.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/103F6728-DC22-EE48-936F-2DCA8485B15B.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/50042DE5-FFCC-404D-8945-0F1C7D17EC72.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/86592C42-85A5-E945-AF3A-88E9D7B0B9AD.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/7131BC17-5942-534C-9753-E4F3C5044009.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/7D6485E2-F9EE-EB40-97B2-D6838A8DC370.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/6C59A3E0-7953-8648-BCE9-184C3A6E347C.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/C2A3EDDA-DFE0-234D-9310-6B1FA5A42092.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/8A5C6D32-31E6-934E-9B75-42242098B6A3.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/A4CAF3EC-A3AC-A14B-95D1-99A19215D83E.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/2AAD67EC-55EB-A944-B535-A78E2C60BCB9.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/475A03E9-D0ED-0842-9A3C-9DCDE05BD8EC.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/A8292193-75F6-E847-98BD-E2F1075130AE.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/D9016B2A-A5F3-434D-815A-2C164EFE3C7B.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/C8B4DA52-6E94-9F40-972A-597187CB8DB0.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/CE6FA982-BA9B-7D42-9ED5-D9E23EC56938.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/B4BF1B3A-0E9F-3248-920F-21DEEFF8E86E.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/6609FAE4-033C-6B41-B0BC-961C73E227C0.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/A1942CC3-9936-A643-BAB3-DD4711D91369.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/D215E87F-43E4-9E4F-ADB5-23716CB6A033.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/4F856888-415D-044C-BBC3-98416AA8E4FF.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/6FF78F2E-6343-FE49-9571-A17902716609.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/A46B2C38-2A12-1B4E-9979-0C34E9F1A707.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/6F4B857A-91EF-8D43-887D-32F53D6DA2F4.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/A42EA2A6-16A5-8242-8C9D-C42414C5490A.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/49389B0C-746B-6B44-9601-8B19BF8A6557.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/85A984A6-8909-2F44-A787-AC87B43ECA43.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/6F9C5926-7184-B648-B214-53546CC3726B.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/7C5479A1-6A77-DB40-AE59-B3EB57B303AA.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/0138C315-40B4-B54A-ABE4-7D558815A3F9.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/06945D67-C120-5D47-B67A-03D9DE1FB060.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/D560AD11-FD37-6445-B086-13F5886ACD05.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/CBB5D2D6-301C-7644-87B2-E50325CD14BE.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/C77835C1-488D-5E45-B622-CC6BB9363675.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/72CBF475-F156-054A-8905-D81E01C1B37A.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/9EB61293-56C6-6B41-AA59-0147276FA657.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/F2D8A5FA-4279-F041-8AB8-D635BB332878.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/39BF5018-3865-AD4E-A60A-741536196038.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/F437C1E9-F6D2-A147-B1B5-E34650123AF2.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/613D65BE-24BC-EF48-BF3A-8CF75DD9463D.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/7053CB9D-E331-A74A-B35D-022BAABA0C97.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/5791BFD1-74DC-4145-88EA-BBC909D169C9.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/109785D2-58EF-514B-9479-96E6D88CB523.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/B6C0CECB-9DFD-9A43-A758-12D69E24937A.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/29303C2D-7CE1-2641-905A-D748C02F3843.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/D6A460F0-184E-7B47-9F1B-42A53A4D6B0C.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/1F8294D4-12A1-854B-97CD-F6E207F6FF86.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/E09698A4-4779-3A4F-A534-3D2CAE1218BE.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/28FBC9A2-4B8D-0447-9E16-04996B78EDCF.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/DFF843CE-4A9C-BB47-89CA-1087792B76E1.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/D553C471-437E-FE42-A234-8A57846A1CAD.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/CD8AFEE7-4CD5-3344-BE5A-19D00F1B291B.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/34D95109-AC9F-F24A-AA8E-79D8138E091C.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/7260808F-7677-E84B-B72E-BBB28C35CFD2.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/C76A37DC-206F-2043-8B80-DC9C07FC8F50.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/4AADDFE0-ADC5-7C43-AC07-61BF5F6EECF3.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/3C10E5A6-9E4B-384A-93AE-F8F42B561353.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/2A00616C-4FB6-9946-8C0B-3354D9664608.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/A3B03FB7-8A50-0649-BBA5-6C49E2D359B5.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/E4C510A4-99D4-4646-B5CD-0B59BD5FC896.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/80593E01-BAA8-8340-8E3A-6AD1CD265975.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/D882EB7A-7302-904C-83D8-BE9E122571ED.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/245D14DC-AAC4-B843-927F-7027AAA89B76.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/5CC63434-9292-3E48-9153-AC0D495BB561.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/1E2EBC25-8AA4-8644-8BDB-A238FAFDFDAA.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/DED18A6C-7C26-2943-B2BD-7F3E5C162678.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/70845E9B-9B01-9345-B98C-A7806AA7E6B1.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/454FDA2F-04EC-1E40-923D-BA3E839BBEED.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/4C5F14FF-7088-2A4D-A0E6-BBC4B88B2832.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/7DE561E5-82D0-2D46-BA42-0285C7ADB361.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/4B4EF024-A613-FD47-BE19-4D2FF52DB454.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/590D8A3D-96D5-1246-BC96-CE1B33D12344.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/B670FB20-54E8-2440-8587-19687DC05A21.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/FC9C1104-CE8E-154E-A085-372B9714583C.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/F533A447-6ED6-6249-B08F-CCCF84B6BA93.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/9AE9F0E8-653C-5345-B4DC-9043F4A817AD.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/8EEE5FAB-27BD-E143-B20F-6B977888E34C.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/0CCB850E-C3FA-B648-905E-6CBF0F65CFF6.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/808F368E-9EE3-054A-9586-AF9CECC35FD1.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/1BEAEDBC-AF92-8C42-BECE-64584581D38B.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/E2D73234-A35B-3D43-94A3-DD97E40F37B2.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/2067BEBA-BC3B-9E48-B6B0-B0E4477BADFC.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/1358C4AC-DBE7-6240-AB1E-2E3FD968D63D.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/6813589C-C53A-684D-9E3E-7FBBFCF2A5E3.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/9266DAFD-7342-2945-8C94-0213080D3F1F.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/15ABEBF0-9861-CA44-BBAD-FD36D94EC9CC.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/68DF7669-A92A-0540-A3BB-C722741AC2B4.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/A5F30AF7-BBBA-B245-BA5A-537A574910E7.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/22192647-3180-4245-BE68-07735F677CEB.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/A94213F6-FB55-6242-8E11-CA3F62697A49.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/5459A5CA-067C-C947-AA03-F70A767A767E.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/06A92E27-EE0A-0343-B324-5B4197BA691D.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/2ADAB913-C6D5-4146-BDB1-B294840183AF.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/2239D7CD-C4B5-9A4C-B9D5-AD07B168828A.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/D5837836-F38B-EF45-AA7C-594E45C9B49F.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/F94CD2B6-202D-0947-AD7E-1EB959C748B6.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/ADB68D11-EB68-E54C-973E-5EEA982D4CBF.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/F3B4CF01-E5BD-7C43-89C2-B17ACB014102.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/D3B4DE30-AD74-0341-B7E3-E63C37DF2E6C.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/B3EEC2BA-8A8D-E947-8F87-16BD6F802B4C.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/7ACC7537-800E-F24F-B3E7-3AB68B28AF6A.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/BFDCF0F0-FD12-9F42-89AF-A94B660D9B49.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/16E6D7EB-3F8F-BD4F-A6B0-06908E63F99D.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/41AA84AC-20C0-0245-81FF-55DB77D91E54.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/8719E8B9-B9C6-BB4D-BD04-AA0B0833C720.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/F312AE19-E249-D647-80FF-C0A2ADDC5DD6.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/944A01D4-1C51-4D44-902C-B8DD1DD3F166.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/B960974F-0BA0-7947-A8A7-12EAB204C44C.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/3CEF96A1-CE27-4646-BD01-A7ED559F5DEE.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/040AF13C-880A-B84C-A996-235C9C1EFD48.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/7CABDDFA-DDBB-1949-8965-8FF7E867969F.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/346C6620-AC34-9B47-AF33-E404D4A7A712.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/795036FD-D5D2-8C44-9D33-F6A696959038.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/A934B834-133F-2744-B991-C72A7FF766EB.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/86D9E14C-C152-C84C-AB9E-06BFEF66A8BE.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/E497E5EC-526A-8144-BED3-861812BB2FF2.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/3C85A9AB-74EC-DD4F-A36C-0A7A06F76B2A.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/71D2450F-99C6-5F45-8A89-E41AF1F1044D.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/993BFD56-38EC-CD4E-BBBF-0CDF1BEC9D80.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/F1DAC883-40DD-3A40-9A75-7282EDAEBAF8.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/75B1FF41-28C0-0843-A10C-AAE27F88AC45.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/E8BA9AF4-7CE0-DC45-BE0E-2D560EF32409.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/CF19F2A8-0203-E84D-BC01-86370820B74D.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/A93A3AD8-BEB7-BC45-9897-798967277666.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/326B0E0A-EAD8-5F47-A338-8DCD7C074F6B.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/71D67237-0FC7-9746-B578-40E89DDA83AE.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/49A6CE79-DFA5-5B46-AD4A-EBB8688A30BA.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/37DDA41A-1F6A-6847-9B7F-E66DCE8EEA7E.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/57FFEBA0-090C-6945-ADD4-48A924E3756D.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/110B6EF1-B296-E449-A5D9-2DEC19893F05.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/BC4A738F-D458-1E48-9B5E-41735F9EBE1B.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/DDCAD252-3AA7-B54A-9B73-5E5DBFA6C90F.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/1272401A-99D1-A440-B7FA-E5F91EBC3D50.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/8FD949AF-741E-9747-8623-E0125A9661B7.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/6A355649-8C65-BB48-95C0-BB81995D2471.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/2B49369D-2B76-B24F-925E-F23165ECDE08.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/ADF10FF6-233E-2E4A-AC56-15DD01DB5C8F.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/16F2F55F-700D-1649-AD26-66AD04D2FAC8.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/62D8F97A-1E73-484B-B52F-D0C3BE47D0B9.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/92E300BE-706A-A448-91BE-47B5EAB8CF08.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/6077B50E-D836-6A4C-8449-2AAE4AC0267E.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/F2BE6AE5-2EC3-4041-B3AC-1E3D5B218ED4.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/7DB1ED28-2640-034C-9A47-C8496FF5E4AA.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/A91AF875-5049-2141-BE6F-C383F7CA7E28.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/697D37C2-5CBA-1D4A-B166-52F1621CC89A.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/C1532CA1-B87F-AF4A-A6AB-E3FF537CB489.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/BD88E668-8CDC-B747-A507-AC2AC01BFB2E.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/809003F6-CD1C-BF45-90DF-5DF833C28F08.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/C43A2EA0-F028-3144-BDC8-F8C214A7F927.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/75B65039-7110-7C49-B1DE-16156A6A6456.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/071D21A4-8C78-A845-A795-0A315F5310F2.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/A67D0D1F-99A1-9C44-82D6-18AEECA20250.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/409B3704-0CF1-1C4D-8B3B-8B4D4151EEA1.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/FF2C4164-56F2-864F-A25A-AA2C7F54F802.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/6B4B394C-7E24-C841-AE50-395379BB61D6.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/6E34D328-1748-AD43-BCC8-43084C7F8C76.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/C3FE7B35-F103-1D42-AE6D-5300500D63F7.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/7C30CC6A-2422-F242-8F07-FB35584C065B.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/C7721332-202C-B249-A7AC-8D18C9C78225.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/D9F3F5B8-C7F6-934D-AE27-69561B674D20.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/79D36E69-2277-F346-B535-10AF6ECCB2C9.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/AF484F83-2480-7D40-B624-9F6EDB02FA5E.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/EB2963CD-C012-5741-8546-B3DC62FD85DF.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/303C24F2-EAAA-DD4F-AC14-5E684756A59B.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/2AC5B9F2-7C70-9541-8D75-3852EED374B5.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/8018A38D-A756-CD40-AE66-3BFC8AB60919.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/6CFBA76F-9304-4042-9B0A-245FFDE44EFA.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/682A6050-CAEB-3B4C-BE41-2561FB4F8C6F.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/BC870D90-F56E-644C-A721-E4A36688B954.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/826A9AD2-8801-A34F-844F-2F97B236C41F.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/67CD4E92-FE35-3841-A099-E820B3792E19.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/92D53194-080B-D242-ACF2-3A6C97BD85A5.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/24C3A5BF-07A0-1B45-A26F-4AA4252EFD81.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/309969E4-FBF9-D14B-995D-5A05C39B109F.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/700A4F79-2252-0748-9070-09AC7A7AAD6B.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/7200D3BD-98F4-C948-8F4B-FE3890DBA7E0.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/405D69FB-2C9E-E04F-9DD3-1E682A1B61FF.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/62AB3F98-FD30-0742-AAD3-1B14A06CCAED.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/AEEF8A3A-87AA-4C41-BB37-221CD08019FE.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/864DB2BA-A03C-2C49-9A49-2100B61BA76C.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/487E421D-DAE3-B148-9E5D-84A3C01355FA.root', 
        '/store/mc/RunIIAutumn18DRPremix/WZ_TuneCP5_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v3/10000/E69711CB-BF20-A044-842D-08BDDE946577.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('--python_filename nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.MINIAODSIMEventContent.outputCommands.extend(cms.untracked.vstring(
    'keep *_displacedGlobalMuons_*_RECO',
    'keep *_displacedStandAloneMuons_*_RECO'
))


process.MINIAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('MINIAODSIM'),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(-900),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('file:RunIIAutumn18MiniAOD.root'),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideBranchesSplitLevel = cms.untracked.VPSet(
        cms.untracked.PSet(
            branch = cms.untracked.string('patPackedCandidates_packedPFCandidates__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('recoGenParticles_prunedGenParticles__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('patTriggerObjectStandAlones_slimmedPatTrigger__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('patPackedGenParticles_packedGenParticles__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('patJets_slimmedJets__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('recoVertexs_offlineSlimmedPrimaryVertices__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('recoCaloClusters_reducedEgamma_reducedESClusters_*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedEERecHits_*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('recoGenJets_slimmedGenJets__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('patJets_slimmedJetsPuppi__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedESRecHits_*'),
            splitLevel = cms.untracked.int32(99)
        )
    ),
    overrideInputFileSplitLevels = cms.untracked.bool(True),
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_upgrade2018_realistic_v15', '')

# Path and EndPath definitions
process.Flag_trackingFailureFilter = cms.Path(process.goodVertices+process.trackingFailureFilter)
process.Flag_goodVertices = cms.Path(process.primaryVertexFilter)
process.Flag_CSCTightHaloFilter = cms.Path(process.CSCTightHaloFilter)
process.Flag_trkPOGFilters = cms.Path(process.trkPOGFilters)
process.Flag_HcalStripHaloFilter = cms.Path(process.HcalStripHaloFilter)
process.Flag_trkPOG_logErrorTooManyClusters = cms.Path(~process.logErrorTooManyClusters)
process.Flag_EcalDeadCellTriggerPrimitiveFilter = cms.Path(process.EcalDeadCellTriggerPrimitiveFilter)
process.Flag_ecalLaserCorrFilter = cms.Path(process.ecalLaserCorrFilter)
process.Flag_globalSuperTightHalo2016Filter = cms.Path(process.globalSuperTightHalo2016Filter)
process.Flag_eeBadScFilter = cms.Path(process.eeBadScFilter)
process.Flag_METFilters = cms.Path(process.metFilters)
process.Flag_chargedHadronTrackResolutionFilter = cms.Path(process.chargedHadronTrackResolutionFilter)
process.Flag_globalTightHalo2016Filter = cms.Path(process.globalTightHalo2016Filter)
process.Flag_CSCTightHaloTrkMuUnvetoFilter = cms.Path(process.CSCTightHaloTrkMuUnvetoFilter)
process.Flag_HBHENoiseIsoFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseIsoFilter)
process.Flag_BadChargedCandidateSummer16Filter = cms.Path(process.BadChargedCandidateSummer16Filter)
process.Flag_hcalLaserEventFilter = cms.Path(process.hcalLaserEventFilter)
process.Flag_BadPFMuonFilter = cms.Path(process.BadPFMuonFilter)
process.Flag_ecalBadCalibFilter = cms.Path(process.ecalBadCalibFilter)
process.Flag_HBHENoiseFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseFilter)
process.Flag_trkPOG_toomanystripclus53X = cms.Path(~process.toomanystripclus53X)
process.Flag_EcalDeadCellBoundaryEnergyFilter = cms.Path(process.EcalDeadCellBoundaryEnergyFilter)
process.Flag_BadChargedCandidateFilter = cms.Path(process.BadChargedCandidateFilter)
process.Flag_trkPOG_manystripclus53X = cms.Path(~process.manystripclus53X)
process.Flag_BadPFMuonSummer16Filter = cms.Path(process.BadPFMuonSummer16Filter)
process.Flag_muonBadTrackFilter = cms.Path(process.muonBadTrackFilter)
process.Flag_CSCTightHalo2015Filter = cms.Path(process.CSCTightHalo2015Filter)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.MINIAODSIMoutput_step = cms.EndPath(process.MINIAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.Flag_HBHENoiseFilter,process.Flag_HBHENoiseIsoFilter,process.Flag_CSCTightHaloFilter,process.Flag_CSCTightHaloTrkMuUnvetoFilter,process.Flag_CSCTightHalo2015Filter,process.Flag_globalTightHalo2016Filter,process.Flag_globalSuperTightHalo2016Filter,process.Flag_HcalStripHaloFilter,process.Flag_hcalLaserEventFilter,process.Flag_EcalDeadCellTriggerPrimitiveFilter,process.Flag_EcalDeadCellBoundaryEnergyFilter,process.Flag_ecalBadCalibFilter,process.Flag_goodVertices,process.Flag_eeBadScFilter,process.Flag_ecalLaserCorrFilter,process.Flag_trkPOGFilters,process.Flag_chargedHadronTrackResolutionFilter,process.Flag_muonBadTrackFilter,process.Flag_BadChargedCandidateFilter,process.Flag_BadPFMuonFilter,process.Flag_BadChargedCandidateSummer16Filter,process.Flag_BadPFMuonSummer16Filter,process.Flag_trkPOG_manystripclus53X,process.Flag_trkPOG_toomanystripclus53X,process.Flag_trkPOG_logErrorTooManyClusters,process.Flag_METFilters,process.endjob_step,process.MINIAODSIMoutput_step)
process.schedule.associate(process.patTask)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions
#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllMC 

#call to customisation function miniAOD_customizeAllMC imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
