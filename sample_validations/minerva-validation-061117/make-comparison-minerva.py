from ROOT import *
import sys

def ConvertNameOfficial(name):
    return name

def MakeTH1Figure(names,files):

    name_official = names[0]
    file_official = files[0]
    mc_official = file_official.Get(name_official)

    name_nuisance = names[1]
    file_nuisance = files[1]
    data_nuisance = infile_nuisance.Get(name_nuisance + "_data")
    mc_nuisance   = infile_nuisance.Get(name_nuisance + "_MC")
    mc_fine       = infile_nuisance.Get(name_nuisance + "_MC_FINE")

    data_nuisance.SetLineColor(kBlack)
    data_nuisance.SetMarkerStyle(20)
    data_nuisance.SetMarkerSize(0.6)
    data_nuisance.SetLineWidth(2)
    if data_nuisance.GetMaximum() > 0.5:
        data_nuisance.GetYaxis().SetRangeUser(0.6,data_nuisance.GetMaximum()*2.5)
    else:
        data_nuisance.GetYaxis().SetRangeUser(0.0,data_nuisance.GetMaximum()*2.0)
    data_nuisance.SetTitle(ConvertNameOfficial(name_official))
    data_nuisance.Draw("E1")

    mc_nuisance.SetTitle("NUISANCE")
    mc_nuisance.SetLineColor(kBlue)
    mc_nuisance.SetLineWidth(2)
    if data_nuisance.GetMaximum() > 0.5:
        mc_nuisance.Draw("SAME E1")
    else:
        mc_nuisance.Draw("SAME HIST C")

    mc_fine.SetTitle("NUISANCE (FINE)")
    mc_fine.SetLineColor(kCyan)
    mc_fine.SetLineWidth(1)
    mc_fine.Draw("SAME HIST C")

    mc_official.SetTitle("Original")
    mc_official.SetLineColor(kRed)
    mc_official.SetLineStyle(7)
    mc_official.SetLineWidth(2)
    mc_official.Draw("SAME PL")

    gPad.BuildLegend(0.5,0.5,0.82,0.85)

    data_nuisance.SetTitle(name_nuisance)
    gStyle.SetOptTitle(1)

    gPad.Update()
    gPad.SaveAs("figures/" + name_official + "_comp.png")

    return "figures/" + name_official + "_comp.png"

def PrintInfo(names,files):
    name_official = names[0]
    name_nuisance = names[1]
    file_nuisance = files[1]
    info_nuisance = infile_nuisance.Get(name_nuisance + "_settings")
    
    if not info_nuisance: return ""
    
    info_nuisance.GetListOfPrimitives().At(0).SetTextSize(0.03)
    info_nuisance.GetListOfPrimitives().At(1).SetTextSize(0.03)

    info_nuisance.Draw()
    gPad.Update()
    gPad.SaveAs("figures/" + name_official + "_info.png")

    return "figures/" + name_official + "_info.png"
