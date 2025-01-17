#
# Copyright (C) 2013-2016 The CyanogenMod Project
#           (C) 2017 The LineageOS Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# Screen density
PRODUCT_AAPT_CONFIG := normal
PRODUCT_AAPT_PREF_CONFIG := xhdpi
PRODUCT_AAPT_PREBUILT_DPI := xhdpi 280dpi hdpi tvdpi mdpi ldpi

# Device specific overlays
DEVICE_PACKAGE_OVERLAYS += $(LOCAL_PATH)/overlay
ifeq ($(BOARD_AOSP_BASED),)
DEVICE_PACKAGE_OVERLAYS += $(LOCAL_PATH)/overlay-lineage
endif

# Soong
PRODUCT_SOONG_NAMESPACES += $(LOCAL_PATH)

# Provide AOSP APN configurations
ifneq ($(BOARD_AOSP_BASED),)
PRODUCT_COPY_FILES += device/sample/etc/apns-full-conf.xml:system/etc/apns-conf.xml
endif

### APEX
PRODUCT_COMPRESSED_APEX := false

# Product common configurations
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Device product elements
include $(LOCAL_PATH)/product/*.mk

# Common Android Go configurations
$(call inherit-product, build/target/product/go_defaults.mk)

# Vendor product configurations
$(call inherit-product, vendor/sony/huashan/huashan-vendor.mk)
