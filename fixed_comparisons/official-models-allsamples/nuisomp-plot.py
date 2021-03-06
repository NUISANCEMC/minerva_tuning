from ROOT import *
import os
import sys
import argparse

GLOBALLIST = []

# Get Likelihood
def GetLikelihood(filename, uid):
    like = -999.9

    # Open input file
    inputfile = TFile(filename,"READ")
    if not inputfile or inputfile.IsZombie():
        print "Cannot find file : ", filename
        sys.exit(1)

    # Get Likehist Value
    likehist = inputfile.Get("likelihood_hist")
    for i in range(likehist.GetNbinsX()):
        if uid == likehist.GetXaxis().GetBinLabel(i+1):
            like = likehist.GetBinContent(i+1)

    # Close
    inputfile.Close()

    return round(like,1)

# Get NDOF
def GetNDOF(filename, uid):
    ndof = -999

    # Open input file
    inputfile = TFile(filename,"READ")
    if not inputfile or inputfile.IsZombie():
        print "Cannot find file : ", filename
        sys.exit(1)

    # Get Likehist Value
    ndofhist = inputfile.Get("ndof_hist")
    for i in range(ndofhist.GetNbinsX()):
        if uid == ndofhist.GetXaxis().GetBinLabel(i+1):
            ndof = ndofhist.GetBinContent(i+1)

    # Close
    inputfile.Close()

    return int(ndof)


def PrettyUID(uid):

    uid = uid.replace("MINERvA_","")
    uid = uid.replace("_nu","_#nu")
    uid = uid.replace("_antinu","_#bar{#nu}")
    uid = uid.replace("CC1pip","CC-1#pi^{+}")
    uid = uid.replace("CC1pi0","CC-1#pi^{0}")
    uid = uid.replace("CCNpip","CC-N#pi^{+}")
    uid = uid.replace("CCCOHPI","CC-Coh")
    uid = uid.replace("CC0pi","CC-0#pi")
    uid = uid.replace("CCDIS","CC-DIS")
    uid = uid.replace("_20deg","_#theta<20#circ")
    uid = uid.replace("_1DQ2","")
    uid = uid.replace("_1DEpi","")
    uid = uid.replace("_1DTpi","")
    uid = uid.replace("_1Dthpi","")
    uid = uid.replace("_1Dthmu","")
    uid = uid.replace("_1Dth","")
    uid = uid.replace("_1DEnu","")
    uid = uid.replace("_TgtCH","_CH")
    uid = uid.replace("_TgtC","_C")
    uid = uid.replace("_TgtFe","_Fe")
    uid = uid.replace("_TgtPb","_Pb")
    uid = uid.replace("_XSec","")
    uid = uid.replace("C12_CH","C/CH")
    uid = uid.replace("Fe56_CH","Fe/CH")
    uid = uid.replace("Pb208_CH","Pb/CH")
    uid = uid.replace("TgtRatioC","C/CH")
    uid = uid.replace("TgtRatioFe","Fe/CH")
    uid = uid.replace("TgtRatioPb","Pb/CH")
    print uid
    return uid.replace("_"," ")

def StyleData(hist,style,uid):
    
    if style == "data":

        hist.SetMarkerStyle(20)
        hist.SetMarkerColor(kBlack)
        hist.SetMarkerSize(0.7)

        hist.SetLineWidth(2)
        hist.SetLineColor(kBlack)

        hist.SetTitle(PrettyUID(uid))
        
    return hist

def StyleTH1D(hist,style,args,i,uid):

    if style == "mc":

        hist.SetMarkerStyle(0)
        
        hist.SetLineWidth(2)
        hist.SetLineColor(eval(args.colours[i]))
        
        like = GetLikelihood(args.files[i],uid)
        ndof = GetNDOF(args.files[i],uid)
        hist.SetTitle( args.labels[i] + " (" + str(like) + "/" + str(ndof) + ")" )


    return hist

def GetSliceX(plot, index):
    newplot = plot.Clone(plot.GetName() + "_tempX_"+ str(index))
    return newplot.ProjectionX(plot.GetName() + "_sliceX_"+ str(index),
                               index+1,index+1)

def GetSliceY(plot, index):
    
    newplot = plot.Clone(plot.GetName() + "_tempY_"+ str(index))
    return newplot.ProjectionY(plot.GetName() + "_sliceY_"+ str(index),
                               index+1,index+1)


# GetObject
# Returns TObject but also allows _tag request
# _____________________________________________
def GetObject(filename, uid, tag="", args=None):

    # Open input file
    inputfile = TFile(filename,"READ")
    if not inputfile or inputfile.IsZombie():
        print "Cannot find file : ", filename
        sys.exit(1)

    # Make name string
    objstring = uid
    if tag != "": objstring += "_" + tag

    # Get Object
    obj = inputfile.Get(objstring)
    # Check object Valid
    if not obj: 
        print "Cannot find TObject : ", objstring
        sys.exit(1)

    # Clone Object
    localobj = obj.Clone(uid + obj.GetName())
    localobj.SetDirectory(0)

    # Close file
    inputfile.Close()

    # Determine if we need to slice
    if args.xslice != None:
        return GetSliceX(localobj, args.xslice)

    if args.yslice != None:
        return GetSliceY(localobj, args.yslice)
        
    # Return
    return localobj
    


