Remote ADB Connection Manager
=============================

RACM (Remote ADB Connection Manager) provides easy way to manage multiple remote ADB (Android Debug Bridge) connections.

ADB can connect remote target with `adb connect <host>:<port>` command, but command operations between multiple targets are very troublesome and increase destructive human errors.
RACM has a simple interface allowing easy and safe operation.
Remote ADB connection is often used by custom emulator environments (e.g. Genymotion) and some networked embedded devices (e.g. RICOH's MultiLink-Panel MFP).

![Screen shot: Main Window](doc/img/main_window_0.1.png "Main Window")

## Settings

When you use the first time, you need to configure the path of ADB command at Settings window from `Edit -> Settings`.

![Screen shot: Settings Window 1](doc/img/settings_window_1_0.1.png "Settings Window 1")

You can customize command shortcuts in `Custom Buttons` tab.

![Screen shot: Settings Window 2](doc/img/settings_window_2_0.1.png "Settings Window 2")

Your configurations are write to `racm.yaml` file in current (same as .exe) directory.

## Requirements

RACM is written in Python and many platforms are supported.
If you use Windows platform, use single .exe file that includes python runtime and many depended libraries.
Other platform users can execute RACM by command line `> chmod u+x racm.py && ./racm.py` after installed depended libraries (see below).

## Libraries

* [wxPython](http://www.wxpython.org/) 3.0
* [PyYAML](http://pyyaml.org/) 3.11
* [py2exe](http://www.py2exe.org/) 0.6.9

## Development Environment

* Python 2.7 32bit
* Windows 10 Pro 64bit
* PyCharm 4.5.4
* wxFormBuilder 3.5.0-beta

## License

RACM is licensed under BSD license.
