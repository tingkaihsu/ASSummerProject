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
h_eff    = TH1F( 'eff', 'Distribution of Effeciency in every 500 secs', 100, 0, 1.2 )
# h_eff    = TH1F( 'avg_part', 'Average Particles per Seconds', 100, 0, 0.15 )
# Set canvas/frame attributes.
h_eff.SetFillColor( 48 )
 
gBenchmark.Start( 'hsimple' )

with open('data1.txt', 'r') as input:
  lines = input.readlines()
  ch1 = []
  ch2 = []
  eff = []
  times = []
  avg_part = []
for line in lines:
  if not line.startswith('#') and not line.startswith('current'):
    data = line.split(' ')
    ch1.append(int(data[0]))
    ch2.append(int(data[1]))
  elif line.startswith('current'):
    data = line.split(' ')
    # print(data)
    times.append(float(data[3]))

i = 0
while (i < len(ch1)-1):
  if (ch1[i+1] != ch1[i]):
    eff.append((ch2[i+1] - ch2[i])/(ch1[i+1]-ch1[i]))
    # print((ch2[i+1] - ch2[i])/(ch1[i+1]-ch1[i]))
    avg_part.append((ch1[i+1]-ch1[i])/(times[i+1]-times[i]))
  i += 1
    # print((ch2[i+1] - ch2[i])/(ch1[i+1]-ch1[i]))

for j in range( len(eff) ):
  if eff[j] <= 1:
    px = eff[j]
# Fill histograms.
    h_eff.Fill( px )
    h_eff.Draw()
    c1.Modified()
    c1.Update()
 
# for j in range( len(avg_part) ):
#   px = avg_part[j]
# # Fill histograms.
#   h_eff.Fill( px )
#   h_eff.Draw()
#   c1.Modified()
#   c1.Update()

# Save all objects in this file.
h_eff.SetFillColor( 0 )
hfile.Write()
h_eff.SetFillColor( 0 )
c1.Modified()
c1.Update()
c1.SaveAs('eff_data1.png')
