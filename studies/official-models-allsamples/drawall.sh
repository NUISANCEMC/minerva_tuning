python nuisomp-plot.py \
    -file ./allsamples-AltPion.root -colour kBlue -label AltPion \
    -file ./allsamples-Default.root -colour kRed -label Default \
    -file ./allsamples-DefaultPlusMECWithNC-DefaultPlusMEC.root -colour kGreen -label Default+MEC \
    -file ./allsamples-DefaultPlusValenciaMEC-DefaultPlusMEC.root -colour kCyan -label Default+Val \
    -file ./allsamples-EffSFTEM.root -colour kRed+2 -label EffSFTEM \
    -file ./allsamples-ValenciaQEBergerSehgalCOHRES-DefaultPlusMEC.root -colour kGreen+2 -label ValBerger \
    -output allcombined.pdf -b -slice x

python nuisomp-plot.py \
    -file ./allsamples-AltPion.root -colour kBlue -label AltPion \
    -file ./allsamples-Default.root -colour kRed -label Default \
    -file ./allsamples-EffSFTEM.root -colour kGreen -label EffSFTEM \
    -output allcombined-split1.pdf -b -slice x

python nuisomp-plot.py \
    -file ./allsamples-DefaultPlusMECWithNC-DefaultPlusMEC.root -colour kRed -label Default+MEC \
    -file ./allsamples-DefaultPlusValenciaMEC-DefaultPlusMEC.root -colour kCyan -label Default+Val \
    -file ./allsamples-ValenciaQEBergerSehgalCOHRES-DefaultPlusMEC.root -colour kGreen+2 -label ValBerger \
    -output allcombined-split2.pdf -b -slice x