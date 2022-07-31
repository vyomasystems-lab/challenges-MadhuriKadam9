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
```
5'b11101: out = inp29;
                            <== No entry for inp30 in design BUG
      default: out = 0;
```

## Design Fix
Updating the design i.e. adding the inp30 entry in design code and re-running the test makes the test pass.

![Bug-fixed](https://user-images.githubusercontent.com/88900482/182028630-93d4ede9-85f5-4192-bc04-3788dfbace8a.PNG)


# 2. Sequence Detector Design Verification
## Verification Environment
The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. 
The test drives inputs to the Design Under Test (Sequence Detector module here) which has 3 each inputs clk, reset and inp_bit and gives High on one bit output *seq_seen* if the said sequence i.e. 1011 is detected.

The values are assigned to the input port using 
```
dut.reset.value = 1
dut.inp_bit.value = 1

```
![OL1011test](https://user-images.githubusercontent.com/88900482/182029249-433469bf-da4e-492e-8503-9325044e42c6.PNG)

## Test Scenario **(Important)**
- Test Inputs: Overlapping sequence 1011011 using timer
- Expected Output: out=0001001
- Observed Output in the DUT dut.out=0001000    It is observed using  print(dut.seq_seen) as shown below

![Seq_det_bug_captured](https://user-images.githubusercontent.com/88900482/182029706-d8a31af4-ba01-44d9-8a4d-8585c4d24da4.PNG)

## Design Bug
Based on the above test input and analysing the design, we see the following
Output mismatches for the above inputs proving that there is a design bug

<img width="264" alt="sol1" src="https://user-images.githubusercontent.com/88900482/182029792-d601c875-85ed-4ae7-8062-7f5a6b154a79.PNG">
<img width="185" alt="sol2" src="https://user-images.githubusercontent.com/88900482/182029797-b96ee1bf-a660-415a-b610-97fb72e8a640.PNG">

## Design Fix
Updating the design i.e. making required changes in design code as shown above and re-running the test makes the test pass. Now It is able to detect overlapping sequence 1011 by printing Seq_seen = 1 two times 

<img width="746" alt="Bug-fixed-test pass" src="https://user-images.githubusercontent.com/88900482/182029881-ed783b09-21e9-4dc5-b9f4-69bb7db933ce.PNG">

