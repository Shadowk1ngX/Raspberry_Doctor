[app]

# (str) Title of your application
title = Raspberry Doctor

# (str) Package name
package.name = raspberrydoctor

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application version
version = 0.1

# (list) Application requirements
# **(IMPORTANT)** Add `jnius` if you're using android.permissions
requirements = python3,kivy,jnius

# **(IMPORTANT)** Tells Buildozer we want to build an Android app
target = android

# (list) Supported orientations
# Valid options: landscape, portrait, portrait-reverse, landscape-reverse
orientation = portrait

# (bool) Indicate if the application should be fullscreen (1) or not (0)
fullscreen = 0

# (list) Permissions for your app
# e.g. INTERNET, WRITE_EXTERNAL_STORAGE, CAMERA, RECORD_AUDIO
android.permissions = android.permission.INTERNET, (name=android.permission.WRITE_EXTERNAL_STORAGE;maxSdkVersion=18),CAMERA, RECORD_AUDIO

# (list) The Android archs to build for, typically arm64-v8a and armeabi-v7a
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enables Android auto backup feature (Android API >= 23)
android.allow_backup = True

#
# iOS / macOS / Windows / Linux / general config
#

# Kivy version to use on OSX (doesn't affect Android)
osx.kivy_version = 1.9.1

# (str) change the major version of python used by the app on macOS
osx.python_version = 3

#
# Android-specific config
#

# (bool) Indicate if the application should be fullscreen or not (Android)
# fullscreen = 0  # (We already set this above.)

# (int) Target Android API (highest possible)
#android.api = 31

# (int) Minimum API your APK / AAB will support
#android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 23b

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (bool) If True, then skip trying to update the Android SDK
#android.skip_update = False

# (bool) If True, automatically accept SDK license agreements
#android.accept_sdk_license = False

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (bool) enables Android auto backup feature (Android API >=23)
#android.allow_backup = True  # (Already set above.)

#
# Python for Android (p4a) specific
#

# (str) python-for-android URL to use for checkout
#p4a.url =

# (str) python-for-android fork to use in case if p4a.url is not specified, defaults to upstream (kivy)
#p4a.fork = kivy

# (str) python-for-android branch to use, defaults to master
#p4a.branch = master

# (str) python-for-android specific commit to use, defaults to HEAD, must be within p4a.branch
#p4a.commit = HEAD

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
#p4a.source_dir =

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#p4a.local_recipes =

# (str) Filename to the hook for p4a
#p4a.hook =

# (str) Bootstrap to use for android builds
#p4a.bootstrap = sdl2

#
# iOS specific
#

ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0

ios.codesign.allowed = false

#
# Buildozer section
#

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
