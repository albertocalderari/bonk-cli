import os
from pathlib import Path

HOME_FOLDER = Path(os.getenv('HOME'))
CONFIG_FILE = HOME_FOLDER / '.bonkcli'

BANNER = """    ____              __      ________    ____
   / __ )____  ____  / /__   / ____/ /   /  _/
  / __  / __ \/ __ \/ //_/  / /   / /    / /  
 / /_/ / /_/ / / / / ,<    / /___/ /____/ /   
/_____/\____/_/ /_/_/|_|   \____/_____/___/   
"""

DOG = """
      0O                                              00       
   OoOOOoOOO                                       Ooooo*O  
   o*oooooOooO                                   Ooooooo**  
   *oOoooooOO*o                                OoooooooOoo  
  OoOoo*o*ooOo**O                            O*oooooooooooO 
  OoOoo****oooo**oO                        Oo**ooooo***oooO 
  Ooooo*****ooo**°*ooooooooOOOOOOOOooooooo****oooo*****oOoO 
  OoOOoo***oooo**oooooooooo*****ooooo*********ooo*****ooOoO 
   oOOOoo*°*oooooooooOOOoooo***oooooooooooooooooo*°**ooOOoO 
   o*OoOo***ooooooooOOOOOoo****oooOOOOOooooooooo***ooOOOoo  
   OoooOOooooooooooOOOOOOOOo**ooOOOOOOOOoooooooooooooooooO  
   O*ooooooooooooOOOOOO OOOOoooOOOO OOOOOOooooooooooOOOooO  
   O*ooooo**oo**o***oOOOOOOOOOOOOOOOOOoOOOOoooooooooooooo   
    ooooo***oo**...°.°*oooooooooOOo**°°°°°*oooooooooooooO   
   OoooooooOOOOOo*°°°*oooOoooooooooo°°°°°°oOOOOooooooooo    
   o*ooooOOOOOooOOOOoOOOo*****ooOOOOoOOOOOOOO##OOOOoooooO   
   ***ooOOOOOOOooOOOOOo°°.°°°°°°*OOOOOOOOOOO#####OOOooooO   
   **oooOOOOOOOOOOOOOo°...°°°°...°OOOOOOOOO#######OOOoooO   
   *ooOOOOOOOOOOOoOOOo°.°°.°°°°°.°OOOOOOOOO########OOOooO   
   ooOOOOOOOOOooOooooo*°°....°°°*oOOOOOOOOOOOOOOOOOOOOOoO   
   ooooOOOOoooooooooooo**°°°°°**ooOOOOOOoOOOOOOOOOOOOOOoO   
   oooooOOOo*°°***oo*******°°***oooooooooooooOOOOOOOOOOOO   
   oooooooo*°..°°°*°°°°°°°°..°°°°°******°°°°°*oOOOOOOOOOoO  
   oooooooo**°......°°°°..°°...°°°°°°°°.....°*oOOOOOOOOOoO  
   o*ooooooo**°.....°°.°°°°°°°°°°°.°°..°°°°*ooooOOOOOOOo*o  
   O*ooo*oooo**°....°°°°°°°°°°°°°°°°°°°°°°*ooOOOOOOOOOoo*o  
   O**oooooooo**°°°°°°o****°°***oo°°°°°°°*ooOOOOOOOOOoo**O  
    ***oooooooo**°°°°°**********o°°°°°**ooOOOOOOOOOOoo***O  
    o°**oooooooo**°°°°°°°*******°°°°°**oOOOOOOOOOOOOo****O  
     ****oooooooo***°°°...°°°°°.°°***ooOOOOOOOOOOOOo*****o  
    O°°°**oooooooo*****°°°...°°°***ooOOOOOOOOOOOOoo*******O 
    o°°****ooooooooo******°°°°****oooOOOOOOOOOOOoo********o 
   O*°°°*****oooooooo**************ooooOOOOOOOooo*********o 
   O°°°°******ooooooo***********oooooooooOOOoooooo********O 
"""