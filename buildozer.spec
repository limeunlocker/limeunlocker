[app]

# (str) Title of your application
title = Lime Offline Unlocker

# (str) Package name
package.name = org.lime.unlock.offline

# (str) Package domain (needed for android/ios packaging)
package.domain = org.lime.unlock

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (empty includes all)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy,httpx,pyjwt

# (str) Supported orientation (landscape, portrait, or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API level
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use (ONLY ONE, no duplicates)
android.sdk = 30.0.3

# (str) Android NDK version to use
android.ndk = 23b

# (int) Android NDK API to use (should match android.minapi)
android.ndk_api = 21

# (bool) Use private storage (True) or public (False)
android.private_storage = True

# (bool) Allows copying shared libraries (aapt/p4a workaround)
android.copy_libs = True

# (list) Architectures to build for
android.archs = armeabi-v7a, arm64-v8a

# (str) Bootstrap to use
bootstrap = sdl2

# (str) Path to build artifacts (no spaces!)
android.storage_dir = .buildozer

# (str) Package format (apk, aab, or both)
android.package_format = apk

# (bool) Fullscreen mode (0 = off, 1 = on)
fullscreen = 0

# (str) Icon filename (uncomment and set if you have an icon)
# icon.filename = %(source.dir)s/data/icon.png

# (str) Presplash filename (uncomment and set if you have one)
# presplash.filename = %(source.dir)s/data/presplash.png
