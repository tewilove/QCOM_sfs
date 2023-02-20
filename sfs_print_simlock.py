#!/usr/bin/python

import base64
import hashlib

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

def main():
    simlock = sfs_mangle('simlock')
    files = ['config']
    cats = [
        '3gpp_nw_1', '3gpp_ns_1', '3gpp_sp_1', '3gpp_cp_1',
        '3gpp_sim_1', '3gpp_spn_1', '3gpp_sp_ehplmn_1', '3gpp_iccid_1',
        '3gpp_impi_1', '3gpp_ns_sp_1', '3gpp2_nw_type1_1', '3gpp2_nw_type2_1',
        '3gpp2_ruim_1',
    ]
    for f in cats:
        files.append('catetory_' + f)
    for f in files:
        m = sfs_mangle(f + '.sfs0')
        print("/safe/sfs/uim/simlock/{0} => /safe/sfs/uim/{1}/{2}".format(f, simlock, m))

if __name__ == "__main__":
    main()