#include <stdio.h>

int main()
{
    FILE *input = fopen("input.txt", "r");;
    if (input == NULL)
    {
        printf("Could not open input.txt\n");
    }
    FILE *output = fopen("output.txt", "w");;
    if (output == NULL)
    {
        printf("Could not open output.txt\n");
    }
    int8_t buffer;
    fread(&buffer, sizeof(buffer), 1, input);
    fwrite(&buffer, sizeof(buffer), 1, output);
    printf("buffer: %c\n", buffer);
    fread(&buffer, sizeof(buffer), 1, input);
    fwrite(&buffer, sizeof(buffer), 1, output);
    printf("buffer: %c\n", buffer);
    fread(&buffer, sizeof(buffer), 1, input);
    fwrite(&buffer, sizeof(buffer), 1, output);
    printf("buffer: %c\n", buffer);


}