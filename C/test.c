#include <stdio.h>
#include <math.h>


struct complex_struct {double x,y;};

double real_part(struct complex_struct z){
    return z.x;    
}

double img_part(struct complex_struct z){
    return z.y;
}

double magnitude(struct complex_struct z){
    return sqrt(z.x*z.x + z.y*z.y);    
}
double angle(struct complex_struct z){
    return 0.0;    
}

int main(void){
    return 0;    
}



