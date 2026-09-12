"""Check an offline dependency/license manifest against policy."""
from __future__ import annotations
def check(dependencies:list[dict],allowed:list[str],denied:list[str]|None=None)->dict:
 allowed_set,denied_set=set(allowed),set(denied or []);issues=[]
 for item in dependencies:
  name=str(item.get('name','unknown'));license=item.get('license')
  if not license:issues.append({'name':name,'issue':'missing license'})
  elif license in denied_set:issues.append({'name':name,'issue':'denied license','license':license})
  elif allowed_set and license not in allowed_set:issues.append({'name':name,'issue':'not allowlisted','license':license})
 return {'dependencies':len(dependencies),'issues':issues}
if __name__=='__main__':
 import json,sys;p=json.load(sys.stdin);print(json.dumps(check(p['dependencies'],p.get('allowed',[]),p.get('denied')),indent=2))
