from ROOT import *
import sys

outfile = TFile("original-minerva-mcplots.root","RECREATE")
outfile.cd()
for i in xrange(1,len(sys.argv)):
    print i
    gr = TGraph(sys.argv[i],"%lg %lg",",")
    gr.Draw("APL")

    gr.SetLineWidth(2)
    gr.SetLineColor(kRed)
    gr.SetTitle("Official GENIE")
    gr.Write(sys.argv[i].replace(".txt",""))

    gPad.Update()
    gPad.SaveAs((sys.argv[i].replace(".txt","")+"_graph.pdf"))
