from pathlib import Path
import os
import dill

dill.settings["recurse"] = True

POOL_STORE_DIR = Path("pool-store")
os.makedirs(POOL_STORE_DIR, exist_ok=True)

def storePool(obj, varName):
  with open(POOL_STORE_DIR / f"{varName}.pkl", 'wb') as f:
      dill.dump(obj, f, dill.HIGHEST_PROTOCOL)
  
def loadPool(varName, ctx):
    with open(Path("pool-store") / f"{varName}.pkl", 'rb') as f:
        ctx[varName] = dill.load(f)
        