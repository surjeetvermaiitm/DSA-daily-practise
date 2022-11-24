#Lnk: https://leetcode.com/problems/powx-n/

class Solution {
public:
    double myPow(double x, int n) {
        if(n<0){
            return myPow(1/x,abs(n));
        }
        if(n==0) return 1;
        if(n==1) return x;
        double p=myPow(x,n/2);
        if(n%2==0){
            return p*p;
        }
        else{
            return p*p*x;
        }
    }
};