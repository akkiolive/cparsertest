#define MMM 123

int foo;
extern long nuke;

double func(int, char*);
extern void funcB(double);

int main(){
    int lar = 1;
    foo = lar;
    func(foo, "bar");

    return 0;
}