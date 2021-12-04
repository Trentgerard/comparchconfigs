import subprocess
import os
benchmarks = [["./bzip2/bzip2_base.i386-m32-gcc42-nn", "./bzip2/dryer.jpg"],["./mcf/mcf_base.i386-m32-gcc42-nn", "./mcf/inp.in"],["./hmmer/hmmer_base.i386-m32-gcc42-nn", "./hmmer/bombesin.hmm"],["./sjeng/sjeng_base.i386-m32-gcc42-nn", "./sjeng/test.txt"],["./milc/milc_base.i386-m32-gcc42-nn", "<", "./milc/su3imp.in"],["./equake/equake_base.pisa_little", "<", "./equake/inp.in", ">", "./equake/inp.out"]]

benckmarknames = ["bzip_out","mcf_out","hmmer_out","sjeng_out","milc_out","equake_out"]

configs = ["./tmps/a/tmp.cfg","./tmps/b/tmp.cfg","./tmps/c/tmp.cfg","./tmps/d/tmp.cfg","./tmps/e/tmp.cfg","./tmps/f/tmp.cfg","./tmps/g/tmp.cfg","./tmps/h/tmp.cfg","./tmps/i/tmp.cfg","./tmps/j/tmp.cfg","./tmps/k/tmp.cfg"]

basefunc = ["$SIMPLESIM/simplesim-3.0/sim-outorder", "-config"] 

i = 0
for folder in benckmarknames:
    #subprocess.run(["mkdir",folder])
    #os.system("cd "+folder)
    j = 1
    for config in configs:
        #subprocess.run(["cp",config,"tmp.cfg"])
        pid = os.fork()
        if pid:
            os.wait()
            os.system("echo "+config+" completed")
            j += 1
        else:
            os.system("echo "+config+" in progress")
            command = ["$SIMPLESIM/simplesim-3.0/sim-outorder", "-config"] + [config] + benchmarks[i]
            command = " ".join(command)
            os.system(command)
            os.system("echo exiting")
            os.system("cp sim1.out ./"+folder+"/sim"+str(j)+".out")
            exit()
            #subprocess.run(["rm","tmp.cfg"])   
    i += 1
    #os.system("cd ..")
    