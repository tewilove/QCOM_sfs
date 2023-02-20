# SFS path mangling
- sfs\_mkdir(path)
```python
def sfs_mangle(fn):
    hash = hashlib.sha1(fn.encode('utf-8')).digest()
    mn = bytearray(base64.b64encode(hash))
    # Replace "/" with "-", and "=" with "_"
    for i in range(0, len(mn)):
        c = mn[i]
        if c == 0x2f:
            mn[i] = ord('-')
        elif c == 0x3d:
            mn[i] = ord('_')
    mn = mn.decode('utf-8')
    return mn
```
- SFS metadata
  - $(NAME).sfs0
  - $(NAME).sfs%lx
  - $(NAME).b
  - $(NAME).b.sfs%lx
  - $(NAME).index
