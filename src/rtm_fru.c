#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>

#include "user_rtm_fru.h"
#include "fru_editor.h"

size_t rtm_fru_info_build( uint8_t **buffer, const char *sn, const char *manuf_time )
{
    uint8_t *hdr_ptr, *board_ptr, *product_ptr, *z3_ptr;
    uint8_t int_use_off = 0, chassis_off = 0, board_off = 0, product_off = 0, z3_compat_off = 0, multirec_off = 0;
    size_t board_sz = 0, product_sz = 0, z3_compat_sz = 0;
    size_t offset = 0;

    uint32_t m_time = strtoul(manuf_time, (char **) NULL, 10);

    /* Skip the common header */
    offset += 8;

    /* Board Information Area */
    board_off = offset;
    board_sz = board_info_area_build( &board_ptr, RTM_LANG_CODE, m_time, RTM_BOARD_MANUFACTURER, RTM_BOARD_NAME, sn, RTM_BOARD_PN, RTM_FRU_FILE_ID );
    offset += board_sz;

    /* Product Information Area */
    product_off = offset;
    product_sz = product_info_area_build( &product_ptr, RTM_LANG_CODE, RTM_PRODUCT_MANUFACTURER, RTM_PRODUCT_NAME, RTM_PRODUCT_PN, RTM_PRODUCT_VERSION, sn, RTM_PRODUCT_ASSET_TAG, RTM_FRU_FILE_ID );
    offset += product_sz;

    /* Multirecord Area */
    multirec_off = offset;

    /* Zone3 Connector Compatibility */
    z3_compat_off = offset;
    z3_compat_sz += zone3_compatibility_record_build( &z3_ptr, RTM_COMPATIBILITY_CODE );
    offset += z3_compat_sz;

    /* Common Header */
    fru_header_build( &hdr_ptr, int_use_off, chassis_off, board_off, product_off, multirec_off );

    *buffer = malloc(offset);

    memcpy( (*buffer)+0, hdr_ptr, 8);
    memcpy( (*buffer)+board_off, board_ptr, board_sz);
    memcpy( (*buffer)+product_off, product_ptr, product_sz);
    memcpy( (*buffer)+z3_compat_off, z3_ptr, z3_compat_sz);

    free(hdr_ptr);
    free(board_ptr);
    free(product_ptr);
    free(z3_ptr);

    return offset;
}


int main( int argc, char *argv[] ) {
    FILE *output;
    uint8_t *buffer, sz;

    if ( argc != 4 ) {
        fprintf(stderr, "The output binary file path must be provided as a positional argument!\n");
        exit(EXIT_FAILURE);
    }
    sz = rtm_fru_info_build( &buffer, argv[2], argv[3] );

    output = fopen(argv[1],"wb");

    if (output) {
        fwrite( buffer, sz, 1, output);
    }

    fclose(output);

    return 1;
}
