import os
import subprocess
import platform
import sys

def extract_apk_with_jadx(apk_path, output_dir, target_package):
    if not os.path.isfile(apk_path):
        raise FileNotFoundError(f"APK file not found: {apk_path}")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Decompiling APK: {apk_path} to {output_dir}")
    
    try:
        jadx_executable = "jadx.bat" if platform.system() == "Windows" else "jadx"
        jadx_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                                "installed-tools","jadx", "bin", jadx_executable)
        
        if not os.path.exists(jadx_path):
            raise FileNotFoundError(f"JADX not found at: {jadx_path}")
            
        command = [jadx_path, "-d", output_dir, apk_path]        
        subprocess.run(command, check=True)
        print(f"Decompilation complete. Files saved to: {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error during decompilation: {e}")
        sys.exit(1)
    
    manifest_path = os.path.join(output_dir, "resources", "AndroidManifest.xml")
    strings_path = os.path.join(output_dir, "resources" ,"res", "values", "strings.xml")
    
    target_classes = []
    for root, _, files in os.walk(output_dir):
        for file in files:
            if file.endswith(".java"):
                package_path = target_package.replace(".", os.sep)
                if package_path in os.path.normpath(root):
                    target_classes.append(os.path.join(root, file))
    
    return manifest_path, strings_path, target_classes
