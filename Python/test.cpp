#include <iostream>
#include <fstream>
#include <string>
#include "TFile.h"
#include "TTree.h"
using namespace std;
void test(const char* input_file, const char* output_file) {
    ifstream infile(input_file);
    //debug
    if (!infile) {
        cerr << "Error opening input file " << input_file << endl;
        return;
    }
    
    //Create a TFile to store the TTree
    TFile *file = new TFile(output_file, "RECREATE");
    TTree *tree = new TTree("tree", "Channel versus counter");
    int ch1 = 0, ch2 = 1;
    tree->Branch("ch1", &ch1, "ch1/I");
    tree->Branch("ch2", &ch2, "ch2/I");
    tree->Fill();
    file->Write();
    file->Close();
    
    //Clean up
    delete file;
    delete tree;
}


int main() {
    const char* input_file = "data.txt";
    const char* output_file = "output.root";
    test(input_file, output_file);
    cout << "Hello world!" << endl;
    return 0;
}