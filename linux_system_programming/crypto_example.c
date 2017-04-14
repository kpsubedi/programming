#include <openssl/conf.h>
#include <openssl/evp.h>
#include <openssl/err.h>


int main(int argc, char **agev)
{

/* Load the human readable error strings for libcrypto */
ERR_load_crypto_strings();

/* Load all digest and cipher algorithms */
OpenSSL_add_all_algorithms();

/* Load config file, and other important initialization */
OPENSSL_config(NULL);


/* Do crypto stuff */



EVP_cleanup();

CRYPTO_cleanup_all_ex_data();

ERR_free_strings();

return 0;
}

