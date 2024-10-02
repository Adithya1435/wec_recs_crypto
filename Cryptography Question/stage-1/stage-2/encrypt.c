#include <stdio.h>
#include <string.h>

void custom_encrypt(const char *msg, const char *key) {
    int msg_len = strlen(msg);
    int key_len = strlen(key);
    int msg_ascii[msg_len];
    int key_ascii[msg_len];
    int encrypted_values[msg_len];

    if(msg_len != key_len) {
        printf("Message and Key lengths do not match\n");
        return;
    }

    for(int i=0;i<msg_len;i++) {
        msg_ascii[i] = (int)msg[i];
        key_ascii[i] = (int)key[i];
    }

    // Apply the encryption logic
    for (int i = 0; i < msg_len; i++) {
        int product = msg_ascii[i] * key_ascii[i];
        if(i == 0) {
            encrypted_values[i] = product % 10000;
        }
        else {
            encrypted_values[i] = (product  + encrypted_values[i - 1]) % 10000;
        }
    }

    // Output the encrypted values
    printf("Encrypted Values: ");
    for (int i = 0; i < msg_len; i++) {
        printf("%d ", encrypted_values[i]);
    }
    printf("\n");
}
