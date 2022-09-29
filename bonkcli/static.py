import os
from pathlib import Path

HOME_FOLDER = Path(os.getenv('HOME'))
CONFIG_FILE = HOME_FOLDER / '.bonkcli'

BANNER = """
    ____              __      ________    ____
   / __ )____  ____  / /__   / ____/ /   /  _/
  / __  / __ \/ __ \/ //_/  / /   / /    / /  
 / /_/ / /_/ / / / / ,<    / /___/ /____/ /   
/_____/\____/_/ /_/_/|_|   \____/_____/___/   """
DOG = """
     AXNN                                                   
  W0OKKO0XXN                                       N0OOOkON 
  KookkkkOOO0W                                  WX0kdxxdll0 
 WOdkkxddxO0xxKW                               XOkkkxkkOkd0W
 WOxOkoooodkOdokN                            XkdxkkxdddxkxON
 NOkOxocccoxkxocoONWWNWW                  WXkoldkxxoolldkkON
 WOkOkoc;;cdkxo:::okxxxkOOO0KKXKK00OOOkkkkdc:cokkdolccldOO0W
 W0OK0xl:;cdkxdooddddxxxxdolccllodddddoooolc:cdkxoc::cok0O0W
  Kk0K0xl;:oxxxxxxxkO00Okxol:clodxxkkkkxddddddxxdc;:ldk00k0W
  0dxkOkdlodxxdddxk0XXKKOkdlccodkOO0KXKOxddddxkkdllldk00kxX 
  XkxkOOkxxxxxxxxOKXXNNXX0Oxodxk0KKXXNXKOkddddxkkkxxkOkkxkN 
  XxoxkkxdddxxxxO000KNNNNXK0OOO0KXNNNXKXXKOkxxxxxkkkO00OO0W 
  W0dxkxdoooolc:;,,:oxO0KK000000KXXK0OxddxkkkkkxdxxkOkkxxK  
  W0xxxddddxxxd:.....;okkkkkkkxkkOOxc'....;dkOkxxxxkkkkxON  
  Xkddxxk0KXK00OxoollxOOOkddxxkkO00kdllccokKXXXK0OOkkkkx0W  
  0lldxOKXNNX0OOO00000kl:,'',,;:d0XX00XXXXXXNWWWWNK0OkxxOW  
  Ocldk0KXNNXK000K0K0d,..........:ONXXXNNXXNWWWWWWNK0kxdOW  
  OldkOKXXXNNXKK0000k:............oKNXXXNNNNWWWWWWNNX0kdkN  
 W0dkO0KKKKKK000OOOOkl'..........:xKXXKKKXNNNWNNNNNNNX0kkX  
  KxxO00000Oxxxkkkkkkxl;'....'',lxOKKKK00KKXXXXXXXXXNXK0OX  
  KddxkO00Oo:;loooddollc:;'';::coxkOOOkkkkOOO0KXNNXXXXXK0X  
  0dddxkOOxc'..',;:;;,''.....'''',:loolc:::::okKXNXXXKKK0KW 
  Kdddxxxxdc'.......................''.......:dOKKKXKKK0kON 
  Xxoddddddl:'.............................':dkOOKKKKK0OxxX 
  Nxodoooddol:'.......'''''.'',,,,'''.....,lxO0K0KKKKK0kodK 
  Ndcoddddddol:,.....:l:;:;,;:;;lo:'....':okOKKKKKKKK0kocxN 
  Wk::oddddddolc;'...'clccccc::col'...,:lxk00KKKKKKK0kocckW 
   Xl;coddxdddooc:,....,;:cc:::;;'.',;cdk00KKKXXXXK0kdl::xN 
   Wx;;codxxxdddol:;,'...........';cloxk00KKKXXXKK0kolc::oKW
   Xo,,:codxxxxxdolc::;'.......',cloxk000KKKXXXK0Oxdlc::ccdX
   0:,,;:cldxkkkxxdoc::;;,,,,;;::cldxkO0KKKXXXK0kdolcc:cccoK
  Wx,',;:::loxkkxxddoc::;;;;;:::clodxkOO000000Oxdoollc:clldK
  Wd,'',;:cllodxxxxdolc::;;;::cclodxxkkOOOOOOkxddoolc::cclxN
"""