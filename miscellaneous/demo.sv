// @see https://www.chipverify.com/verification/codehub
// @file 170_systemverilog_while_and_do-while_loop_ex0.sv
//--------------------------------------------------
// Copyright (c) 2019 ChipVerify. All Rights Reserved.
// Author   : Admin
// Article  : SystemVerilog while and do-while loop
// Category : SystemVerilog
//--------------------------------------------------

//----------------------------------
//             Testbench
//----------------------------------

// Author  : Admin, ChipVerify
// Website : www.chipverify.com

module tb;
    initial begin
        int cnt = 0;
        do begin
            $display("cnt = %0d", cnt);
            cnt++;
        end while (cnt < 5);
    end
endmodule
