import subprocess

benchmarks = [["../bzip2/bzip2_base.i386-m32-gcc42-nn", "../bzip2/dryer.jpg"],["../mcf/mcf_base.i386-m32-gcc42-nn", "../mcf/inp.in"],["../hmmer/hmmer_base.i386-m32-gcc42-nn", "../hmmer/bombesin.hmm"],["../sjeng/sjeng_base.i386-m32-gcc42-nn", "../sjeng/test.txt"],["../milc/milc_base.i386-m32-gcc42-nn", "<", "../milc/su3imp.in"],["../equake/equake_base.pisa_little", "<", "../equake/inp.in", ">", "../equake/inp.out"]]

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
    