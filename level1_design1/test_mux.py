# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    for i in range(5):

     INP0 = random.randint(0, 3)  
     INP1 = random.randint(0, 3)  
     INP2 = random.randint(0, 3)    
     INP3 = random.randint(0, 3)
     #INP4 = random.randint(0, 3)
     #INP5 = random.randint(0, 3)
     #INP6 = random.randint(0, 3)
     #INP7 = random.randint(0, 3)
      
     #print('SEL = ',SEL)
     #print(dut.sel)

     dut.inp0.value = INP0
     dut.inp1.value = INP1
     dut.inp2.value = INP2
     dut.inp3.value = INP3
     #dut.inp4.value = INP4
     #dut.inp5.value = INP5
     #dut.inp6.value = INP6
     #dut.inp7.value = INP7

     SEL = 3
     dut.sel.value = SEL
 
     await Timer(2, units='ns')

     dut._log.info(f'INP0={INP0:05} INP1={INP1:05} INP2={INP2:05} INP3={INP3:05}  SEL={SEL:05} model={int(dut.inp3.value):05} DUT={int(dut.out.value):05}')
    assert dut.out.value == dut.inp3.value, "Randomised test failed with: {INP3} = {OUT}".format(INP0=dut.inp0.value,INP1=dut.inp1.value,INP2=dut.inp2.value, INP3=dut.inp3.value, OUT=dut.out.value)
    