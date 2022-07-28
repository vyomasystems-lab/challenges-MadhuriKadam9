# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for 0 to 7 Inputs"""
    for i in range(5):

     INP0 = random.randint(0, 3)  
     INP1 = random.randint(0, 3)  
     INP2 = random.randint(0, 3)    
     INP3 = random.randint(0, 3)
     INP4 = random.randint(0, 3)
     INP5 = random.randint(0, 3)
     INP6 = random.randint(0, 3)
     INP30 = random.randint(0, 3)
      
     dut.inp0.value = INP0
     dut.inp1.value = INP1
     dut.inp2.value = INP2
     dut.inp3.value = INP3
     dut.inp4.value = INP4
     dut.inp5.value = INP5
     dut.inp6.value = INP6
     dut.inp30.value = INP30

     SEL = 30
     dut.sel.value = SEL
 
     await Timer(2, units='ns')

     dut._log.info(f'INP0={INP0:05} INP1={INP1:05} INP2={INP2:05} INP3={INP3:05} INP4={INP4:05} INP5={INP5:05} INP6={INP6:05} INP30={INP30:05} SEL={SEL:05} model={int(dut.inp30.value):05} DUT={int(dut.out.value):05}')
    assert dut.out.value == dut.inp0.value, "Randomised test failed with: {INP0} = {OUT}".format(INP0=dut.inp0.value,INP1=dut.inp1.value,INP2=dut.inp2.value,INP3=dut.inp3.value, INP4=dut.inp4.value, INP5=dut.inp5.value, INP6=dut.inp6.value, INP30=dut.inp30.value, OUT=dut.out.value)

@cocotb.test()
async def mux_basic_test(dut):
    """Test for INP30"""

    INP30 = 3    
    SEL = 30

    # input driving
    dut.inp30.value = INP30    
    dut.sel.value = SEL

    await Timer(2, units='ns')
    
    assert dut.out.value == INP30, "Mux result is incorrect: {INP30} != {OUT}, expected value={EXP}".format(
            INP30=int(dut.inp30.value), SEL=int(dut.sel.value), OUT=int(dut.out.value), EXP=INP30)




