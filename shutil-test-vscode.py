import shutil
import os

print("vscode 설치가 완료되었을것으로 추정되므로, extension을 설치합니다.")


src_path="./vscode-extensions-wosub"
dest_path="C:/Users/girin/.vscode/extensions"

if(not os.path.exists(dest_path)):
    print("extensions 폴더가 존재하지 않습니다. 그냥 붙여넣습니다.")
    shutil.copytree(src_path,dest_path)
else:
    print("원래 존재하는 extensions 폴더를 삭제한 후, 붙여넣습니다.")
    shutil.rmtree(dest_path)
    shutil.copytree(src_path,dest_path)

print("shutil 수행이 완료되었습니다.")