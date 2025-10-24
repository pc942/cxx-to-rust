#include "pilot/math.hpp"
#include <cassert>
using namespace pilot;
int main(){ assert(sum({1,2,3})==6); assert(clamp(10,0,5)==5); return 0; }
