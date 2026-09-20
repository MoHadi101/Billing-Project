from cx_Freeze import setup, Executable
import sys

# Für Windows: GUI-Modus (kein Konsolenfenster)
base = None
if sys.platform == "win32":
    base = "gui"

# Dateien, die mit ins Build-Verzeichnis kopiert werden sollen
include_files = ["icon.ico"]

# ------------------------------------------------------------
# Shortcut-Tabelle für den MSI-Installer
# ------------------------------------------------------------
shortcut_table = [
    ("DesktopShortcut",               # interner Name
     "DesktopFolder",                 # Zielordner: Desktop
     "Online-Retail Billing System",  # Anzeigename der Verknüpfung
     "TARGETDIR",                     # Komponente (Hauptverzeichnis)
     "[TARGETDIR]BillingSystem.exe",  # Pfad zur .exe (ACHTUNG: Name muss mit target_name übereinstimmen)
     None, None, None, None, None, None, None)
]

# MSI-Daten: Die Shortcut-Tabelle wird in die Installer-Daten eingefügt
msi_data = {"Shortcut": shortcut_table}

# Optionen für den MSI-Installer
bdist_msi_options = {
    "data": msi_data,
    "upgrade_code": "{11111111-2222-3333-4444-555555555555}",  # eindeutige ID (kannst du so lassen)
    "add_to_path": False,
}

setup(
    name="OnlineRetailBillingSystem",      # interner Name (keine Leerzeichen)
    version="1.0",
    description="Online-Retail Billing System",
    author="Mohamad Al Hade",
    options={
        "build_exe": {
            "include_files": include_files,
            "packages": ["os", "random", "tkinter"],
            "include_msvcr": True,
        },
        "bdist_msi": bdist_msi_options,
    },
    executables=[
        Executable(
            script="main.py",
            base=base,
            icon="icon.ico",                # Icon für die .exe
            target_name="BillingSystem.exe" # Name der erzeugten .exe (wichtig!)
        )
    ]
)