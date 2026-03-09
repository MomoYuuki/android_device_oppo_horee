#
# Copyright (C) 2018 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
TARGET_SUPPORTS_OMX_SERVICE := false
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit from horee device
$(call inherit-product, device/oneplus/horee/device.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

PRODUCT_NAME := lineage_horee
PRODUCT_DEVICE := horee
PRODUCT_MANUFACTURER := OPPO
PRODUCT_BRAND := OPPO
PRODUCT_MODEL := PEDM00

PRODUCT_GMS_CLIENTID_BASE := android-oppo

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="PEDM00-user 14 UKQ1.230924.001 R.1edb8dd_42aa_42ab release-keys" \
    BuildFingerprint=OPPO/PEDM00/OP4E5D:14/UKQ1.230924.001/R.1edb8dd_42aa_42ab:user/release-keys \
    DeviceName=OP4E5D \
    DeviceProduct=PEDM00 \
    SystemDevice=OP4E5D \
    SystemName=PEDM00
