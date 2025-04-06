#!/bin/bash

JADX_VERSION="1.5.1"
JADX_ZIP="jadx-${JADX_VERSION}.zip"
JADX_URL="https://github.com/skylot/jadx/releases/download/v${JADX_VERSION}/${JADX_ZIP}"
INSTALL_DIR="installed-tools"
DOWNLOAD_PATH="${INSTALL_DIR}/${JADX_ZIP}"

mkdir -p "$INSTALL_DIR"

echo "[*] Downloading JADX $JADX_VERSION..."
if command -v curl >/dev/null 2>&1; then
  curl -L "$JADX_URL" -o "$DOWNLOAD_PATH"
elif command -v wget >/dev/null 2>&1; then
  wget -O "$DOWNLOAD_PATH" "$JADX_URL"
else
  echo "[!] Neither curl nor wget is installed. Aborting."
  exit 1
fi

echo "[*] Unzipping..."
unzip -q "$DOWNLOAD_PATH" -d "$INSTALL_DIR"

echo "[+] JADX $JADX_VERSION installed in '$INSTALL_DIR'"
