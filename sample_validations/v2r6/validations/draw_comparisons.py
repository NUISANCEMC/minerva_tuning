from ROOT import *

# draw_comparisons.py
# ----------------------------
# Quick script to load in NUISANCE outputs and compare to digitised original MC histograms
# run: python ./draw_comparisons
# Must be ran in the folder where digitised_minervaplots.root and combined_nuisanceplots.root is.

infile_official = TFile("digitised_minervaplots.root","READ")
infile_nuisance = TFile("combined_nuisanceplots.root","READ")

# List all combinrations
plotlist = []
plotlist.append( ["minerva_cc0pi1p_2015","MINERvA_CC0pi_XSec_1DQ2_nu_proton"])
plotlist.append( ["minerva_cc0piC_Q2",""])
plotlist.append( ["minerva_cc0piC_Q2ratio",""])
plotlist.append( ["minerva_cc0piFe_Q2",""])
plotlist.append( ["minerva_cc0piFe_Q2ratio",""])
plotlist.append( ["minerva_cc0piPb_Q2",""])
plotlist.append( ["minerva_cc0piPb_Q2ratio",""])
plotlist.append( ["minerva_cc1pi0angle_2016","MINERvA_CC1pi0_XSec_1Dthmu_antinu"])
plotlist.append( ["minerva_cc1pi0enu_2016","MINERvA_CC1pi0_XSec_1DEnu_antinu"])
plotlist.append( ["minerva_cc1pi0ke_2016","MINERvA_CC1pi0_XSec_1DTpi0_antinu"])
plotlist.append( ["minerva_cc1pi0muonmom_2016","MINERvA_CC1pi0_XSec_1Dpmu_antinu"])
plotlist.append( ["minerva_cc1pi0pionangle_2016","MINERvA_CC1pi0_XSec_1Dth_antinu_2016"])
plotlist.append( ["minerva_cc1pi0q2_2016","MINERvA_CC1pi0_XSec_1DQ2_antinu"])
plotlist.append( ["minerva_cc1pip_angle_2016","MINERvA_CC1pip_XSec_1Dthmu_nu_2017"])
plotlist.append( ["minerva_cc1pipangle_2016","MINERvA_CC1pip_XSec_1Dth_nu_2017"])
plotlist.append( ["minerva_cc1pipenu_2016","MINERvA_CC1pip_XSec_1DEnu_nu_2017"])
plotlist.append( ["minerva_cc1pipke_2016","MINERvA_CC1pip_XSec_1DTpi_nu_2017"])
plotlist.append( ["minerva_cc1pipmuonmom_2016","MINERvA_CC1pip_XSec_1Dpmu_nu_2017"])
plotlist.append( ["minerva_cc1pipq2_2016","MINERvA_CC1pip_XSec_1DQ2_nu_2017"])
plotlist.append( ["minerva_cc1piptpi_eberly","MINERvA_CC1pip_XSec_1DTpi_nu"])
plotlist.append( ["minerva_ccinceav2D_284_slice1",""])
plotlist.append( ["minerva_ccinceav2D_284_slice2",""])
plotlist.append( ["minerva_ccinceav2D_284_slice3",""])
plotlist.append( ["minerva_ccinceav2D_284_slice4",""])
plotlist.append( ["minerva_ccinceav2D_284_slice5",""])
plotlist.append( ["minerva_ccinceav2D_284_slice6",""])
plotlist.append( ["minerva_ccnpipangle_eberly","MINERvA_CCNpip_XSec_1Dth_nu"])
plotlist.append( ["minerva_ccnpiptpi_eberly","MINERvA_CCNpip_XSec_1DTpi_nu"])
plotlist.append( ["minerva_cohenu_numu","MINERvA_CCCOHPI_XSec_1DEnu_nu"])
plotlist.append( ["minerva_cohenu_numubar","MINERvA_CCCOHPI_XSec_1DEnu_antinu"])
plotlist.append( ["minerva_cohthetapinumu","MINERvA_CCCOHPI_XSec_1Dth_nu"])
plotlist.append( ["minerva_cohthetapinumubar","MINERvA_CCCOHPI_XSec_1Dth_antinu"])
plotlist.append( ["minerva_cohtpinumu","MINERvA_CCCOHPI_XSec_1DEpi_nu"])
plotlist.append( ["minerva_cohtpinumubar","MINERvA_CCCOHPI_XSec_1Dth_antinu"])
plotlist.append( ["minerva_nueee","MINERvA_CC0pi_XSec_1DEe_nue"])
plotlist.append( ["minerva_nueq2","MINERvA_CC0pi_XSec_1DQ2_nue"])
plotlist.append( ["minerva_nueratio",""])
plotlist.append( ["minerva_nuethetae","MINERvA_CC0pi_XSec_1Dthetae_nue"])
plotlist.append( ["minerva_numu_cc1pipangle_eberly","MINERvA_CC1pip_XSec_1Dth_nu"])
plotlist.append( ["minerva_numu_ccqe","MINERvA_CCQE_XSec_1DQ2_nu"])
plotlist.append( ["minerva_nubar_ccqe","MINERvA_CCQE_XSec_1DQ2_antinu"])
plotlist.append( ["minerva_numu_ccincratio_enuC","MINERvA_CCinc_XSec_1DEnu_ratio_C12_CH"])
plotlist.append( ["minerva_numu_ccincratio_enuFe","MINERvA_CCinc_XSec_1DEnu_ratio_Fe56_CH"])
plotlist.append( ["minerva_numu_ccincratio_enuPb","MINERvA_CCinc_XSec_1DEnu_ratio_Pb208_CH"])
plotlist.append( ["minerva_numu_ccincratio_xC","MINERvA_CCinc_XSec_1Dx_ratio_C12_CH"])
plotlist.append( ["minerva_numu_ccincratio_xFe","MINERvA_CCinc_XSec_1Dx_ratio_Fe56_CH"])
plotlist.append( ["minerva_numu_ccincratio_xPb","MINERvA_CCinc_XSec_1Dx_ratio_Pb208_CH"])
plotlist.append( ["minerva_numub_ccpi0anglepi_2015","MINERvA_CC1pi0_XSec_1Dth_antinu_2015"])
plotlist.append( ["minerva_numub_ccpi0ppi_2015","MINERvA_CC1pi0_XSec_1Dppi0_antinu"])
plotlist.append( ["minerva_nueee","MINERvA_CC0pi_XSec_1DEe_nue"])
plotlist.append( ["minerva_nueq2","MINERvA_CC0pi_XSec_1DQ2_nue"])
plotlist.append( ["minerva_nueratio",""])
plotlist.append( ["minerva_nuethetae","MINERvA_CC0pi_XSec_1DThetae_nue"])


