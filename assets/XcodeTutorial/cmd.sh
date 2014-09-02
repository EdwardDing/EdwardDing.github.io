curl -O http://www.bobzy.cn/xcode/gen_entitlements.txt
mv gen_entitlements.txt gen_entitlements.py
chmod 777 gen_entitlements.py
sudo mkdir /Applications/Xcode.app/Contents/Developer/iphoneentitlements
sudo mv gen_entitlements.py /Applications/Xcode.app/Contents/Developer/iphoneentitlements/
