#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,avx2,fma")
#pragma GCC optimize("unroll-loops")
#include <bits/stdc++.h> 
using namespace std;
 
typedef long long ll;
typedef long double ld;
typedef pair<int,int> p32;
typedef pair<ll,ll> p64;
typedef pair<double,double> pdd;
typedef vector<ll> v64;
typedef vector<int> v32;
typedef vector<vector<int> > vv32;
typedef vector<vector<ll> > vv64;
typedef vector<vector<p64> > vvp64;
typedef vector<p64> vp64;
typedef vector<p32> vp32;
ll MOD = 998244353;
double eps = 1e-12;
#define forn(i,e) for(ll i = 0; i < e; i++)
#define forsn(i,s,e) for(ll i = s; i < e; i++)
#define rforn(i,s) for(ll i = s; i >= 0; i--)
#define rforsn(i,s,e) for(ll i = s; i >= e; i--)
#define ln "\n"
#define dbg(x) cout<<#x<<" = "<<x<<ln
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define INF 2e18
#define fast_cin() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define all(x) (x).begin(), (x).end()
#define sz(x) ((ll)(x).size())
 

vector<vector<int>> solve(vector<int> arr, int target_sum){
    // sorting the vector in order to use two pointer approach
    sort(arr.begin(),arr.end());
    vector<vector<int>> result;
    int n = arr.size();
    // for every a[i] using the two pointer approach in order to get the pair sum
    for (int i = 0; i <= n-3; i++){
        int j = i+1;
        int k = n-1;

        // two pointer approach
        while(j<k){
            int current_sum = arr[i];
            current_sum+=arr[j];
            current_sum+=arr[k];
            if (current_sum == target_sum){
                result.pb({arr[i],arr[j],arr[k]});
                k--;
                j++;
            }else if (current_sum > target_sum){
                k--;
            }else{
                j++;
            }
        }
    }
    return result;
    
}

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    fast_cin();
    vector<int> arr = {1,2,3,4,5,6,7,8,9,15};
    int sum = 18;
    auto res = solve(arr,sum);
    for(auto a : res){
        for(auto no : a){
            cout<<no<<" ";
        }
        cout<<endl;
    }
    return 0;
}