for i, names in enumerate(plotlist):
    print names
    if "cc1pip" not in names[0]: continue
    data_nuisance = infile_nuisance.Get(names[1] + "_data")
    if not data_nuisance: continue
    mc_nuisance = infile_nuisance.Get(names[1] + "_MC")
    mc_fine = infile_nuisance.Get(names[1] + "_MC_FINE")

    data_nuisance.Draw("E1")
    data_nuisance.GetYaxis().SetRangeUser(0.0,data_nuisance.GetMaximum()*1.5)
    data_nuisance.SetTitle(names[0])

    data_nuisance.SetLineColor(kBlack)
    data_nuisance.SetLineWidth(2)

    mc_nuisance.SetTitle("NUISANCE")
    mc_nuisance.Draw("SAME HIST C")
    mc_nuisance.SetLineColor(kBlue)
    mc_nuisance.SetLineWidth(2)

    mc_fine.SetTitle("NUIS-FINE")
    mc_fine.Draw("SAME HIST C")
    mc_fine.SetLineColor(kCyan)
    mc_fine.SetLineWidth(1)

    mc_minerva = infile_official.Get(names[0])
    mc_minerva.SetTitle("Original")
    mc_minerva.Draw("SAME PL")
    mc_minerva.SetLineColor(kRed)
    mc_minerva.SetLineStyle(7)
    mc_minerva.SetLineWidth(2)

    gPad.BuildLegend()

    gPad.Update()
    gPad.SaveAs("figures/" + names[0] + "_comp.png")

