#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Checking Python
int check_python() {
    if (system("python --version") == 0) {
        printf("Python is already installed.\n");
        return 1;
    } else {
        printf("Python is not installed.\n");
        return 0;
    }
}

// Checking SQLmap
int check_sqlmap() {
    if (system("test -d ~/sqlmap") == 0) {
        printf("SQLmap is already installed.\n");
        return 1;
    } else {
        printf("SQLmap is not installed.\n");
        return 0;
    }
}

// Checking CustomTkinter
int check_customtkinter() {
    if (system("python -c \"import customtkinter\"") == 0) {
        printf("CustomTkinter is already installed.\n");
        return 1;
    } else {
        printf("CustomTkinter is not installed.\n");
        return 0;
    }
}

// Function Loading Python
void install_python() {
    printf("Python is loading...\n");
    system("powershell -Command \"Start-Process 'https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe' -Wait\"");
}

// Function Loading SQLmap
void install_sqlmap() {
    printf("SQLmap is loading...\n");
    system("git clone https://github.com/sqlmapproject/sqlmap.git ~/sqlmap");
}

// Function Loading CustomTKinter
void install_customtkinter() {
    printf("CustomTkinter is loading...\n");
    system("python -m pip install customtkinter");
}

int main() {
    printf("Checking The Required Apps & Modules...\n");

    if (!check_python()) {
        install_python();
    }
    
    if (!check_sqlmap()) {
        install_sqlmap();
    }
    
    if (!check_customtkinter()) {
        install_customtkinter();
    }

    printf("Installation is finished.\n");

    return 0;
}
