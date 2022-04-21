#!/bin/bash
ulimit -s unlimited
set -e
cd /home/users/fsetti/HHggTauTau/coupling_scan/CMSSW_10_2_13/src
export SCRAM_ARCH=slc7_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
cd /home/users/fsetti/HHggTauTau/coupling_scan/CMSSW_10_2_13/src/flashggFinalFit/Datacard
export PYTHONPATH=$PYTHONPATH:/home/users/fsetti/HHggTauTau/coupling_scan/CMSSW_10_2_13/src/flashggFinalFit/tools:/home/users/fsetti/HHggTauTau/coupling_scan/CMSSW_10_2_13/src/flashggFinalFit/Datacard/tools

python /home/users/fsetti/HHggTauTau/coupling_scan/CMSSW_10_2_13/src/flashggFinalFit/Datacard/makeYields.py --cat SR1 --procs ggHHkl0kt1,ggHHkl1kt1,ggHHkl2p45kt1,ggHHkl5kt1,ggHHkl0kt1WWdilep,ggHHkl1kt1WWdilep,ggHHkl2p45kt1WWdilep,ggHHkl5kt1WWdilep,ggH,ttH,VH,VBFH --ext 12Apr2022_noSyst --mass 125 --inputWSDirMap 2016=/home/users/fsetti/HHggTauTau/coupling_scan/CMSSW_10_2_13/src/flashggFinalFit/files_systs/12Apr2022_noSyst//ws_signal_2016,2017=/home/users/fsetti/HHggTauTau/coupling_scan/CMSSW_10_2_13/src/flashggFinalFit/files_systs/12Apr2022_noSyst//ws_signal_2017,2018=/home/users/fsetti/HHggTauTau/coupling_scan/CMSSW_10_2_13/src/flashggFinalFit/files_systs/12Apr2022_noSyst//ws_signal_2018 --sigModelWSDir ./Models/signal --sigModelExt packaged --bkgModelWSDir ./Models/background --bkgModelExt multipdf  --mergeYears
