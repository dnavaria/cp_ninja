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
 
// counting all pairs that equals to that value x, Note: values of the array are reused
int solve(int arr[], int n, int val){
    unordered_map<int,int> um;
    int pair_count = 0 ;
    for (int i = 0; i < n; i++){
        int x = arr[i] - val;
        if (arr[i] < val && x < 0){
            x = abs(x);
        }else{
            x = -x;
        }
        if (um.count(x ) > 0){
            pair_count+= um[x];
        }
        if (um.count(arr[i]) > 0){
            um[arr[i]] += 1;
        }else{
            um[arr[i]] = 1;
        }
    // cout<<arr[i]<<" "<<um[arr[i]]<<" "<<pair_count<<endl;
    }
    return pair_count;
}

// int main()
// {
//     #ifndef ONLINE_JUDGE
//         freopen("input.txt", "r", stdin);
//         freopen("output.txt", "w", stdout);
//     #endif
//     fast_cin();
//     ll t;
//     cin >> t;
//     for(int it=1;it<=t;it++) {
//         cout << "Case #" << it+1 << ": ";
//         solve();
//     }
//     return 0;
// }