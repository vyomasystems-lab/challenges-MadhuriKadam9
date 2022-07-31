# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_wat_vend(dut):
    """Test for water bottle vending """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.rst.value = 1
    dut.clk.value = 0
    await FallingEdge(dut.clk)  
    dut.rst.value = 0
    dut.inp.value = 1     # Rs. 5 Inserted
    await FallingEdge(dut.clk)     
    print(dut.out)       # Rs. 5 Collected but No Bottle
    await FallingEdge(dut.clk)
    dut.inp.value = 2     # Rs. 10 Inserted
    await FallingEdge(dut.clk)
    print(dut.out)        # Total Rs. 15 Collected so Bottle is delivered
            
    assert dut.out.value == 1, f"Water bottle is not delivered"
