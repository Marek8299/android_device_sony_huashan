/*
 * Copyright (C) 2019 The LineageOS Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

namespace android
{
    /* std::optional<PhysicalDisplayId> android::SurfaceComposerClient::getInternalDisplayToken */
    extern "C" void* _ZN7android21SurfaceComposerClient23getInternalDisplayTokenEv();

    /* sp<IBinder> BpSurfaceComposer::getBuiltInDisplay */
    extern "C" void* _ZN7android21SurfaceComposerClient17getBuiltInDisplayEi(long __attribute__((unused)) id)
    {
        return _ZN7android21SurfaceComposerClient23getInternalDisplayTokenEv();
    }

    extern "C" void _ZN7android21SurfaceComposerClient14getDisplayInfoERKNS_2spINS_7IBinderEEEPNS_11DisplayInfoE(void) {}

    extern "C" void _ZN7android14SurfaceControl10getSurfaceEv(void);

    extern "C" void _ZNK7android14SurfaceControl10getSurfaceEv(void) {
      _ZN7android14SurfaceControl10getSurfaceEv();
    }
};
