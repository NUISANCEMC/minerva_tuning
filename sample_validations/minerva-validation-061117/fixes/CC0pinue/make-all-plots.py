from ROOT import *
import sys

def ConvertNameOfficial(name):
    return name

def GetSliceX(plot, index):
    
    return plot.ProjectionX(plot.GetName() + "_sliceX_" + str(index),
                            index+1,index+1)
                                
def GetSliceY(plot, index):
    
    return plot.ProjectionY(plot.GetName() + "_sliceY_"+ str(index),
                            index+1,index+1)


def MakeTH2Figure(names,files):
    
    name_official = names[0]

    name_nuisance = names[1]
    file_nuisance = files[0]
    data_nuisance = infile_nuisance.Get(name_nuisance + "_data")
    mc_nuisance   = infile_nuisance.Get(name_nuisance + "_MC")
    
    SliceDim = "Y"
    HistNames = []
    if SliceDim == "Y":
        for i in range(data_nuisance.GetNbinsX()):
            data_nuisance_slice = GetSliceY(data_nuisance,i)
            data_nuisance_slice.SetLineColor(kBlack)
            data_nuisance_slice.SetMarkerStyle(20)
            data_nuisance_slice.SetMarkerSize(0.6)
            data_nuisance_slice.SetLineWidth(2)
            data_nuisance_slice.SetTitle(ConvertNameOfficial(name_official))
            data_nuisance_slice.GetYaxis().SetRangeUser(0.0, data_nuisance_slice.GetMaximum()*2.0)
            data_nuisance_slice.Draw("E1")

            mc_nuisance_slice = GetSliceY(mc_nuisance,i)
            mc_nuisance_slice.SetTitle("NUISANCE")
            mc_nuisance_slice.SetLineColor(kBlue)
            mc_nuisance_slice.SetLineWidth(2)
            mc_nuisance_slice.Draw("SAME HIST")

            gPad.Update()
            gPad.BuildLegend(0.5,0.5,0.82,0.85)

            data_nuisance_slice.SetTitle(name_nuisance)
            gStyle.SetOptTitle(1)
            
            gPad.Update()
            gPad.SaveAs("figures/nuisance_" + name_official + "_slice_" + str(i) + "_comp.png")
            HistNames.append("figures/nuisance_" + name_official + "_slice_" + str(i) + "_comp.png")
    
    elif SliceDim == "X":
        for i in range(data_nuisance.GetNbinsY()):
            data_nuisance_slice = GetSliceX(data_nuisance,i)
            data_nuisance_slice.SetLineColor(kBlack)
            data_nuisance_slice.SetMarkerStyle(20)
            data_nuisance_slice.SetMarkerSize(0.6)
            data_nuisance_slice.SetLineWidth(2)
            data_nuisance_slice.SetTitle(ConvertNameOfficial(name_official))
            data_nuisance_slice.GetYaxis().SetRangeUser(0.0, data_nuisance_slice.GetMaximum()*2.0)
            data_nuisance_slice.Draw("E1")

            mc_nuisance_slice = GetSliceX(mc_nuisance,i)
            mc_nuisance_slice.SetTitle("NUISANCE")
            mc_nuisance_slice.SetLineColor(kBlue)
            mc_nuisance_slice.SetLineWidth(2)
            mc_nuisance_slice.Draw("SAME HIST")

            gPad.Update()
            gPad.BuildLegend(0.5,0.5,0.82,0.85)

            data_nuisance_slice.SetTitle(name_nuisance)
            gStyle.SetOptTitle(1)

            gPad.Update()
            gPad.SaveAs("figures/nuisance_" + name_official + "_slice_" + str(i) + "_comp.png")
            HistNames.append("figures/nuisance_" + name_official + "_slice_" + str(i) + "_comp.png")

    return HistNames



def MakeTH1Figure(names,files):

    name_official = names[0]
    name_nuisance = names[1]
    file_nuisance = files[0]
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

    gPad.BuildLegend(0.5,0.5,0.82,0.85)

    data_nuisance.SetTitle(name_nuisance)
    gStyle.SetOptTitle(1)

    gPad.Update()
    gPad.SaveAs("figures/nuisance_" + name_official + "_comp.png")

    return "figures/nuisance_" + name_official + "_comp.png"

def PrintInfo(names,files):
    name_official = names[0]
    name_nuisance = names[1]
    file_nuisance = files[0]
    info_nuisance = infile_nuisance.Get(name_nuisance + "_settings")
    
    if not info_nuisance: return ""
    
    info_nuisance.GetListOfPrimitives().At(0).SetTextSize(0.03)
    info_nuisance.GetListOfPrimitives().At(1).SetTextSize(0.03)

    info_nuisance.Draw()
    gPad.Update()
    gPad.SaveAs("figures/nuisance_" + name_official + "_info.png")

    return "figures/nuisance_" + name_official + "_info.png"

if __name__=="__main__":

    filename_nuisance = sys.argv[1]
    infile_nuisance = TFile(filename_nuisance,"READ")
    filelist = []
    filelist.append(infile_nuisance)

    plotlist = []
    for keys in infile_nuisance.GetListOfKeys():
        keyname = keys.GetName()
        if not keyname.endswith("_data"): continue
        plotlist.append( [keyname.replace("_data",""), keyname.replace("_data","")] )

    allhist = []
    allinfo = []
    
    for i, names in enumerate(plotlist):

        data_nuisance = infile_nuisance.Get(names[1] + "_data")
        if not data_nuisance: continue
        
        hist = ""
        info = PrintInfo(names,filelist)
        if "TH2" in str(type(data_nuisance)): 
            hists = MakeTH2Figure(names,filelist)
            for hist in hists:
                allhist.append(hist)
                allinfo.append(info)
        else: 
            hist = MakeTH1Figure(names,filelist)
            allhist.append(hist)
            allinfo.append(info)


    # Now Make a Latex Document
    f = open(filename_nuisance.replace(".root","")+"-allnuisanceplots.tex","w")
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
