#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/oppo/horee',
    'device/realme/sm8250-common',
    'hardware/oplus',
    'vendor/realme/sm8250-common',
    'vendor/qcom/opensource/display',
]

blob_fixups: blob_fixups_user_type = {
    'odm/lib64/vendor.oplus.hardware.urcc-V1-ndk_platform.so': blob_fixup()
        .add_needed('libjsoncpp_shim.so'),
    'odm/lib64/libarcsoft_qnnhtp.so': blob_fixup()
        .clear_symbol_version('remote_handle_close')
        .clear_symbol_version('remote_handle_invoke')
        .clear_symbol_version('remote_handle_open')
        .clear_symbol_version('remote_register_buf_attr')
        .clear_symbol_version('remote_register_buf'),
    # These configs belong to horee; common fixups only apply to common blobs.
    'vendor/etc/libnfc-nci.conf': blob_fixup()
        .regex_replace('NFC_DEBUG_ENABLED=1', 'NFC_DEBUG_ENABLED=0'),
    'vendor/etc/libnfc-nxp.conf': blob_fixup()
        .regex_replace('(NXPLOG_.*_LOGLEVEL)=0x03', '\\1=0x02')
        .regex_replace('NFC_DEBUG_ENABLED=1', 'NFC_DEBUG_ENABLED=0'),
    ('odm/bin/hw/vendor.oplus.hardware.charger-V6-service', 'odm/lib64/libGaiaClient_vnd.so'): blob_fixup()
        .add_needed('libbase_shim.so')
        .add_needed('libjsoncpp_shim.so')
        .replace_needed('libosenseaidlhalclient.so', 'libosenseaidlhalclient_charge.so')
        .replace_needed('vendor.oplus.hardware.charger-V6-ndk_platform.so', 'vendor.oplus.hardware.charger-V6-ndk.so')
        .replace_needed('vendor.oplus.hardware.osense.client-V1-ndk_platform.so', 'vendor.oplus.hardware.osense.client-V1-ndk.so'),
    'odm/lib64/libosenseaidlhalclient_charge.so': blob_fixup()
        .replace_needed('vendor.oplus.hardware.osense.client-V1-ndk_platform.so', 'vendor.oplus.hardware.osense.client-V1-ndk.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'horee',
    'oppo',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8250-common', 'realme'
    )
    utils.run()
