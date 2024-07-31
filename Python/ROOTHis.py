from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH2F, TLegend, TF1, TMath
from ROOT import gROOT, gBenchmark, gRandom, gSystem
import ctypes
import numpy as np
def DrawHis(filepath, hisname, interval, savefile):
  with open(filepath, 'r') as input:
    lines = input.readlines()
    ch1 = []
    ch2 = []
    eff = []
    times = []
    avg_part = []
    upper = 0
    lower = 100000
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
      avg_part.append((ch1[i+1]-ch1[i]))
      if (hisname == 'eff'):
        if lower > (ch2[i+1] - ch2[i])/(ch1[i+1]-ch1[i]):
          lower = (ch2[i+1] - ch2[i])/(ch1[i+1]-ch1[i])
        if upper < (ch2[i+1] - ch2[i])/(ch1[i+1]-ch1[i]):
          upper = (ch2[i+1] - ch2[i])/(ch1[i+1]-ch1[i])
      else:
        if lower > (ch1[i+1]-ch1[i]):
          lower = (ch1[i+1]-ch1[i])
        if upper < (ch1[i+1]-ch1[i]):
          upper = (ch1[i+1]-ch1[i])
    i += 1

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
  # h_eff    = TH1F( 'eff', 'Distribution of Effeciency in every 1200 secs', 100, 0, 1.2 )
  # h_eff    = TH1F( 'avg_part', 'Average Particles in 600 Seconds', 100, 10, 80 )
  if hisname == 'eff':
    title = "Efficiency in every " + interval + " secs"
  else:
    title = "Average Particles in " +  interval + " secs"
  h = TH1F(hisname, title, 100, lower, upper)
  # Set canvas/frame attributes.
  h.SetFillColor( 48 )
  
  gBenchmark.Start( 'hsimple' )
  if hisname == 'eff':
    for j in range( len(eff) ):
      if eff[j] <= 1:
        bin = eff[j]
        h.Fill( bin )
  else:
    for j in range( len(avg_part) ):
      bin = avg_part[j]
      h.Fill( bin )

  avg = 0
  for k in range(len(times)-1):
    avg += times[k+1] - times[k]
  avg /= len(times)
  print(avg/60.0)

  hfile.Write()
  h_c = h.GetCumulative()
  h_c.SetStats(0)
  avg_part_arr = np.array(avg_part)
  h.Draw()
  if hisname != 'eff':
    avg = np.average(avg_part_arr)
    print("avg: ", avg)
    f1 = TF1("f1", "[0]*TMath::Poisson(x, 74)", lower, upper)
    f1.SetParameter(10, 10)
    h.Fit("f1", "R")
    # f1.Draw("SAME")

  c1.Modified()
  c1.Update()
  c1.SaveAs(savefile)

DrawHis("data2.txt", "avg_part", "1200", "eff_funct.png")