# Draw_MC
# Draws simple *_data *_MC plots
# _____________________________________________
def Draw_DATAMC(args,xargs,uid):

    # Determine Type
    ndim = 0
    for f in Args.files:
        data = GetObject(f, uid, "data",args)
        ndim = data.GetDimension()

    if ndim == 1: Draw_DATAMC_1D(args,xargs,uid)
    elif ndim == 2: Draw_DATAMCSHAPE_2D(args,xargs,uid)

    return


# Draw DATAMC_1D
# Draw simple *_data *_MC plots for TH1D
# _____________________________________________
def Draw_DATAMC_1D(args,xargs,uid):

    # Loop over files and get all plots
    DataPlots = []
    MCPlots   = []
    for f in Args.files:
        DataPlots.append(GetObject(f, uid, "data",args))
        MCPlots.append(GetObject(f,uid,"MC",args))

    # GetRange
    ymin = 1E9
    ymax = -1E9
    for plot in DataPlots:
        ymin = min([ymin, plot.GetMinimum()])
        ymax = max([ymax, plot.GetMaximum()])
    for plot in MCPlots:
        ymin = min([ymin, plot.GetMinimum()])
        ymax = max([ymax, plot.GetMaximum()])
    yrange = ymax - ymin

    # Now Draw
    DataMain = StyleData(DataPlots[0],"data", uid)
    DataMain.Draw("E1")
    for i, plot in enumerate(MCPlots):
        StyleTH1D(MCPlots[i],"mc",args,i,uid)
        MCPlots[i].Draw("SAME HIST C")

    # Set Range
    if yrange > 1E-10:
        DataMain.GetYaxis().SetRangeUser(ymin - yrange*1.0, ymax + yrange*1.0)
    else:
        DataMain.GetYaxis().SetRangeUser(0.0, ymax + yrange*0.8)

    # Build Legend
    leg = gPad.BuildLegend(0.38,0.88 - len(MCPlots)*0.07, 0.82,0.88)
    leg.SetTextSize(0.04)

    GLOBALLIST.append([DataPlots, MCPlots])
    gPad.Update()
    return

# _____________________________________________
def Draw_DATAMCSHAPE(args,xargs,uid):

    # Determine Type
    args.xslice = None
    args.yslice = None

    ndim = 0
    for f in Args.files:
        data = GetObject(f, uid, "data",args)
        ndim = data.GetDimension()

    if ndim == 1: Draw_DATAMCSHAPE_1D(args,xargs,uid)
    elif ndim == 2: Draw_DATAMCSHAPE_2D(args,xargs,uid)

    return

# Draw DATAMCSHAPE_1D
# Draw simple *_data *_MC plots for TH1D
# _____________________________________________
def Draw_DATAMCSHAPE_1D(args,xargs,uid):

    # Loop over files and get all plots
    DataPlots  = []
    MCPlots    = []
    ShapePlots = []
    for f in Args.files:
        DataPlots.append(GetObject(f, uid, "data",args))
        MCPlots.append(GetObject(f,uid,"MC",args))
        ShapePlots.append(GetObject(f,uid,"MC_SHAPE",args))
        
    # GetRange
    ymin = 1E9
    ymax = -1E9
    for plot in DataPlots:
        ymin = min([ymin, plot.GetMinimum()])
        ymax = max([ymax, plot.GetMaximum()])
    for plot in MCPlots:
        ymin = min([ymin, plot.GetMinimum()])
        ymax = max([ymax, plot.GetMaximum()])
    yrange = ymax - ymin

    # Now Draw
    DataMain = StyleData(DataPlots[0],"data", uid)
    DataMain.Draw("E1")
    for i, plot in enumerate(MCPlots):
        StyleTH1D(MCPlots[i],"mc",args,i,uid)
        MCPlots[i].Draw("SAME HIST C")

    # Set Range
    if yrange > 1E-10:
        DataMain.GetYaxis().SetRangeUser(ymin - yrange*1.0, ymax + yrange*1.0)
    else:
        DataMain.GetYaxis().SetRangeUser(0.0, ymax + yrange*0.8)

    # Build Legend
    leg = gPad.BuildLegend(0.38,0.88 - (1.+len(MCPlots))*0.07, 0.82,0.88)
    leg.SetTextSize(0.04)

    fakeline = TLine(1.1,0.0,1.2,0.0)
    fakeline.SetLineColor(kBlack)
    fakeline.SetLineStyle(7)
    fakeline.SetLineWidth(2)
    leg.AddEntry(fakeline, "norm. to data", "l")

    # Now draw shape
    for i, plot in enumerate(ShapePlots):
        StyleTH1D(ShapePlots[i],"mc",args,i,uid)
        ShapePlots[i].SetLineStyle(7)
        ShapePlots[i].SetLineWidth(2)
        ShapePlots[i].Draw("SAME HIST C")

    GLOBALLIST.append([DataPlots, MCPlots, ShapePlots])
    gPad.Update()
    return


