#include "pilot/math.hpp"
#include <algorithm>
namespace pilot {
int sum(const std::vector<int>& xs){ int s=0; for(auto v: xs) s+=v; return s; }
int clamp(int v,int lo,int hi){ return std::min(hi,std::max(lo,v)); }
}
