#include <iostream>
#include <fstream>
#include <string>

using namespace std;
class CHA {
public:
    void getdata(string mystr) {
        // loop interating string
        string ch1, ch2;
        bool first = true;
        for ( char& c : mystr ) {
            if (c != ' ') {
                if (first) {
                    ch1 += c;
                }
                else {
                    ch2 += c;
                }
            }
            else {
                first = false;
            }
        }
        this->ch1 = stoi(ch1);
        this->ch2 = stoi(ch2);
        if (this->ch1 != 0) {
            this->eff = (float)this->ch2 / (float)this->ch1;
        }
        else {
            this->eff = 0;
        }
        return;
    }
    int getch1() {
        return ch1;
    }
    int getch2() {
        return ch2;
    }
    float geteff() {
        return eff;
    }

private:
    int ch1 = 0;
    int ch2 = 0;
    float eff = 0;
};

void ROOTRead() {
    ifstream myfile;
    myfile.open("data.txt");
    string mystring;
    CHA arr[10000];
    int idx = -1;   //the first line is ch1 and ch2
    int size = 0;
    while (getline(myfile, mystring)) {
        // cout << mystring << endl;
        if (idx>=0) {
            ++size;
            arr[size].getdata(mystring);
            // cout << arr[idx].getch1() << " " << arr[idx].getch2() << endl;
        }
        ++idx;
    }

    cout << size << endl;
    myfile.close();

    double eff[500];
    double eves[500];
    for (int i = 0; i < 500; ++i) {
        // cout << arr[i].geteff() << endl;
        eff[i] = arr[i].geteff();
        eves[i] = i;
    }
    TCanvas *c1 = new TCanvas("image", "n4254", 40,40,800,600);
    auto s_eff = new TScatter(500, eves, eff);
    s_eff->SetTitle("Effeciency V.S Total events;Total events;Effeciency");
    s_eff->SetMarkerColor(kRed);
    s_eff->SetMarkerStyle(20);
    s_eff->Draw("A");
    c1->SaveAs("eff_sca_gra.png");
    return;
}