# Draw DATAMCSHAPE_2D
# Draw simple *_data *_MC plots for TH1D
# _____________________________________________
def Draw_DATAMCSHAPE_2D(args,xargs,uid):

    # Loop over files and get all plots
    DataPlots  = []
    MCPlots    = []
    ShapePlots = []
    for f in Args.files:
        DataPlots.append(GetObject(f, uid, "data",args))

    # Loop over bin slices
    if args.slice == "x":
        for i in range(DataPlots[0].GetNbinsX()):
            args.xslice = i+2
            Draw_DATAMCSHAPE_1D(args,xargs,uid)
            break

    return


# PARSER 
# _____________________________________________
def ParseArguments():

    parser = argparse.ArgumentParser (description = "nuiscomp plotting tool",
                                      usage = "./nuiscomp-plot <options>")

    required = parser.add_argument_group ("required arguments")
    required.add_argument ("-file",   action = "append", dest = "files", metavar = "[PATH TO OUTPUT FILE]", required = True)
    required.add_argument ("-output", action = "store",  dest = "output",  metavar = "[PATH TO OUTPUT FILE]", required = True)
    required.add_argument ("-label",  action = "append", dest = "labels",  metavar = "[PATH TO OUTPUTFILE]", required = False)
    required.add_argument ("-colour", action = "append", dest = "colours",  metavar = "[TAG TO IDENTIFY FIT]", required = False)
    required.add_argument ("-slice", action = "store", dest = "slice",  metavar = "[TAG TO IDENTIFY FIT]", required = False)
                 
    args, other = parser.parse_known_args()
    
    nuisargs = ' '.join(other)

    args.xslice = None
    args.yslice = None

    # Assign labels colours if none given
    if not args.colours: args.colours = []
    if not args.labels: args.labels = []

    # Loop over arguments and assign values if label/colour etc not in sync
    print "Read arguments:"
    for i, f in enumerate(args.files):
        if len(args.labels) < i+1: args.labels.append(f)
        if len(args.colours) < i+1: args.colours.append(i+1)

        print i, f, args.labels[i], args.colours[i]
    
    return args, nuisargs


# _____________________________________________
if __name__=="__main__":

    # Parse inputs
    Args, ExtraArgs = ParseArguments()

    # Loop over ALL files and get UniqueIDS
    UniqueIDs = []
    for f in Args.files:
        
        # Read file
        inputfile = TFile(f,"READ")
        if not inputfile or inputfile.IsZombie():
            print "Cannot find file : ", inputfile
            sys.exit(1)
        
        # Get all UniqueID data IDs
        for plotkey in inputfile.GetListOfKeys():
            # Skip Non Data Keys
            if not plotkey.GetName().endswith("_data"): continue
            # Skip existing Keys
            if plotkey.GetName().replace("_data","") in UniqueIDs: continue
            # Add to list
            UniqueIDs.append(plotkey.GetName().replace("_data",""))

        # Close
        inputfile.Close()
        
    # Pass UniqueIDs to draw routines
    typestring = "DATAMCSHAPE"
    typelist = typestring.split(",")
    ndraws = len(typelist)
    
    # Create a new Canvas for the drawing
    c1 = TCanvas("newcanv","newcanv",800,600)
    
    # PLOTTING START
    # _____________________________________________

    # Make a 'contents' page
    contents = TPaveText(0.0,0.0,1.0,1.0)
    contents.SetTextSize(0.06)
    contents.SetFillColor(0)

    c1.cd()
    contents.Draw()

    # Open the file
    c1.Print(Args.output + "(")

    # MAIN DRAW LOOP
    # _____________________________________________

    # Divide the canvas according to number of options
    if (ndraws == 1): val = None
    elif (ndraws <= 4): c1.Divide(2,2)
    elif (ndraws <= 6): c1.Divide(3,2)

    # Loop over Unique IDs. One canvas save per ID
    for uid in UniqueIDs:

        # Loop over options and draw each one to SubPad
        for i in range(ndraws):
    
            # Change Pad
            if ndraws == 1: c1.cd()
            else: c1.cd(i+1)
            
            # Get Command
            typedraw = typelist[i]
            
            # Awful Switch
            if (typedraw == "DATAMC"): Draw_DATAMC(Args,ExtraArgs,uid)
            elif (typedraw == "DATAMCSHAPE"): Draw_DATAMCSHAPE(Args,ExtraArgs,uid)
            c1.Update()

            break

        # Save this draw to file
        c1.Update()
        c1.Print(Args.output)

    # Make a blank page and close
    c1.Clear()
    c1.Print(Args.output + ")")

    # PLOTTING FINISH
    # _____________________________________________

    # Finish
    print "Finished plotting!"

