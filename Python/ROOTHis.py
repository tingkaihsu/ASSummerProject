from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH2F
from ROOT import gROOT, gBenchmark, gRandom, gSystem
import ctypes
 
# Create a new canvas, and customize it.
c1 = TCanvas( 'c1', 'Dynamic Filling Example', 200, 10, 700, 500 )
c1.SetFillColor( 42 )
c1.GetFrame().SetFillColor( 21 )
c1.GetFrame().SetBorderSize( 6 )
c1.GetFrame().SetBorderMode( -1 )
 
# Create a new ROOT binary machine independent file.
# Note that this file may contain any kind of ROOT objects, histograms,
# pictures, graphics objects, detector geometries, tracks, events, etc..
# This file is now becoming the current directory.
 
hfile = gROOT.FindObject( 'channel.root' )
if hfile:
   hfile.Close()
hfile = TFile( 'channel.root', 'RECREATE', 'Use ROOT file with histograms to show Effeciency' )
 
# Create some histograms, a profile histogram and an ntuple
hpx    = TH1F( 'eff', 'Distribution of Effeciency in every 100 secs', 100, -4, 4 )
 
# Set canvas/frame attributes.
hpx.SetFillColor( 48 )
 
gBenchmark.Start( 'hsimple' )

with open('data.txt', 'r') as input:
  lines = input.readlines()
  ch1 = []
  ch2 = []
  eff = []
for line in lines:
  if not line.startswith('#'):
    data = line.split(' ')
    ch1.append(int(data[0]))
    ch2.append(int(data[1]))

i = 0
while (i < len(ch1)-1):
  if (ch1[i+1] != ch1[i]):
    eff.append((ch2[i+1] - ch2[i])/(ch1[i+1]-ch1[i]))
    # print((ch2[i+1] - ch2[i])/(ch1[i+1]-ch1[i]))
  i += 100
    # print((ch2[i+1] - ch2[i])/(ch1[i+1]-ch1[i]))

for i in range( len(eff) ):
   px = eff[i]
 # Fill histograms.
   hpx.Fill( px )
   hpx.Draw()
   c1.Modified()
   c1.Update()
 
# Save all objects in this file.
hpx.SetFillColor( 0 )
hfile.Write()
hpx.SetFillColor( 0 )
c1.Modified()
c1.Update()