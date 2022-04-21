# Python file to store systematics: for STXS analysis

# Comment out all nuisances that you do not want to include

# THEORY SYSTEMATICS:

# For type:constant
#  1) specify same value for all processes
#  2) define process map json in ./theory_uncertainties (add process names where necessary!)

# For type:factory
# Tier system: adds different uncertainties to dataframe
#   1) shape: absolute yield of process kept constant, shape effects i.e. calc migrations across cats
#   2) ishape: as (1) but absolute yield for proc x cat is allowed to vary
#   3) norm: absolute yield of production mode (s0) kept constant but migrations across sub-processes e.g. STXS bins.Same value in each category.
#   4) inorm: as (3) but absolute yield of production mode (s0) can vary
#   5) inc: variations in production mode (s0), same value for each subprocess in each category
# Relations: shape = ishape/inorm
#            norm  = inorm/inc
# Specify as list in dict: e.g. 'tiers'=['inc','inorm','norm','ishape','shape']

theory_systematics = [
                # Normalisation uncertainties: enter interpretations
                {'name':'BR_hgg','title':'BR_hgg','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':"0.98/1.021"},
]
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# EXPERIMENTAL SYSTEMATICS
# correlateAcrossYears = 0 : no correlation
# correlateAcrossYears = 1 : fully correlated
# correlateAcrossYears = -1 : partially correlated

experimental_systematics = [
                # Updated luminosity partial-correlation scheme: 13/5/21 (recommended simplified nuisances)
                {'name':'lumi_13TeV_Uncorrelated','title':'lumi_13TeV_Uncorrelated','type':'constant','prior':'lnN','correlateAcrossYears':0,'value':{'2016':'1.010','2017':'1.020','2018':'1.015'}},
                {'name':'lumi_13TeV_Correlated','title':'lumi_13TeV_Correlated','type':'constant','prior':'lnN','correlateAcrossYears':-1,'value':{'2016':'1.006','2017':'1.009','2018':'1.020'}},
                {'name':'lumi_13TeV_Correlated_1718','title':'lumi_13TeV_Correlated_1718','type':'constant','prior':'lnN','correlateAcrossYears':-1,'value':{'2016':'-','2017':'1.006','2018':'1.002'}},
                {'name':'weight_electron_veto_sf_Diphoton_Photon','title':'CMS_hgg_electronVetoSF','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'weight_electron_id_sf_SelectedElectron','title':'CMS_hgg_ElectronIDSF','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'weight_muon_id_sfSTAT_SelectedMuon','title':'CMS_hgg_MuonIDSF_STAT','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'weight_muon_id_sfSYS_SelectedMuon','title':'CMS_hgg_MuonIDSF_SYS','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'weight_trigger_sf','title':'CMS_hgg_TriggerSF','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'JER','title':'JER','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'JES','title':'JES','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'MET_JER','title':'MET_JER','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'MET_JES','title':'MET_JES','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'MET_Unclustered','title':'MET_Unclustered','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'Muon_pt','title':'Muon_pt','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'Tau_pt','title' :'Tau_pt','type':'factory','prior':'lnN','correlateAcrossYears':0},
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Shape nuisances: effect encoded in signal model
# mode = (other,scalesGlobal,scales,scalesCorr,smears): match the definition in the signal models

signal_shape_systematics = [
                {'name':'MCScale_scale','title':'MCScale_scale','type':'signal_shape','mode':'scales','mean':'0.0','sigma':'1.0'},
                {'name':'material','title':'material','type':'signal_shape','mode':'scalesCorr','mean':'0.0','sigma':'1.0'},
                {'name':'fnuf','title':'fnuf','type':'signal_shape','mode':'scalesCorr','mean':'0.0','sigma':'1.0'},
]