if __name__=="__main__":

    filename_nuisance = sys.argv[1]
    infile_official = TFile("original-minerva-mcplots.root","READ")
    infile_nuisance = TFile(filename_nuisance,"READ")
    filelist = []
    filelist.append(infile_official)
    filelist.append(infile_nuisance)

    plotlist = []
    plotlist.append( ["minerva_numu_ccqe","MINERvA_CCQE_XSec_1DQ2_nu"])
    plotlist.append( ["minerva_nubar_ccqe","MINERvA_CCQE_XSec_1DQ2_antinu"])

    plotlist.append( ["minerva_cc0pi1p_2015","MINERvA_CC0pi_XSec_1DQ2_nu_proton"])
    plotlist.append( ["minerva_cc0piC_Q2",""])
    plotlist.append( ["minerva_cc0piC_Q2ratio",""])
    plotlist.append( ["minerva_cc0piFe_Q2",""])
    plotlist.append( ["minerva_cc0piFe_Q2ratio",""])
    plotlist.append( ["minerva_cc0piPb_Q2",""])
    plotlist.append( ["minerva_cc0piPb_Q2ratio",""])

    plotlist.append( ["minerva_nueee","MINERvA_CC0pi_XSec_1DEe_nue"])
    plotlist.append( ["minerva_nueq2","MINERvA_CC0pi_XSec_1DQ2_nue"])
    plotlist.append( ["minerva_nueratio",""])
    plotlist.append( ["minerva_nuethetae","MINERvA_CC0pi_XSec_1Dthetae_nue"])

    plotlist.append( ["minerva_numu_cc1pipangle_eberly","MINERvA_CC1pip_XSec_1Dth_nu"])
    plotlist.append( ["minerva_numu_cc1pipangle_eberly","MINERvA_CC1pip_XSec_1Dth_nu"])
    plotlist.append( ["minerva_cc1piptpi_eberly","MINERvA_CC1pip_XSec_1DTpi_nu"])
    
    plotlist.append( ["minerva_cc1pip_angle_2016","MINERvA_CC1pip_XSec_1Dthmu_nu_2017"])
    plotlist.append( ["minerva_cc1pipangle_2016","MINERvA_CC1pip_XSec_1Dth_nu_2017"])
    plotlist.append( ["minerva_cc1pipenu_2016","MINERvA_CC1pip_XSec_1DEnu_nu_2017"])
    plotlist.append( ["minerva_cc1pipke_2016","MINERvA_CC1pip_XSec_1DTpi_nu_2017"])
    plotlist.append( ["minerva_cc1pipmuonmom_2016","MINERvA_CC1pip_XSec_1Dpmu_nu_2017"])
    plotlist.append( ["minerva_cc1pipq2_2016","MINERvA_CC1pip_XSec_1DQ2_nu_2017"])

    plotlist.append( ["minerva_ccnpipangle_eberly","MINERvA_CCNpip_XSec_1Dth_nu"])
    plotlist.append( ["minerva_ccnpiptpi_eberly","MINERvA_CCNpip_XSec_1DTpi_nu"])

    plotlist.append( ["minerva_numub_ccpi0anglepi_2015","MINERvA_CC1pi0_XSec_1Dth_antinu_2015"])
    plotlist.append( ["minerva_numub_ccpi0ppi_2015","MINERvA_CC1pi0_XSec_1Dppi0_antinu"])
    plotlist.append( ["minerva_cc1pi0angle_2016","MINERvA_CC1pi0_XSec_1Dthmu_antinu"])
    plotlist.append( ["minerva_cc1pi0enu_2016","MINERvA_CC1pi0_XSec_1DEnu_antinu"])
    plotlist.append( ["minerva_cc1pi0ke_2016","MINERvA_CC1pi0_XSec_1DTpi0_antinu"])
    plotlist.append( ["minerva_cc1pi0muonmom_2016","MINERvA_CC1pi0_XSec_1Dpmu_antinu"])
    plotlist.append( ["minerva_cc1pi0pionangle_2016","MINERvA_CC1pi0_XSec_1Dth_antinu_2016"])
    plotlist.append( ["minerva_cc1pi0q2_2016","MINERvA_CC1pi0_XSec_1DQ2_antinu"])

    plotlist.append( ["minerva_cohenu_numu","MINERvA_CCCOHPI_XSec_1DEnu_nu"])
    plotlist.append( ["minerva_cohthetapinumu","MINERvA_CCCOHPI_XSec_1Dth_nu"])
    plotlist.append( ["minerva_cohtpinumu","MINERvA_CCCOHPI_XSec_1DEpi_nu"])

    plotlist.append( ["minerva_cohenu_numubar","MINERvA_CCCOHPI_XSec_1DEnu_antinu"])
    plotlist.append( ["minerva_cohthetapinumubar","MINERvA_CCCOHPI_XSec_1Dth_antinu"])
    plotlist.append( ["minerva_cohtpinumubar","MINERvA_CCCOHPI_XSec_1DEpi_antinu"])

    plotlist.append( ["minerva_ccinceav2D_284","MINERvA_CCinc_XSec_2DEavq3_nu","Y"])

    plotlist.append( ["minerva_numu_ccincratio_enuC","MINERvA_CCinc_XSec_1DEnu_ratio_C12_CH"])
    plotlist.append( ["minerva_numu_ccincratio_enuFe","MINERvA_CCinc_XSec_1DEnu_ratio_Fe56_CH"])
    plotlist.append( ["minerva_numu_ccincratio_enuPb","MINERvA_CCinc_XSec_1DEnu_ratio_Pb208_CH"])
    
    plotlist.append( ["minerva_numu_ccincratio_xC","MINERvA_CCinc_XSec_1Dx_ratio_C12_CH"])
    plotlist.append( ["minerva_numu_ccincratio_xFe","MINERvA_CCinc_XSec_1Dx_ratio_Fe56_CH"])
    plotlist.append( ["minerva_numu_ccincratio_xPb","MINERvA_CCinc_XSec_1Dx_ratio_Pb208_CH"])

    
    allhist = []
    allinfo = []
    
    for i, names in enumerate(plotlist):

        data_nuisance = infile_nuisance.Get(names[1] + "_data")
        if not data_nuisance: continue

        hist = ""
        if "TH2" in str(type(data_nuisance)): print "TH2D"
        else: hist = MakeTH1Figure(names,filelist)
        info = PrintInfo(names,filelist)

        allhist.append(hist)
        allinfo.append(info)
    

    # Now Make a Latex Document
    f = open(filename_nuisance.replace(".root","")+".tex","w")
    f.write("\\documentclass{article}\n")
    f.write("\\usepackage{graphicx}\n")
    f.write("\\usepackage[margin=0.4in]{geometry}\n")
    f.write("\\usepackage{morefloats}\n")
    f.write("\\begin{document}\n")
    for i in range(len(allhist)):
        
        if allhist[i] == "": continue

#        f.write("\\begin{figure}[H!]\n")
        f.write("\\centering\n")
        f.write("\\includegraphics[width=0.49\\textwidth]{" + allhist[i] + "}\n")
        if allinfo[i] != "":
            f.write("\\includegraphics[width=0.49\\textwidth]{" + allinfo[i] + "}\n")
        else:
            f.write("\\\\")
#        f.write("\\end{figure}\n")
        f.write("")
        
    f.write("\\end{document}\n")
