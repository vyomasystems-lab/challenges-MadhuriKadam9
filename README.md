# challenges-MadhuriKadam9
challenges-MadhuriKadam9 created by GitHub Classroom
# 1. Mux Design Verification
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.
<img width="830" alt="S1" src="https://user-images.githubusercontent.com/88900482/182027817-d6a61724-564e-4a04-a722-075dedcb33d1.PNG">

## Verification Environment
The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. 
The test drives inputs to the Design Under Test (Mux module here) which has 31 each 4-bit inputs from inp0, inp1 ....to inp30 and gives one 4-bit output *out*
based on the value at select input i.e. sel

The values are assigned to the input port using 
```
dut.inp30.value = 3
dut.sel.value = 30
```
<img width="586" alt="INP30test" src="https://user-images.githubusercontent.com/88900482/182028016-1b8fa43e-444a-477a-aa84-fa339aecbc02.PNG">

The assert statement is used for comparing the Mux's outut to the expected value.

The following error is seen:

<img width="655" alt="mux_bug" src="https://user-images.githubusercontent.com/88900482/182028043-7b5ba61f-fb4c-468c-9f15-6ed95b394d95.PNG">

## Test Scenario **(Important)**
- Test Inputs: inp30=3 sel=30
- Expected Output: out=3
- Observed Output in the DUT dut.out=0

## Design Bug
Based on the above test input and analysing the design, we see the following

Output mismatches for the above inputs proving that there is a design bug

# 2. Sequence Detector Design Verification

