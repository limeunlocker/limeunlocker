
[app]

# (str) Title of your application
title = Lime Offline Unlocker

# (str) Package name
package.name = org.lime.unlock.offline

# (str) Package domain (needed for android/ios packaging)
package.domain = org.lime.unlock

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy,httpx,pyjwt

# (str) Custom source folders for requirements
# (e.g. if some module is stored outside the working dir)
#p4a.source_dir =

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 31

# (str) Android NDK version to use
android.ndk = 23b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (bool) Android NDK allows copying shared libraries (aapt/p4a workaround)
android.copy_libs = True

# (list) Architectures to build for
android.archs = armeabi-v7a, arm64-v8a

# (str) Bootstrap to use for android builds
bootstrap = sdl2

# (str) Path to build artifacts (no spaces!)
android.storage_dir = .buildozer

# (str) Package format: apk, aab, or both
android.package_format = apk

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Supported screens (comma separated)
# android.supported_screens = small, normal, large, xlarge

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0
