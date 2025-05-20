#!/bin/bash

sudo apt update
sudo apt install -y build-essential linux-headers-$(uname -r)

sudo vmware-modconfig --console --install-all

sudo mkdir -p /root/vmware-keys
cd /root/vmware-keys

sudo openssl req -new -x509 -newkey rsa:2048 -keyout MOK.priv -outform DER -out MOK.der -nodes -days 36500 -subj "/CN=VMware Secure Boot/"

sudo /usr/src/linux-headers-$(uname -r)/scripts/sign-file sha256 /root/vmware-keys/MOK.priv /root/vmware-keys/MOK.der /lib/modules/$(uname -r)/misc/vmmon.ko
sudo /usr/src/linux-headers-$(uname -r)/scripts/sign-file sha256 /root/vmware-keys/MOK.priv /root/vmware-keys/MOK.der /lib/modules/$(uname -r)/misc/vmnet.ko

sudo mokutil --import /root/vmware-keys/MOK.der

sudo tee /etc/systemd/system/load-vmware-modules.service > /dev/null <<EOF
[Unit]
Description=Load vmmon and vmmnet after reboot
After=network.target

[Service]
Type=oneshot
ExecStart=/bin/bash -c '/sbin/modprobe vmmon && /sbin/modprobe vmnet'
RemainAfterExit=true

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl enable load-vmware-modules.service

sudo init 6

echo ""

echo "🔁 Mo se riavvia, 'spe"
