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
        this->eff = (float)this->ch2 / (float)this->ch1;
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

    while (getline(myfile, mystring)) {
        // cout << mystring << endl;
        if (idx >= 0) {
            arr[idx].getdata(mystring);
            // cout << arr[idx].getch1() << " " << arr[idx].getch2() << endl;
        }
        ++idx;
    }

    myfile.close();

    TH1* h_eff = new TH1D("eff", "Histogram of Effeciency", 100,0.0,1.0);
    
    for (int i = 0; i < size(arr); ++i) {
        h_eff->Fill(arr[i].geteff());
    }
    h_eff->Draw("bar1");
    return;
}