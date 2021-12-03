import subprocess

benchmarks = [["bzip2_base.i386-m32-gcc42-nn", "dryer.jpg"],["mcf_base.i386-m32-gcc42-nn", "inp.in"],["hmmer_base.i386-m32-gcc42-nn", "bombesin.hmm"],["sjeng_base.i386-m32-gcc42-nn", "test.txt"],["milc_base.i386-m32-gcc42-nn", "<", "su3imp.in"],["equake_base.pisa_little", "<", "inp.in", ">", "inp.out"]]

benckmarknames = ["bzip_out","mcf_out","hmmer_out","sjeng_out","milc_out","equake_out"]

configs = ["../tmps/tmp1.cfg","../tmps/tmp2.cfg","../tmps/tmp3.cfg","../tmps/tmp4.cfg","../tmps/tmp5.cfg","../tmps/tmp6.cfg","../tmps/tmp7.cfg","../tmps/tmp8.cfg","../tmps/tmp9.cfg","../tmps/tmp10.cfg","../tmps/tmp11.cfg"]

basefunc = ["$SIMPLESIM/simplesim-3.0/sim-outorder", "-config"] 

i = 0
for folder in benckmarknames:
    subprocess.run(["mkdir",folder])
    subprocess.run(["cd",folder])
    for config in configs:
        command = basefunc + [config] + benchmarks[i]
        subprocess.run(command)
    i += 1
    subprocess.run(["cd",".."])
    